"""Generates statistics and markdown files from tournament data."""
from __future__ import annotations

import html
from datetime import datetime
from typing import Any, Dict, List, Optional, TextIO, Tuple

from roman_arabic_numerals import conv

from counting import constants
from counting.country_registry import (
    get_country_genitive,
    get_country_title,
    get_country_header,
    get_markdown_output_path,
    validate_country_slug,
)
from counting.entity_registry import EntityIdAllocator, EntityRegistry
from counting.external_ids import (
    merge_external_ids,
    missing_data_tournament_url,
    parse_external_id_from_results_url,
    resolve_results_url,
    results_markdown_label,
)
from counting.data_errors import (
    collect_computed_errors,
    empty_errors,
    flatten_tournaments,
    is_critical_error,
    merge_data_errors,
    normalize_errors,
    sort_error_items,
    tournament_is_past,
)
from counting.google_sheets_exporter import GoogleSheetsExporter
from counting.languages import language_phrase, normalize_languages
from counting.models import Awardee, MetaData, Player, Team, TournamentAwardee, TournamentData
from counting.processors import count_champions, medal_column_groups
from counting.sheet_utils import (
    default_links,
    merge_links,
    normalize_age,
    player_profile_url,
    team_profile_url,
)
from counting.t_fashion import (
    format_date_for_tournament,
    iso_date_is_past,
    parse_russian_date,
    parse_russian_date_range,
    to_iso_date,
    tournament_display_date,
)
from counting.tournament_processor import TournamentProcessor

# Tab UI for country pages. Markers wrap markdown so Goldmark can still parse it;
# JS moves those nodes into panels. Intro stays outside the tab bar.
_COUNTRY_TABS_HEAD = """<style>
.country-tab-bar{display:flex;flex-wrap:wrap;gap:.25rem .15rem;margin:1.25rem 0 1rem;border-bottom:1px solid color-mix(in srgb,currentColor 35%,transparent)}
.country-tab-bar button{appearance:none;background:none;border:0;border-bottom:2px solid transparent;margin-bottom:-1px;padding:.45rem .85rem;cursor:pointer;font:inherit;color:inherit}
.country-tab-bar button.is-active{border-bottom-color:currentColor;font-weight:600}
.country-tab-hide-until-ready~*:not(.country-always-visible){display:none}
</style>
<script>
(function(){
function wrapTabs(){
  var starts=document.querySelectorAll(".country-tab-start");
  if(!starts.length)return;
  starts.forEach(function(start){
    var id=start.getAttribute("data-tab");
    var panel=document.createElement("div");
    panel.className="country-tab-panel";
    panel.id="country-tab-"+id;
    panel.setAttribute("role","tabpanel");
    var node=start.nextSibling;
    while(node){
      var next=node.nextSibling;
      if(node.nodeType===1&&node.classList&&node.classList.contains("country-tab-end")){
        node.remove();
        break;
      }
      if(node.nodeType===1&&node.classList&&node.classList.contains("country-tab-start"))break;
      panel.appendChild(node);
      node=next;
    }
    start.parentNode.insertBefore(panel,start);
    start.remove();
  });
  var hide=document.querySelector(".country-tab-hide-until-ready");
  if(hide)hide.remove();
  var buttons=document.querySelectorAll(".country-tab-bar [data-tab]");
  function show(id){
    document.querySelectorAll(".country-tab-panel").forEach(function(p){
      p.hidden=p.id!=="country-tab-"+id;
    });
    buttons.forEach(function(b){
      var on=b.getAttribute("data-tab")===id;
      b.classList.toggle("is-active",on);
      b.setAttribute("aria-selected",on?"true":"false");
    });
  }
  buttons.forEach(function(b){
    b.addEventListener("click",function(){show(b.getAttribute("data-tab"));});
  });
  function findTarget(hash){
    if(!hash)return null;
    function match(root){
      if(!root)return null;
      var el=root.getElementById?root.getElementById(hash):null;
      if(el)return el;
      if(root.querySelector){
        try{
          el=root.querySelector('[id="'+hash+'"], [name="'+hash+'"]');
          if(el)return el;
        }catch(e){}
      }
      var named=(root.getElementsByName?root.getElementsByName(hash):[]);
      if(named&&named.length)return named[0];
      return null;
    }
    var visible=document.querySelector(".country-tab-panel:not([hidden])");
    var el=match(visible)||match(document);
    if(el)return el;
    try{
      var decoded=decodeURIComponent(hash);
      if(decoded!==hash){
        hash=decoded;
        visible=document.querySelector(".country-tab-panel:not([hidden])");
        return match(visible)||match(document);
      }
    }catch(e){}
    return null;
  }
  function tabFromHash(){
    var hash=(location.hash||"").replace(/^#/,"");
    if(!hash)return buttons[0]&&buttons[0].getAttribute("data-tab");
    if(document.getElementById("country-tab-"+hash))return hash;
    var el=findTarget(hash);
    if(el){
      var panel=el.closest(".country-tab-panel");
      if(panel&&panel.id.indexOf("country-tab-")===0)return panel.id.slice("country-tab-".length);
    }
    return buttons[0]&&buttons[0].getAttribute("data-tab");
  }
  function reveal(){
    show(tabFromHash());
    var el=findTarget((location.hash||"").replace(/^#/,""));
    if(el)window.requestAnimationFrame(function(){el.scrollIntoView();});
  }
  reveal();
  window.addEventListener("hashchange",reveal);
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",wrapTabs);
else wrapTabs();
})();
</script>
"""


class StatsGenerator:
    """Generates statistics and markdown files from tournament data."""

    def __init__(
        self,
        country: str,
        read_only_sheets: bool = False,
    ):
        self.country = country
        self.age = constants.DEFAULT_AGE
        self.read_only_sheets = read_only_sheets
        self.processor = TournamentProcessor()
        self.allocator = EntityIdAllocator()
        self.registry = EntityRegistry(self.allocator)
        exporter = GoogleSheetsExporter()
        if exporter.is_available():
            self.allocator.load_from_exporter(exporter)

    def generate_stats(
        self,
        tournament_ids: List[str],
        number_champ: Optional[int] = None,
        game: str = constants.DEFAULT_GAME,
    ) -> None:
        if number_champ is None:
            number_champ = len(tournament_ids)

        # Stop right away if the country is not in COUNTRY_REGISTRY,
        # instead of failing after all tournaments have been downloaded.
        validate_country_slug(self.country)

        if game in constants.INDIVIDUAL_GAMES:
            self._reject_individual_api(game)
            return

        team_stats: Dict[int, Awardee] = {}
        player_stats: Dict[int, Awardee] = {}
        tournaments_data: Dict[str, List[TournamentData]] = {}
        errors = empty_errors()
        numbers_champ = {game: number_champ}

        for tournament_id in tournament_ids:
            tournament_result = self._process_single_tournament(
                number_champ=number_champ,
                team_stats=team_stats,
                player_stats=player_stats,
                errors=errors,
                game=game,
                tournament_id=tournament_id,
            )
            if tournament_result:
                team_stats, player_stats, errors, tournament_data = tournament_result
                tournaments_data.setdefault(tournament_data.game, []).append(tournament_data)
                number_champ -= 1

        self._save_results(
            numbers_champ, team_stats, player_stats, tournaments_data, errors,
            generate_intro=True,
        )

    def recalculate_from_tournaments(
        self,
        tournaments_data: Dict[str, List[TournamentData]],
    ) -> Tuple[Dict[int, Awardee], Dict[int, Awardee], Dict[str, List[TournamentData]], Dict[str, Any]]:
        """Recompute team/player stats from stored tournament rows."""
        self._seed_registry_from_tournaments(tournaments_data)
        team_stats: Dict[int, Awardee] = {}
        player_stats: Dict[int, Awardee] = {}
        errors = empty_errors()
        result: Dict[str, List[TournamentData]] = {}

        for game_type, tournament_list in tournaments_data.items():
            result[game_type] = []
            for tournament in tournament_list:
                if tournament.awardees:
                    processed = self._process_single_tournament(
                        number_champ=tournament.number,
                        team_stats=team_stats,
                        player_stats=player_stats,
                        errors=errors,
                        game=tournament.game,
                        tournament_data=tournament,
                    )
                    if processed:
                        team_stats, player_stats, errors, processed_tournament = processed
                        result[game_type].append(processed_tournament)
                    else:
                        result[game_type].append(tournament)
                else:
                    if not tournament.id:
                        tournament.id = self.registry.resolve_tournament_id(tournament.external_ids)
                    result[game_type].append(tournament)

        for game_type in result:
            result[game_type] = sorted(result[game_type], key=lambda t: t.number, reverse=True)
        return team_stats, player_stats, result, errors

    def build_output_data(
        self,
        numbers_champ: Dict[str, int],
        team_stats: Dict[int, Awardee],
        player_stats: Dict[int, Awardee],
        tournaments_data: Dict[str, List[TournamentData]],
        errors: Dict[str, Any],
        meta: Optional[MetaData] = None,
        intro: Optional[str] = None,
    ) -> Dict[str, Any]:
        time_dump = datetime.now().isoformat()
        total_tournaments = sum(len(v) for v in tournaments_data.values())
        if intro is not None:
            intro_text = intro.strip()
        elif isinstance(meta, MetaData):
            intro_text = (meta.intro or "").strip()
        elif isinstance(meta, dict):
            intro_text = str(meta.get("intro") or "").strip()
        else:
            intro_text = ""
        age = self._resolve_age(meta)
        self.age = age
        meta_obj = MetaData(
            country=self.country,
            generated_at=time_dump,
            statistics={
                "team_count": len(team_stats),
                "player_count": len(player_stats),
                "tournament_count": total_tournaments,
            },
            numbers_champ=numbers_champ,
            intro=intro_text,
            age=age,
        )
        return {
            "teams": {str(i): t.to_dict() for i, t in self.registry.teams.items()},
            "players": {str(i): p.to_dict() for i, p in self.registry.players.items()},
            "tournaments": {
                game: [t.to_dict() for t in lst] for game, lst in tournaments_data.items()
            },
            "meta": meta_obj.to_dict(),
            "errors": errors,
        }

    def _seed_registry_from_tournaments(
        self, tournaments_data: Dict[str, List[TournamentData]]
    ) -> None:
        """Register known entities so later API imports can match by external id."""
        for tournament_list in tournaments_data.values():
            for tournament in tournament_list:
                if tournament.id or tournament.external_ids:
                    tournament.id = self.registry.observe_tournament_ids(
                        tournament.id, tournament.external_ids
                    )
                for awardee in tournament.awardees.values():
                    resolved_players = [
                        self._resolve_roster_player(player) for player in awardee.team.players
                    ]
                    if awardee.individual or tournament.game in constants.INDIVIDUAL_GAMES:
                        display = (
                            resolved_players[0].roster_display_name()
                            if resolved_players
                            else awardee.team.name
                        )
                        awardee.team = Team(
                            id=0, name=display, city="", players=resolved_players
                        )
                        awardee.individual = True
                        continue
                    registered = self.registry.observe_team(awardee.team)
                    awardee.team = self._snapshot_team(registered, resolved_players)

    def _save_results(
        self,
        numbers_champ: Dict[str, int],
        team_stats: Dict[int, Awardee],
        player_stats: Dict[int, Awardee],
        tournaments_data: Dict[str, List[TournamentData]],
        errors: Dict[str, Any],
        meta: Optional[MetaData] = None,
        generate_intro: bool = False,
    ) -> None:
        intro = ""
        if isinstance(meta, MetaData):
            intro = meta.intro or ""
        elif isinstance(meta, dict):
            intro = str(meta.get("intro") or "")
        if generate_intro and not intro.strip():
            intro = self._default_intro(tournaments_data)
        errors = self._finalize_errors(tournaments_data, errors)
        output_data = self.build_output_data(
            numbers_champ, team_stats, player_stats, tournaments_data, errors,
            meta=meta, intro=intro,
        )

        exporter = GoogleSheetsExporter()
        if exporter.is_available():
            if not self.read_only_sheets:
                print(f"Exporting to Google Sheets worksheet: {self.country}")
                exporter.export_data(self.country, output_data)
                self.allocator.persist_to_exporter(exporter)
            exporter.write_public_json()
        else:
            print("Google Sheets is not available; public JSON not updated.")

        self._generate_markdown_files(
            team_stats, player_stats, tournaments_data, errors, intro=intro,
        )

    def _load_from_sheets(self) -> Optional[Dict[str, Any]]:
        exporter = GoogleSheetsExporter()
        if not exporter.is_available():
            print("Google Sheets is not available.")
            return None
        data = exporter.load_data(self.country)
        if data:
            self._seed_registry_from_loaded(data)
        return data

    def _seed_registry_from_loaded(self, data: Dict[str, Any]) -> None:
        for raw in (data.get("teams") or {}).values():
            team = Team.from_dict(raw) if isinstance(raw, dict) else raw
            self.registry.observe_team(team)
        for raw in (data.get("players") or {}).values():
            player = Player.from_dict(raw) if isinstance(raw, dict) else raw
            self.registry.observe_player(player)
        self._seed_registry_from_tournaments(data.get("tournaments") or {})

    def add_tournament(self, tournament_id: str, game: str = constants.DEFAULT_GAME) -> bool:
        if game in constants.INDIVIDUAL_GAMES:
            self._reject_individual_api(game)
            return False
        data = self._load_from_sheets()
        if not data:
            return False
        meta = data["meta"]
        next_champ_number, numbers_champ = self._get_next_championship_number(meta.numbers_champ, game)

        team_stats, player_stats, tournaments_data, errors = self.recalculate_from_tournaments(
            data["tournaments"]
        )
        tournament_result = self._process_single_tournament(
            number_champ=next_champ_number,
            team_stats=team_stats,
            player_stats=player_stats,
            errors=errors,
            game=game,
            tournament_id=tournament_id,
        )
        if not tournament_result:
            return False
        team_stats, player_stats, errors, new_tournament = tournament_result
        tournaments_data.setdefault(new_tournament.game, []).append(new_tournament)
        for game_type in tournaments_data:
            tournaments_data[game_type] = sorted(
                tournaments_data[game_type], key=lambda t: t.number, reverse=True
            )
        self._save_results(
            numbers_champ, team_stats, player_stats, tournaments_data,
            data.get("errors"),
            meta=meta, generate_intro=True,
        )
        return True

    def add_empty_tournament(
        self, date: str, country: str, place: Optional[str] = None, game: str = constants.DEFAULT_GAME
    ) -> bool:
        data = self._load_from_sheets()
        if not data:
            return False
        meta = data["meta"]
        next_champ_number, numbers_champ = self._get_next_championship_number(meta.numbers_champ, game)
        try:
            day, month, year = parse_russian_date(date)
            start_date = to_iso_date(day, month, year)
            end_date = start_date
            formatted_date = format_date_for_tournament(day, month, year)
        except ValueError:
            try:
                start_date, end_date = parse_russian_date_range(date)
                formatted_date = tournament_display_date(start_date, end_date)
                year = int(end_date[:4])
            except ValueError as exc:
                print(str(exc))
                return False

        team_stats, player_stats, tournaments_data, errors = self.recalculate_from_tournaments(
            data["tournaments"]
        )
        empty_tournament = TournamentData(
            id=self.registry.resolve_tournament_id({}),
            number=next_champ_number,
            date=formatted_date,
            start_date=start_date,
            end_date=end_date,
            city=place or "",
            year=year,
            game=game,
            links=default_links(),
        )
        tournaments_data.setdefault(game, []).append(empty_tournament)
        for game_type in tournaments_data:
            tournaments_data[game_type] = sorted(
                tournaments_data[game_type], key=lambda t: t.number, reverse=True
            )
        self._save_results(
            numbers_champ, team_stats, player_stats, tournaments_data,
            data.get("errors"),
            meta=meta, generate_intro=True,
        )
        return True

    def update_tournament(
        self,
        update_type: str,
        update_info: str,
        game: Optional[str] = None,
    ) -> bool:
        data = self._load_from_sheets()
        if not data:
            return False
        meta = data["meta"]
        team_stats, player_stats, tournaments_data, errors = self.recalculate_from_tournaments(
            data["tournaments"]
        )

        target = self._pick_tournament_for_update(tournaments_data, game, update_type)
        if not target:
            return False

        updated = False
        if update_type == "ts":
            tournament_result = self._process_single_tournament(
                number_champ=target.number,
                team_stats=team_stats,
                player_stats=player_stats,
                errors=errors,
                game=target.game,
                tournament_id=int(update_info),
            )
            if not tournament_result:
                return False
            team_stats, player_stats, errors, tournament_with_results = tournament_result
            target.awardees = tournament_with_results.awardees
            target.countable = tournament_with_results.countable
            # Languages typed into the sheet by hand win over the API.
            if not target.languages:
                target.languages = list(tournament_with_results.languages)
            target.external_ids = merge_external_ids(
                target.external_ids, tournament_with_results.external_ids
            )
            if tournament_with_results.id:
                target.id = tournament_with_results.id
            if tournament_with_results.links.get("results"):
                target.links["results"] = tournament_with_results.links["results"]
            updated = True
        elif update_type == "results":
            target.links["results"] = update_info
            target.external_ids = merge_external_ids(
                target.external_ids,
                parse_external_id_from_results_url(update_info),
            )
            updated = True
        elif update_type in (
            "tg", "fb", "vk", "site", "recap", "letopis", "announce",
            "photos", "questions",
        ):
            target.links[update_type] = update_info
            updated = True
        elif update_type == "place":
            target.city = update_info
            updated = True

        if not updated:
            return False
        self._save_results(
            meta.numbers_champ, team_stats, player_stats, tournaments_data,
            data.get("errors"),
            meta=meta,
        )
        return True

    @staticmethod
    def _pick_tournament_for_update(
        tournaments_data: Dict[str, List[TournamentData]],
        game: Optional[str],
        update_type: str,
    ) -> Optional[TournamentData]:
        """Choose which edition `-u` should change.

        Link/city updates (`results`, `tg`, …) can land on an already-filled
        edition of the requested game so SSI (Individuals already entered) still
        picks up sheet/CLI extras the same way as team games. `-u ts` still
        requires an empty edition so a refetch does not wipe podium rows.
        """
        link_or_place = update_type in (
            "results", "tg", "fb", "vk", "site", "recap", "letopis",
            "announce", "photos", "questions", "place",
        )

        def newest_empty(game_key: str) -> Optional[TournamentData]:
            empty = [t for t in tournaments_data.get(game_key, []) if not t.awardees]
            if not empty:
                return None
            return sorted(empty, key=lambda t: t.number, reverse=True)[0]

        def newest(game_key: str) -> Optional[TournamentData]:
            lst = tournaments_data.get(game_key, [])
            if not lst:
                return None
            return sorted(lst, key=lambda t: t.number, reverse=True)[0]

        if game:
            empty = newest_empty(game)
            if empty:
                return empty
            if link_or_place:
                found = newest(game)
                if found:
                    return found
            print(f"No tournament found to update for game {game}.")
            return None

        for tournament_list in tournaments_data.values():
            for tournament in sorted(tournament_list, key=lambda t: t.number, reverse=True):
                if not tournament.awardees:
                    if (
                        update_type == "ts"
                        and tournament.game in constants.INDIVIDUAL_GAMES
                    ):
                        continue
                    return tournament
        print("No empty tournament found to update.")
        return None

    def update_from_google_sheets(self) -> bool:
        data = self._load_from_sheets()
        if not data:
            return False
        meta = data["meta"]
        team_stats, player_stats, tournaments_data, errors = self.recalculate_from_tournaments(
            data["tournaments"]
        )
        self._save_results(
            meta.numbers_champ, team_stats, player_stats, tournaments_data,
            data.get("errors"),
            meta=meta,
        )
        return True

    def _get_next_championship_number(
        self, numbers_champ: Dict[str, int], game: str
    ) -> Tuple[int, Dict[str, int]]:
        if game not in numbers_champ:
            numbers_champ[game] = 0
        numbers_champ[game] += 1
        return numbers_champ[game], numbers_champ

    def _process_single_tournament(
        self,
        number_champ: int,
        team_stats: Dict[int, Awardee],
        player_stats: Dict[int, Awardee],
        errors: Dict[str, Any],
        game: str = constants.DEFAULT_GAME,
        tournament_id: Optional[str] = None,
        tournament_data: Optional[TournamentData] = None,
    ) -> Optional[Tuple[Dict[int, Awardee], Dict[int, Awardee], Dict[str, Any], TournamentData]]:
        if tournament_data is not None:
            info = {"year": tournament_data.year}
            source = tournament_data
            if not source.id:
                source.id = self.registry.resolve_tournament_id(source.external_ids)
            else:
                source.id = self.registry.observe_tournament_ids(source.id, source.external_ids)
            tid = tournament_id or source.links.get("results", "") or str(source.id)
        else:
            if tournament_id is None:
                return None
            info, results = self.processor.process_tournament(int(tournament_id))
            if not info or not results:
                return None
            ts_external = {constants.EXTERNAL_ID_TS: str(tournament_id)}
            internal_tournament_id = self.registry.resolve_tournament_id(ts_external)
            awardees_by_place: Dict[int, TournamentAwardee] = {}
            for place, raw_team in self._rank_results(results):
                if place >= constants.TOP_PLACES:
                    break
                raw = self.processor.extract_team_data(raw_team)
                players = [
                    self.registry.resolve_player(
                        name=p.name,
                        surname=p.surname,
                        external_ids=p.external_ids,
                    )
                    for p in raw.players
                ]
                team = self.registry.resolve_team(
                    name=raw.name,
                    city=raw.city,
                    external_ids=raw.external_ids,
                    players=players,
                )
                awardees_by_place[len(awardees_by_place)] = TournamentAwardee(
                    team=team, place=place, roster_complete=bool(team.players)
                )
            if not awardees_by_place:
                print(f"No podium teams found in tournament {tournament_id}")
            source = TournamentData(
                id=internal_tournament_id,
                number=number_champ,
                date=info["date"],
                start_date=info.get("start_date", ""),
                end_date=info.get("end_date", ""),
                city=info["city"],
                year=info["year"],
                game=game,
                awardees=awardees_by_place,
                links=merge_links(
                    {"results": f"https://rating.chgk.info/tournament/{tournament_id}"}
                ),
                external_ids=ts_external,
                # Podium fetched from the API is a real championship result,
                # so it counts unless the sheet is later edited to say no.
                countable=True,
                languages=normalize_languages(info.get("languages")),
            )
            tid = str(tournament_id)

        processed = TournamentData(
            id=source.id,
            number=number_champ,
            date=source.date,
            start_date=source.start_date,
            end_date=source.end_date,
            city=source.city,
            year=source.year,
            game=source.game,
            awardees={},
            links=merge_links(source.links),
            external_ids=dict(source.external_ids),
            countable=source.countable,
            languages=list(source.languages),
            display_name=source.display_name,
            comment=source.comment,
        )

        for _, awardee in sorted(
            source.awardees.items(), key=lambda item: (item[1].place, item[0])
        ):
            place = awardee.place
            if place >= constants.TOP_PLACES:
                continue
            # Ensure internal ids when reprocessing sheet-loaded rows.
            # Keep per-tournament old_* on the roster copy (not on the registry).
            resolved_players = [
                self._resolve_roster_player(player) for player in awardee.team.players
            ]
            is_individual = (
                awardee.individual or game in constants.INDIVIDUAL_GAMES
            )
            if is_individual:
                display = (
                    resolved_players[0].roster_display_name()
                    if resolved_players
                    else awardee.team.name
                )
                resolved_awardee = TournamentAwardee(
                    team=Team(id=0, name=display, city="", players=resolved_players),
                    place=place,
                    old_name=awardee.old_name,
                    roster_complete=bool(resolved_players),
                    individual=True,
                    sex=awardee.sex,
                )
            else:
                registered = (
                    self.registry.observe_team(awardee.team)
                    if awardee.team.id
                    else self.registry.resolve_team(
                        name=awardee.team.name,
                        city=awardee.team.city,
                        external_ids=awardee.team.external_ids,
                        players=[],
                    )
                )
                if awardee.team.non_russian_name and not registered.non_russian_name:
                    registered.non_russian_name = awardee.team.non_russian_name
                resolved_awardee = TournamentAwardee(
                    team=self._snapshot_team(registered, resolved_players),
                    place=place,
                    old_name=awardee.old_name,
                    roster_complete=awardee.roster_complete,
                )
            team_stats, player_stats, errors = self._apply_awardee_stats(
                team_stats,
                player_stats,
                errors,
                resolved_awardee,
                place,
                game,
                info,
                processed,
                tid,
            )
            processed.awardees[len(processed.awardees)] = resolved_awardee
        return team_stats, player_stats, errors, processed

    @staticmethod
    def _rank_results(results: List[Dict[str, Any]]) -> List[Tuple[int, Dict[str, Any]]]:
        """Order raw API results by tournament position and derive 0-based places.

        Uses competition ranking: teams sharing the same ``position`` value
        share the same place, so ties are not broken arbitrarily by list order.
        A team's place equals the number of teams that finished strictly ahead.
        """
        positions: List[float] = []
        for index, raw_team in enumerate(results):
            try:
                position = float(raw_team.get("position"))
            except (TypeError, ValueError):
                position = float(index + 1)
            positions.append(position)
        order = sorted(range(len(results)), key=lambda i: (positions[i], i))
        return [
            (sum(1 for p in positions if p < positions[i]), results[i])
            for i in order
        ]

    def _apply_awardee_stats(
        self,
        team_stats: Dict[int, Awardee],
        player_stats: Dict[int, Awardee],
        errors: Dict[str, Any],
        awardee: TournamentAwardee,
        place: int,
        game: str,
        info: Dict[str, Any],
        processed_tournament: TournamentData,
        tournament_id: str,
    ) -> Tuple[Dict[int, Awardee], Dict[int, Awardee], Dict[str, Any]]:
        team = awardee.team
        # Only countable tournaments award medals. Missing rosters still appear
        # in the Errors section / Нет данных tab.
        if processed_tournament.countable:
            if game not in constants.INDIVIDUAL_GAMES:
                team_stats = count_champions(
                    team_stats,
                    team.id,
                    place,
                    game=game,
                    name=team.name,
                    city=team.city,
                    external_ids=team.external_ids,
                    non_russian_name=team.non_russian_name,
                )
            for player in team.players:
                player_stats = count_champions(
                    player_stats,
                    player.id,
                    place,
                    game=game,
                    name=f"{player.name} {player.surname}",
                    city=team.city,
                    external_ids=player.external_ids,
                )

        return team_stats, player_stats, errors

    @staticmethod
    def _needs_roster_error(awardee: TournamentAwardee) -> bool:
        if awardee.individual:
            return awardee.individual_player() is None
        return not awardee.roster_complete


    def _generate_markdown_files(
        self,
        team_stats: Dict[int, Awardee],
        player_stats: Dict[int, Awardee],
        tournaments_data: Dict[str, List[TournamentData]],
        errors: Dict[str, Any],
        intro: str = "",
    ) -> None:
        dest = get_markdown_output_path(self.country)
        dest.parent.mkdir(parents=True, exist_ok=True)

        country_title = get_country_title(self.country)
        country_header = get_country_header(self.country)
        preamble = f"---\ntitle: {country_title}\nweight: 1\nbookToC: false\n---\n\n# {country_header}\n\n"
        if intro:
            preamble += f"{intro}\n\n"
        game_types = self._ordered_game_types(tournaments_data)
        sections = self._year_section_keys(game_types)
        tabs = [
            (constants.TEAMS_ANCHORS, constants.TEAMS_CONTEXT),
            (constants.PLAYERS_ANCHORS, constants.PLAYERS_CONTEXT),
        ]
        for section in sections:
            tabs.append((
                self._game_tab_id(section),
                self._tournament_tab_label(section, len(sections), game_types),
            ))
        extra_description, missing_rows = self._missing_data_content(
            errors, tournaments_data
        )
        if extra_description or missing_rows:
            tabs.append((constants.MISSING_DATA_ANCHORS, constants.MISSING_DATA_TAB))

        with open(dest, "w") as result_file:
            result_file.write(preamble)
            self._write_tab_bar(result_file, tabs)
            result_file.write('<div class="country-tab-hide-until-ready"></div>\n')

            self._write_tab_start(result_file, constants.TEAMS_ANCHORS)
            self._write_team_stats(result_file, team_stats, tournaments_data)
            self._write_tab_end(result_file)

            self._write_tab_start(result_file, constants.PLAYERS_ANCHORS)
            self._write_player_stats(result_file, player_stats, tournaments_data)
            self._write_tab_end(result_file)

            for section in sections:
                tournament_list = self._tournaments_for_section(
                    section, tournaments_data, game_types
                )
                self._write_tab_start(result_file, self._game_tab_id(section))
                self._write_game_tournaments(
                    result_file, section, tournament_list, len(sections) > 1
                )
                self._write_tab_end(result_file)

            if extra_description or missing_rows:
                self._write_tab_start(result_file, constants.MISSING_DATA_ANCHORS)
                self._write_missing_data(result_file, extra_description, missing_rows)
                self._write_tab_end(result_file)

    @staticmethod
    def _ordered_game_types(tournaments_data: Dict[str, List[TournamentData]]) -> List[str]:
        game_types = sorted(
            game for game, rows in tournaments_data.items() if rows
        )
        if constants.DEFAULT_GAME in game_types:
            game_types.remove(constants.DEFAULT_GAME)
            game_types.insert(0, constants.DEFAULT_GAME)
        return game_types

    @staticmethod
    def _game_tab_id(game: str) -> str:
        return f"game-{game}"

    @staticmethod
    def _contents_anchor(game: str, multiple_games: bool) -> str:
        """Year-list target: contents, or chgk_contents / hamsa_contents when several games share a page."""
        if multiple_games:
            return f"{game}_{constants.CONTENTS_ANCHOR}"
        return constants.CONTENTS_ANCHOR

    @staticmethod
    def _has_shared_primary_games(game_types: List[str]) -> bool:
        return sum(1 for game in game_types if game in constants.PRIMARY_MEDAL_GAMES) > 1

    @staticmethod
    def _year_section_keys(game_types: List[str]) -> List[str]:
        """Collapse chgk/kvrm/zakovat/od into one kvrm tab when several exist."""
        if not StatsGenerator._has_shared_primary_games(game_types):
            return list(game_types)
        others = [game for game in game_types if game not in constants.PRIMARY_MEDAL_GAMES]
        return [constants.PRIMARY_GAMES_ANCHOR, *others]

    @staticmethod
    def _tournaments_for_section(
        section: str,
        tournaments_data: Dict[str, List[TournamentData]],
        game_types: List[str],
    ) -> List[TournamentData]:
        if (
            section == constants.PRIMARY_GAMES_ANCHOR
            and StatsGenerator._has_shared_primary_games(game_types)
        ):
            games = [game for game in game_types if game in constants.PRIMARY_MEDAL_GAMES]
        else:
            games = [section]
        combined = [
            tournament
            for game in games
            for tournament in tournaments_data.get(game, [])
        ]
        return sorted(combined, key=lambda t: (t.year, t.number), reverse=True)

    @staticmethod
    def _tournament_tab_label(
        section: str, tab_count: int, game_types: List[str]
    ) -> str:
        if tab_count <= 1:
            return constants.CHAMPIONSHIPS_TAB
        if (
            StatsGenerator._has_shared_primary_games(game_types)
            and section == constants.PRIMARY_GAMES_ANCHOR
        ):
            return (
                f"{constants.TOURNAMENTS_TAB_PREFIX}"
                f"{constants.GAMES_COLUMN_NAMES[constants.PRIMARY_GAMES_ANCHOR]}"
            )
        if section == constants.DEFAULT_GAME:
            return (
                f"{constants.TOURNAMENTS_TAB_PREFIX}"
                f"{constants.GAMES_COLUMN_NAMES[constants.DEFAULT_GAME]}"
            )
        short = constants.GAMES_SHORT_NAMES.get(section, section)
        return f"{constants.TOURNAMENTS_TAB_PREFIX}{short}"

    @staticmethod
    def _write_tab_bar(file: TextIO, tabs: List[Tuple[str, str]]) -> None:
        file.write(_COUNTRY_TABS_HEAD)
        file.write('<nav class="country-tab-bar" role="tablist">')
        for index, (tab_id, label) in enumerate(tabs):
            selected = "true" if index == 0 else "false"
            active_class = ' class="is-active"' if index == 0 else ""
            file.write(
                f'<button type="button" role="tab"{active_class} '
                f'data-tab="{html.escape(tab_id, quote=True)}" '
                f'aria-selected="{selected}">{html.escape(label)}</button>'
            )
        file.write("</nav>\n")

    @staticmethod
    def _write_tab_start(file: TextIO, tab_id: str) -> None:
        file.write(f'<div class="country-tab-start" data-tab="{html.escape(tab_id, quote=True)}"></div>\n\n')

    @staticmethod
    def _write_tab_end(file: TextIO) -> None:
        file.write('\n<div class="country-tab-end"></div>\n')

    def _default_intro(
        self, tournaments_data: Dict[str, List[TournamentData]]
    ) -> str:
        """Build the opening sentence from the earliest tournament year."""
        years = [
            t.year
            for tournament_list in tournaments_data.values()
            for t in tournament_list
            if t.year
        ]
        if years:
            return (
                f"{self._championships_heading()} "
                f"проводятся с {min(years)} года."
            )
        return ""

    def _championships_heading(self, country_genitive: Optional[str] = None) -> str:
        """«Студенческие чемпионаты России» from metadata age."""
        country = country_genitive or get_country_genitive(self.country)
        template = constants.AGE_CHAMPIONSHIPS_HEADING.get(
            self.age or constants.DEFAULT_AGE,
            constants.AGE_CHAMPIONSHIPS_HEADING[constants.DEFAULT_AGE],
        )
        return template.format(country=country)

    @staticmethod
    def _resolve_age(meta: Optional[Any]) -> str:
        if isinstance(meta, MetaData):
            return normalize_age(meta.age)
        if isinstance(meta, dict):
            return normalize_age(meta.get("age"))
        return constants.DEFAULT_AGE

    def _finalize_errors(
        self,
        tournaments_data: Dict[str, List[TournamentData]],
        existing: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        return merge_data_errors(
            existing,
            collect_computed_errors(
                tournaments_data,
                needs_roster_error=self._needs_roster_error,
            ),
            tournaments_data,
        )

    def _missing_data_content(
        self,
        errors: Dict[str, Any],
        tournaments_data: Dict[str, List[TournamentData]],
    ) -> Tuple[str, List[Tuple[TournamentData, str]]]:
        payload = normalize_errors(errors)
        by_id = flatten_tournaments(tournaments_data)
        rows: List[Tuple[TournamentData, str]] = []
        for item in sort_error_items(payload.get("items") or [], by_id):
            if not is_critical_error(item):
                continue
            description = str(item.get("description") or "").strip()
            if not description:
                continue
            tournament = by_id.get(int(item.get("id") or 0))
            if not tournament or not tournament_is_past(tournament):
                continue
            rows.append((tournament, description))
        return payload.get("description", ""), rows

    def _write_missing_data(
        self,
        file: TextIO,
        extra_description: str,
        rows: List[Tuple[TournamentData, str]],
    ) -> None:
        file.write(f'<a id="{constants.MISSING_DATA_ANCHORS}"></a>\n\n')
        intro = constants.MISSING_DATA_INTRO
        extra = extra_description.strip()
        file.write(f"{intro} {extra}\n\n" if extra else f"{intro}\n\n")
        if not rows:
            return
        file.write(
            "<table>\n<thead>\n<tr>"
            f"<th>{constants.MISSING_DATA_YEAR}</th>"
            f"<th>{constants.MISSING_DATA_TOURNAMENT}</th>"
            f"<th>{constants.MISSING_DATA_WHAT}</th>"
            "</tr>\n</thead>\n<tbody>\n"
        )
        for tournament, description in rows:
            name = self.get_name_tournament(tournament, constants.GAMES_COLUMN_NAMES)
            url = missing_data_tournament_url(
                tournament.links.get("results", ""), tournament.external_ids
            )
            if url:
                name_cell = f'<a href="{html.escape(url, quote=True)}">{html.escape(name)}</a>'
            else:
                name_cell = html.escape(name)
            file.write(
                "<tr>"
                f"<td>{html.escape(str(tournament.year or ''))}</td>"
                f"<td>{name_cell}</td>"
                f"<td>{html.escape(description)}</td>"
                "</tr>\n"
            )
        file.write("</tbody>\n</table>\n")

    def get_name_tournament(
        self,
        tournament: TournamentData,
        game_names: Optional[Dict[str, str]] = None,
    ) -> str:
        """Title for markdown: special name, else «V молодёжный чемпионат Армении по …»."""
        if tournament.display_name:
            return tournament.display_name
        country = get_country_genitive(self.country)
        age = self.age or constants.DEFAULT_AGE
        prefix = constants.AGE_CHAMPIONSHIP_PREFIX.get(age, "")
        suffix = constants.AGE_CHAMPIONSHIP_SUFFIX.get(age, "")
        title = (
            f"{conv.arab_rom(tournament.number)} {prefix}чемпионат {country}{suffix}"
        )
        if not game_names:
            return title
        game_label = game_names.get(tournament.game or constants.DEFAULT_GAME, "")
        if game_label:
            return f"{title} по {game_label}"
        return title

    @staticmethod
    def _snapshot_team(team: Team, players: List[Player]) -> Team:
        """Copy team identity with a private roster (old names stay per tournament)."""
        return Team(
            id=team.id,
            name=team.name,
            city=team.city,
            players=list(players),
            external_ids=dict(team.external_ids),
            non_russian_name=team.non_russian_name,
        )

    def _resolve_roster_player(self, player: Player) -> Player:
        """Resolve/observe player in registry; keep roster-only old names on the copy."""
        registered = (
            self.registry.observe_player(player)
            if player.id
            else self.registry.resolve_player(
                name=player.name,
                surname=player.surname,
                external_ids=player.external_ids,
            )
        )
        if player.non_russian_name and not registered.non_russian_name:
            registered.non_russian_name = player.non_russian_name
        if player.non_russian_surname and not registered.non_russian_surname:
            registered.non_russian_surname = player.non_russian_surname
        return Player(
            id=registered.id,
            name=registered.name or player.name,
            surname=registered.surname or player.surname,
            external_ids=dict(registered.external_ids),
            non_russian_name=registered.non_russian_name,
            non_russian_surname=registered.non_russian_surname,
            old_name=player.old_name,
            old_surname=player.old_surname,
        )

    def _collect_player_old_names(
        self, tournaments_data: Dict[str, List[TournamentData]]
    ) -> Dict[int, List[str]]:
        """Unique historical names per player id, in first-seen order."""
        by_player: Dict[int, List[str]] = {}
        seen: Dict[int, set] = {}
        for tournament_list in tournaments_data.values():
            for tournament in sorted(tournament_list, key=lambda t: (t.year, t.number)):
                for awardee in tournament.awardees.values():
                    for player in awardee.team.players:
                        old = f"{player.old_name.strip()} {player.old_surname.strip()}".strip()
                        if not old or not player.id:
                            continue
                        seen.setdefault(player.id, set())
                        if old in seen[player.id]:
                            continue
                        seen[player.id].add(old)
                        by_player.setdefault(player.id, []).append(old)
        return by_player

    @staticmethod
    def _format_player_display_name(actual: str, old_names: List[str]) -> str:
        if not old_names:
            return actual
        return f"{actual} ({' / '.join(old_names)})"

    def _collect_team_name_aliases(
        self, tournaments_data: Dict[str, List[TournamentData]]
    ) -> Dict[int, List[str]]:
        aliases_by_team: Dict[int, List[str]] = {}
        seen: Dict[int, set] = {}
        for tournament_list in tournaments_data.values():
            for tournament in sorted(tournament_list, key=lambda t: (t.year, t.number)):
                for awardee in tournament.awardees.values():
                    if awardee.individual:
                        continue
                    team_id = awardee.team.id
                    seen.setdefault(team_id, set())
                    for name in (awardee.get_cyrillic_name(), awardee.team.name, awardee.old_name.strip()):
                        if name and name not in seen[team_id]:
                            seen[team_id].add(name)
                            aliases_by_team.setdefault(team_id, []).append(name)
        return aliases_by_team

    def _format_team_name_with_aliases(
        self, team: Awardee, aliases_by_team: Dict[int, List[str]]
    ) -> str:
        aliases = aliases_by_team.get(team.id, [])
        if not aliases:
            primary = team.name
            others: List[str] = []
        else:
            primary = aliases[0]
            others = [name for name in aliases[1:] if name != primary]
        display = Team(
            id=team.id,
            name=primary,
            city=team.city,
            non_russian_name=team.non_russian_name,
        ).display_name(primary)
        return f"{display} ({' / '.join(others)})" if others else display

    @staticmethod
    def _medal_columns(stats: Dict[int, Awardee]) -> List[Tuple[str, Tuple[str, ...]]]:
        games = {
            game
            for awardee in stats.values()
            for game in awardee.games_with_medals()
        }
        columns = medal_column_groups(games)
        # One game (or one merged group) already matches I/II/III/∑ — skip the copy.
        if len(columns) <= 1:
            return []
        return columns

    @staticmethod
    def _sort_medal_rows(
        stats: Dict[int, Awardee],
        names: Dict[int, str],
    ) -> List[Awardee]:
        games = {
            game
            for awardee in stats.values()
            for game in awardee.games_with_medals()
        }
        multi_game = len(games) > 1

        def name_key(awardee: Awardee) -> str:
            return names.get(awardee.id, awardee.name).casefold()

        def sort_key(awardee: Awardee) -> Tuple:
            if not multi_game:
                return (
                    -awardee.sum,
                    -awardee.gold,
                    -awardee.silver,
                    name_key(awardee),
                )
            primary_gold, primary_silver, primary_bronze, _ = awardee.counts_for(
                constants.PRIMARY_MEDAL_GAMES
            )
            return (
                -awardee.sum,
                -awardee.gold,
                -awardee.silver,
                -awardee.bronze,
                -primary_gold,
                -primary_silver,
                -primary_bronze,
                name_key(awardee),
            )

        return sorted(stats.values(), key=sort_key)

    @staticmethod
    def _write_medal_table_header(
        file: TextIO,
        identity_headers: List[str],
        columns: List[Tuple[str, Tuple[str, ...]]],
    ) -> None:
        file.write("\n<table>\n<thead>\n<tr>")
        if not columns:
            for header in identity_headers:
                file.write(f"<th>{header}</th>")
            file.write("<th>I</th><th>II</th><th>III</th><th>∑</th>")
            file.write("</tr>\n</thead>\n<tbody>\n")
            return
        for header in identity_headers:
            file.write(f'<th rowspan="2">{header}</th>')
        file.write(
            f'<th colspan="4" style="text-align:center">{constants.ALL_MEDALS_HEADER}</th>'
        )
        for name, _games in columns:
            label = constants.GAMES_COLUMN_NAMES.get(name, name)
            file.write(f'<th colspan="3" style="text-align:center">{label}</th>')
        file.write("</tr>\n<tr>")
        file.write("<th>I</th><th>II</th><th>III</th><th>∑</th>")
        for _ in columns:
            file.write("<th>I</th><th>II</th><th>III</th>")
        file.write("</tr>\n</thead>\n<tbody>\n")

    @staticmethod
    def _write_medal_table_row(
        file: TextIO,
        awardee: Awardee,
        identity_cells: List[str],
        columns: List[Tuple[str, Tuple[str, ...]]],
    ) -> None:
        file.write("<tr>\n")
        for cell in identity_cells:
            file.write(f"<td>{cell}</td>\n")
        file.write(
            f"<td>{awardee.gold}</td>\n"
            f"<td>{awardee.silver}</td>\n"
            f"<td>{awardee.bronze}</td>\n"
            f"<td>{awardee.sum}</td>\n"
        )
        for _name, games in columns:
            gold, silver, bronze, _total = awardee.counts_for(games)
            file.write(f"<td>{gold}</td>\n<td>{silver}</td>\n<td>{bronze}</td>\n")
        file.write("</tr>\n")

    def _write_team_stats(
        self,
        file: TextIO,
        team_stats: Dict[int, Awardee],
        tournaments_data: Dict[str, List[TournamentData]],
    ) -> None:
        """Write team statistics table."""
        aliases_by_team = self._collect_team_name_aliases(tournaments_data)
        names = {
            team.id: self._format_team_name_with_aliases(team, aliases_by_team)
            for team in team_stats.values()
        }
        columns = self._medal_columns(team_stats)
        file.write(f'<a id="{constants.TEAMS_ANCHORS}"></a>\n')
        self._write_medal_table_header(file, ["Команда", "Город"], columns)
        for team in self._sort_medal_rows(team_stats, names):
            url = team_profile_url(team.external_ids)
            name = names[team.id]
            name_cell = f'<a href="{url}">{name}</a>' if url else name
            self._write_medal_table_row(
                file, team, [name_cell, team.city], columns
            )
        file.write("</tbody>\n</table>\n")

    def _write_player_stats(
        self,
        file: TextIO,
        player_stats: Dict[int, Awardee],
        tournaments_data: Dict[str, List[TournamentData]],
    ) -> None:
        """Write player statistics table (actual name with old names in brackets)."""
        old_names_by_player = self._collect_player_old_names(tournaments_data)
        names = {
            player.id: self._format_player_display_name(
                player.name, old_names_by_player.get(player.id, [])
            )
            for player in player_stats.values()
        }
        columns = self._medal_columns(player_stats)
        file.write(f'<a id="{constants.PLAYERS_ANCHORS}"></a>\n')
        self._write_medal_table_header(file, ["Игрок"], columns)
        for player in self._sort_medal_rows(player_stats, names):
            url = player_profile_url(player.external_ids)
            display = names[player.id]
            cell = f'<a href="{url}">{display}</a>' if url else display
            self._write_medal_table_row(file, player, [cell], columns)
        file.write("</tbody>\n</table>\n")

    @staticmethod
    def _has_finished(tournament: TournamentData) -> bool:
        """True when the tournament end date is in the past.

        An unreadable or missing date counts as not finished, so undated
        entries are treated as upcoming.
        """
        raw_date = tournament.end_date or tournament.start_date
        if not raw_date:
            return False
        return iso_date_is_past(raw_date)

    def _year_anchor(self, tournament: TournamentData, game_type: str = "") -> str:
        """Per-tournament anchor always uses that edition's own game: chgk_2024, od_2023."""
        game = tournament.game or game_type or constants.DEFAULT_GAME
        return f"{game}_{tournament.year}"

    @staticmethod
    def _team_label_with_city(display_name: str, city: str) -> str:
        """Wrap Cyrillic-only names in «»; non-Russian form already includes «»."""
        if "«" in display_name:
            core = display_name
        else:
            core = f"«{display_name}»"
        return f"{core} ({city})" if city else core

    @classmethod
    def _format_team_markdown_link(
        cls, display_name: str, city: str, external_ids: Optional[Dict[str, str]] = None
    ) -> str:
        label = cls._team_label_with_city(display_name, city)
        url = team_profile_url(external_ids)
        if url:
            return f"**[{label}]({url})**"
        return f"**{label}**"

    @classmethod
    def _format_team_markdown_inline(
        cls, display_name: str, external_ids: Optional[Dict[str, str]], city: str
    ) -> str:
        label = cls._team_label_with_city(display_name, city)
        url = team_profile_url(external_ids)
        if url:
            # Link the name part only (before city).
            if city and label.endswith(f" ({city})"):
                name_part = label[: -len(f" ({city})")]
                return f"[{name_part}]({url}) ({city})"
            return f"[{label}]({url})"
        return label

    @staticmethod
    def _awardees_at_place(tournament: TournamentData, place: int) -> List[TournamentAwardee]:
        return [
            awardee
            for _, awardee in sorted(tournament.awardees.items())
            if awardee.place == place
        ]

    def _format_team_enumeration(self, awardees: List[TournamentAwardee]) -> str:
        formatted = [
            self._format_team_markdown_inline(
                a.get_display_name(), a.team.external_ids, a.team.city
            )
            for a in awardees
        ]
        if len(formatted) == 1:
            return formatted[0]
        return self._join_russian_list(formatted)

    @staticmethod
    def _sort_awardees_by_name(
        awardees: List[TournamentAwardee],
    ) -> List[TournamentAwardee]:
        return sorted(
            awardees,
            key=lambda a: (
                a.get_display_name().casefold(),
                (a.team.city or "").casefold(),
            ),
        )

    def _write_team_roster(self, file: TextIO, awardee: TournamentAwardee) -> None:
        for player in awardee.team.players:
            file.write(f"- {player.roster_display_name()}\n")

    def _has_known_winner_roster(self, awardee: TournamentAwardee) -> bool:
        return bool(awardee.team.players)

    def _unknown_winner_roster_note(self, awardees: List[TournamentAwardee]) -> str:
        labels = [
            self._format_team_markdown_inline(
                a.get_display_name(), a.team.external_ids, a.team.city
            )
            for a in awardees
        ]
        teams = self._join_russian_list(labels)
        ask = (
            "Если вы что-то о нём знаете, напишите, пожалуйста, "
            f"на <{constants.CONTACT_EMAIL}>."
        )
        if len(labels) == 1:
            return f"Состав команды {teams} неизвестен. {ask}"
        return f"Состав команд {teams} неизвестен. {ask}"

    @classmethod
    def _format_player_markdown_link(cls, player: Player) -> str:
        name = player.roster_display_name()
        url = player_profile_url(player.external_ids)
        if url:
            return f"**[{name}]({url})**"
        return f"**{name}**"

    @classmethod
    def _format_player_markdown_inline(cls, player: Player) -> str:
        name = player.roster_display_name()
        url = player_profile_url(player.external_ids)
        if url:
            return f"[{name}]({url})"
        return name

    def _format_player_enumeration(self, awardees: List[TournamentAwardee]) -> str:
        formatted = []
        for awardee in awardees:
            player = awardee.individual_player()
            if player:
                formatted.append(self._format_player_markdown_inline(player))
        if not formatted:
            return ""
        if len(formatted) == 1:
            return formatted[0]
        return self._join_russian_list(formatted)

    @staticmethod
    def _sort_individual_awardees_by_surname(
        awardees: List[TournamentAwardee],
    ) -> List[TournamentAwardee]:
        def sort_key(awardee: TournamentAwardee) -> Tuple[str, str]:
            player = awardee.individual_player()
            if not player:
                return ("", "")
            surname = (player.old_surname or player.surname or "").strip()
            name = (player.old_name or player.name or "").strip()
            return (surname.casefold(), name.casefold())

        return sorted(awardees, key=sort_key)

    @staticmethod
    def _individual_place_verb(awardee: TournamentAwardee) -> str:
        return constants.SEX_PLACE_VERB.get(
            awardee.sex, constants.SEX_PLACE_VERB[constants.DEFAULT_SEX]
        )

    @classmethod
    def _individual_place_verb_for(cls, awardees: List[TournamentAwardee]) -> str:
        if len(awardees) > 1:
            return "разделили"
        if awardees:
            return cls._individual_place_verb(awardees[0])
        return constants.SEX_PLACE_VERB[constants.DEFAULT_SEX]

    def _write_team_places(
        self,
        file: TextIO,
        winners: List[TournamentAwardee],
        seconds: List[TournamentAwardee],
        thirds: List[TournamentAwardee],
    ) -> None:
        if len(winners) > 1:
            ordered = self._sort_awardees_by_name(winners)
            names = self._format_team_enumeration(ordered)
            known = [a for a in ordered if self._has_known_winner_roster(a)]
            unknown = [
                a for a in ordered
                if self._needs_roster_error(a) and not self._has_known_winner_roster(a)
            ]
            file.write(f"\nПервое место разделили команды {names}.")
            if known:
                first = known[0]
                first_label = self._format_team_markdown_inline(
                    first.get_display_name(), first.team.external_ids, ""
                )
                file.write(f" Состав команды {first_label}:\n")
                self._write_team_roster(file, first)
                for awardee in known[1:]:
                    label = self._format_team_markdown_inline(
                        awardee.get_display_name(),
                        awardee.team.external_ids,
                        "",
                    )
                    file.write(f"\nСостав команды {label}:\n")
                    self._write_team_roster(file, awardee)
            if unknown:
                file.write(f"\n*{self._unknown_winner_roster_note(unknown)}*\n")
        else:
            for winner_awardee in winners:
                winner = winner_awardee.team
                file.write(
                    f'\nПобедитель: {self._format_team_markdown_link(winner_awardee.get_display_name(), winner.city, winner.external_ids)}\n'
                )
                if self._has_known_winner_roster(winner_awardee):
                    self._write_team_roster(file, winner_awardee)
                elif self._needs_roster_error(winner_awardee):
                    file.write(
                        f"\n*{self._unknown_winner_roster_note([winner_awardee])}*\n"
                    )
        if len(seconds) == 1 and len(thirds) == 1:
            second = seconds[0]
            third = thirds[0]
            file.write(
                f'\nВторое место заняла команда {self._format_team_markdown_inline(second.get_display_name(), second.team.external_ids, second.team.city)}, '
                f'третье — {self._format_team_markdown_inline(third.get_display_name(), third.team.external_ids, third.team.city)}.'
            )
        elif seconds or thirds:
            sentences = []
            if seconds:
                verb = "разделили команды" if len(seconds) > 1 else "заняла команда"
                sentences.append(f'Второе место {verb} {self._format_team_enumeration(seconds)}.')
            if thirds:
                verb = "разделили команды" if len(thirds) > 1 else "заняла команда"
                sentences.append(f'Третье место {verb} {self._format_team_enumeration(thirds)}.')
            file.write("\n" + " ".join(sentences))

    def _write_individual_places(
        self,
        file: TextIO,
        winners: List[TournamentAwardee],
        seconds: List[TournamentAwardee],
        thirds: List[TournamentAwardee],
    ) -> None:
        if len(winners) > 1:
            ordered = self._sort_individual_awardees_by_surname(winners)
            names = self._format_player_enumeration(ordered)
            if names:
                file.write(f"\nПервое место разделили {names}.")
            elif any(self._needs_roster_error(a) for a in ordered):
                file.write(f"\n*{constants.PLAYERS_ERROR}*\n")
        else:
            for winner_awardee in winners:
                player = winner_awardee.individual_player()
                if player:
                    file.write(f"\nПобедитель: {self._format_player_markdown_link(player)}\n")
                elif self._needs_roster_error(winner_awardee):
                    file.write(f"\n*{constants.PLAYERS_ERROR}*\n")
        if len(seconds) == 1 and len(thirds) == 1:
            second = seconds[0].individual_player()
            third = thirds[0].individual_player()
            if second and third:
                verb = self._individual_place_verb(seconds[0])
                file.write(
                    f"\nВторое место {verb} {self._format_player_markdown_inline(second)}, "
                    f"третье — {self._format_player_markdown_inline(third)}."
                )
        elif seconds or thirds:
            sentences = []
            if seconds:
                names = self._format_player_enumeration(seconds)
                if names:
                    verb = self._individual_place_verb_for(seconds)
                    sentences.append(f"Второе место {verb} {names}.")
            if thirds:
                names = self._format_player_enumeration(thirds)
                if names:
                    verb = self._individual_place_verb_for(thirds)
                    sentences.append(f"Третье место {verb} {names}.")
            if sentences:
                file.write("\n" + " ".join(sentences) + "\n")
        named = sum(
            1 for awardee in (*winners, *seconds, *thirds)
            if awardee.individual_player()
        )
        if named < constants.TOP_PLACES:
            file.write(f"\n*{constants.INDIVIDUAL_PRIZERS_INCOMPLETE}*")

    def _years_entry_label(self, tournament: TournamentData) -> str:
        """«V чемпионат Армении по спортивному ЧГК (2022, на армянском языке)» in the game tab year list.

        Only a single non-Russian language is named here; an edition played in
        several languages keeps the plain year and spells them out in its own
        block.
        """
        note = ""
        if len(tournament.languages) == 1:
            phrase = language_phrase(tournament.languages)
            if phrase:
                note = f", {phrase}"
        return (
            f"{self.get_name_tournament(tournament, constants.GAMES_SHORT_NAMES)} "
            f"({tournament.year}{note})"
        )

    def _write_game_tournaments(
        self,
        file: TextIO,
        game_type: str,
        tournament_list: List[TournamentData],
        multiple_games: bool = False,
    ) -> None:
        """Year list and edition blocks for one game, shown inside a tab."""
        contents = self._contents_anchor(game_type, multiple_games)
        file.write(
            f'<a id="{self._game_tab_id(game_type)}"></a>'
            f'<a id="{contents}" name="{contents}"></a>\n\n'
        )
        for tournament in tournament_list:
            file.write(
                f"- [{self._years_entry_label(tournament)}]"
                f"(#{self._year_anchor(tournament, game_type)})\n"
            )
        file.write("\n")
        for tournament in tournament_list:
            self._write_tournament_details(file, tournament, game_type, contents)

    def _write_tournament_details(
        self,
        file: TextIO,
        tournament: TournamentData,
        game_type: str,
        contents_anchor: str = "",
    ) -> None:
        name_tournament = self.get_name_tournament(
            tournament, constants.GAMES_FULL_NAMES_CASE
        )
        anchor = self._year_anchor(tournament, game_type)
        raw_date = tournament_display_date(
            tournament.start_date, tournament.end_date, tournament.date
        ).strip()
        date_part = f" {raw_date}" if raw_date else ""
        is_in_future = not self._has_finished(tournament)
        verb = "пройдёт" if is_in_future else "прошёл"
        # «Вопросы задавались на армянском языке.» — nothing for Russian alone.
        phrase = language_phrase(tournament.languages)
        language_note = ""
        if phrase:
            lang_verb = "задавались" if not is_in_future else "будут задаваться"
            language_note = f"Вопросы {lang_verb} {phrase}. "
        if tournament.city:
            file.write(
                f'\n**{name_tournament}** {verb}{date_part} в {tournament.city}. '
            )
        else:
            file.write(
                f'\n**{name_tournament}** {verb}{date_part}. {constants.CITY_UNKNOWN} '
            )
        file.write(language_note)
        if not is_in_future and not tournament.awardees:
            file.write(f"{constants.RESULTS_NOT_COUNTED} ")
        file.write(f'<a id="{anchor}"></a>')
        if tournament.awardees:
            file.write("\n")
            winners = self._awardees_at_place(tournament, 0)
            seconds = self._awardees_at_place(tournament, 1)
            thirds = self._awardees_at_place(tournament, 2)
            if tournament.game in constants.INDIVIDUAL_GAMES:
                self._write_individual_places(file, winners, seconds, thirds)
            else:
                self._write_team_places(file, winners, seconds, thirds)
        self._write_tournament_sheet_info(file, tournament)
        self._write_tournament_links(file, tournament.links, is_in_future)
        if not tournament.countable and self._has_finished(tournament):
            file.write(f"\n\n*{constants.UNCOUNTABLE_NOTE}*")
        file.write(
            f"\n\n*[{constants.BACK_TO_CONTENTS}]"
            f"(#{contents_anchor or constants.CONTENTS_ANCHOR})*\n\n---\n"
        )

    def _write_tournament_sheet_info(
        self, file: TextIO, tournament: TournamentData
    ) -> None:
        """Comment, results, questions, photos — same for team and SSI editions."""
        if tournament.comment:
            file.write(f" {tournament.comment}")
        results_link = resolve_results_url(
            tournament.links.get("results", ""), tournament.external_ids
        )
        questions = tournament.links.get("questions", "").strip()
        photos = tournament.links.get("photos", "").strip()
        if results_link:
            label = results_markdown_label(results_link)
            file.write(f"\n\nПолные результаты можно найти [{label}]({results_link})")
            if questions:
                file.write(f", вопросы турнира можно почитать [здесь]({questions})")
            file.write(".")
        elif questions:
            file.write(f"\n\nВопросы турнира можно почитать [здесь]({questions}).")
        if photos:
            prefix = " " if (results_link or questions) else "\n\n"
            file.write(
                f"{prefix}Фотографии с турнира можно посмотреть по [этой ссылке]({photos})."
            )

    def _write_tournament_links(
        self, file: TextIO, links: Dict[str, str], is_in_future: bool
    ) -> None:
        announce = links.get("announce", "").strip()
        site = links.get("site", "").strip()
        tg = links.get("tg", "").strip()
        vk = links.get("vk", "").strip()
        fb = links.get("fb", "").strip()
        recap = links.get("recap", "").strip()
        letopis = links.get("letopis", "").strip()

        if announce and is_in_future:
            parts = [f"[в анонсе]({announce})"]
            if tg:
                parts.append(f"[в этом телеграм-канале]({tg})")
            if fb:
                parts.append(f"[в Facebook]({fb})")
            if vk:
                parts.append(f"[в группе ВКонтакте]({vk})")
            file.write(f"\n\n{constants.MORE_INFO_LABEL}{self._join_russian_list(parts)}.")
            return

        parts: List[str] = []
        if site:
            parts.append(f"[на сайте чемпионата]({site})")
        if tg:
            parts.append(f"[в этом телеграм-канале]({tg})")
        if fb:
            parts.append(f"[в Facebook]({fb})")
        if vk:
            parts.append(f"[в группе ВКонтакте]({vk})")
        if recap:
            parts.append(f"[здесь]({recap})")
        if letopis:
            parts.append(f"[в Летописи]({letopis})")
        if not parts:
            return
        file.write(f" {constants.MORE_INFO_LABEL}{self._join_russian_list(parts)}.")

    @staticmethod
    def _join_russian_list(parts: List[str]) -> str:
        if len(parts) == 1:
            return parts[0]
        if len(parts) == 2:
            return f"{parts[0]} и {parts[1]}"
        return ", ".join(parts[:-1]) + " и " + parts[-1]

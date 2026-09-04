"""Google Sheets exporter/importer for tournament statistics (v2 schema)."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    import pygsheets
    PYGSHEETS_AVAILABLE = True
except ImportError:
    PYGSHEETS_AVAILABLE = False

from counting import constants
from counting.data_errors import empty_errors, normalize_errors
from counting.sources import empty_sources, normalize_sources
from counting.videos import empty_videos, normalize_videos
from counting.external_ids import external_id_row_values, external_ids_from_row, normalize_external_ids
from counting.languages import language_name, normalize_language
from counting.models import (
    MetaData,
    Player,
    Team,
    TournamentAwardee,
    TournamentData,
)
from counting.sheet_utils import (
    ERROR_HEADERS,
    INDIVIDUAL_HEADERS,
    LANGUAGE_HEADERS,
    LINK_HEADERS,
    LINK_KEYS,
    NAME_HEADERS,
    PLAYER_REGISTRY_HEADERS,
    PODIUM_HEADERS,
    ROSTER_HEADERS,
    SOURCE_HEADERS,
    TEAM_REGISTRY_HEADERS,
    TOURNAMENT_HEADERS,
    VIDEO_HEADERS,
    format_bool_flag,
    format_roster_complete,
    format_sheet_id,
    has_links,
    merge_links,
    normalize_age,
    normalize_sex,
    parse_bool_flag,
    parse_roster_complete,
    parse_sheet_id,
    parse_sheet_int,
)
from counting.t_fashion import iso_date_year, normalize_tournament_dates


class GoogleSheetsExporter:
    """Exports and loads tournament statistics to/from Google Sheets."""

    SECTION_TOURNAMENTS = "Tournaments"
    SECTION_LINKS = "Links"
    SECTION_PODIUM = "Podium"
    SECTION_ROSTERS = "Rosters"
    SECTION_INDIVIDUALS = "Individuals"
    SECTION_LANGUAGES = "Languages"
    SECTION_NAMES = "Names"
    SECTION_SOURCES = "Sources"
    SECTION_VIDEO = "Video"
    SECTION_TEAMS = "Teams"
    SECTION_PLAYERS = "Players"
    SECTION_ERRORS = "Errors"
    _SECTION_TITLES = (
        SECTION_TOURNAMENTS,
        SECTION_LINKS,
        SECTION_PODIUM,
        SECTION_ROSTERS,
        SECTION_INDIVIDUALS,
        SECTION_LANGUAGES,
        SECTION_NAMES,
        SECTION_SOURCES,
        SECTION_VIDEO,
        SECTION_TEAMS,
        SECTION_PLAYERS,
        SECTION_ERRORS,
    )

    def __init__(
        self,
        credentials_path: Optional[str] = None,
        spreadsheet_id: Optional[str] = None,
    ):
        self.credentials_path = credentials_path or constants.GOOGLE_SHEETS_CREDENTIALS
        self.spreadsheet_id = spreadsheet_id or constants.GOOGLE_SHEETS_SPREADSHEET_ID
        self.client = None
        self.spreadsheet = None
        if not PYGSHEETS_AVAILABLE:
            print("Warning: pygsheets not available. Google Sheets export disabled.")
            return
        if self.credentials_path and self.spreadsheet_id:
            try:
                self.client = pygsheets.authorize(service_account_file=self.credentials_path)
                self.spreadsheet = self.client.open_by_key(self.spreadsheet_id)
            except Exception as exc:
                print(f"Warning: Failed to initialize Google Sheets client: {exc}")
                self.client = None
                self.spreadsheet = None

    def is_available(self) -> bool:
        return PYGSHEETS_AVAILABLE and self.client is not None and self.spreadsheet is not None

    @staticmethod
    def is_public_worksheet(title: str) -> bool:
        """True for country tabs included in the public JSON dump."""
        name = (title or "").strip()
        if not name or name.startswith("_"):
            return False
        skipped = {item.casefold() for item in constants.SKIP_WORKSHEET_TITLES}
        return name.casefold() not in skipped

    def list_country_worksheets(self) -> List[str]:
        if not self.is_available():
            return []
        return [
            ws.title for ws in self.spreadsheet.worksheets()
            if self.is_public_worksheet(ws.title)
        ]

    def public_workbook_snapshot(self) -> Dict[str, Dict[str, Any]]:
        """Sheet-shaped dump: ``{tab: {metadata, tournaments, links, …}}``."""
        snapshot: Dict[str, Dict[str, Any]] = {}
        if not self.is_available():
            return snapshot
        for ws in self.spreadsheet.worksheets():
            if not self.is_public_worksheet(ws.title):
                continue
            all_values = ws.get_all_values()
            snapshot[ws.title] = self._worksheet_as_public_dict(ws.title, all_values)
        return snapshot

    def write_public_json(self, path: Optional[str] = None) -> bool:
        """Rewrite ``content/info/data.json`` from every public worksheet.

        The test spreadsheet must never overwrite the production dump.
        """
        if self.spreadsheet_id == constants.GOOGLE_SHEETS_TEST_SPREADSHEET_ID:
            print("Skipping public JSON rewrite (test spreadsheet).")
            return False
        if not self.is_available():
            print("Google Sheets is not available; public JSON not updated.")
            return False
        payload = self.public_workbook_snapshot()
        dest = Path(path or constants.OUTPUT_JSON)
        dest.parent.mkdir(parents=True, exist_ok=True)
        with open(dest, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        print(f"Wrote public JSON: {dest} ({len(payload)} countries)")
        return True

    def _worksheet_as_public_dict(
        self, title: str, all_values: List[List[str]]
    ) -> Dict[str, Any]:
        sections = self._parse_v2_sections(all_values, title)
        return {
            "metadata": self._load_metadata(all_values, title),
            "tournaments": sections["tournaments"],
            "links": sections["links"],
            "podium": sections["podium"],
            "rosters": sections["rosters"],
            "individuals": sections["individuals"],
            "languages": sections["languages"],
            "names": sections["names"],
            "sources": self._parse_sources_section(all_values),
            "videos": self._parse_video_section(all_values),
            "teams": sections["teams"],
            "players": sections["players"],
            "errors": self._parse_errors_section(all_values),
        }

    def get_spreadsheet_modified_time(self) -> str:
        if not self.is_available() or not self.client:
            return ""
        try:
            drive = self.client.drive
            meta = drive.get_file_metadata(self.spreadsheet_id, fields="modifiedTime")
            return meta.get("modifiedTime", "")
        except Exception:
            return ""

    def load_data(self, country: str) -> Optional[Dict[str, Any]]:
        if not self.is_available():
            return None
        try:
            worksheet = self.spreadsheet.worksheet_by_title(country)
        except pygsheets.exceptions.WorksheetNotFound:
            print(f"Worksheet '{country}' not found in Google Sheets")
            return None

        all_values = worksheet.get_all_values()
        meta = self._load_metadata(all_values, country)
        sections = self._parse_v2_sections(all_values, country)
        team_registry = self._load_team_registry(sections["teams"])
        player_registry = self._load_player_registry(sections["players"])
        tournaments = self._join_tables(
            sections["tournaments"],
            sections["podium"],
            sections["rosters"],
            team_registry,
            player_registry,
            sections["languages"],
            sections["names"],
            sections["links"],
            sections["individuals"],
        )

        tournament_objects: Dict[str, List[TournamentData]] = {}
        for tournament in tournaments:
            tournament_objects.setdefault(tournament.game, []).append(tournament)

        statistics = {
            "team_count": meta.get("team_count", 0),
            "player_count": meta.get("player_count", 0),
            "tournament_count": meta.get("tournament_count", 0),
        }
        meta_obj = MetaData(
            country=meta.get("country", country),
            generated_at=meta.get("generated_at", ""),
            statistics=statistics,
            numbers_champ=meta.get("numbers_champ", {}),
            intro=meta.get("intro", ""),
            age=normalize_age(meta.get("age", constants.DEFAULT_AGE)),
        )
        return {
            "teams": {str(i): t.to_dict() for i, t in team_registry.items()},
            "players": {str(i): p.to_dict() for i, p in player_registry.items()},
            "tournaments": tournament_objects,
            "meta": meta_obj,
            "errors": self._parse_errors_section(all_values),
            "sources": self._parse_sources_section(all_values),
            "videos": self._parse_video_section(all_values),
        }

    def export_data(
        self,
        country: str,
        output_data: Dict[str, Any],
    ) -> bool:
        if not self.is_available():
            return False
        try:
            try:
                worksheet = self.spreadsheet.worksheet_by_title(country)
            except pygsheets.exceptions.WorksheetNotFound:
                worksheet = self.spreadsheet.add_worksheet(country)

            rows = self._build_v2_rows(country, output_data)
            worksheet.clear(fields="*")
            if rows:
                worksheet.update_values("A1", rows, parse=False)
            print(f"Successfully exported data to Google Sheets: {country}")
            return True
        except Exception as exc:
            print(f"Error exporting to Google Sheets: {exc}")
            return False

    def _load_metadata(self, all_values: List[List[str]], country: str) -> Dict[str, Any]:
        meta: Dict[str, Any] = {
            "country": country,
            "numbers_champ": {},
            "intro": "",
            "age": constants.DEFAULT_AGE,
        }
        for row in all_values:
            if row and row[0] in self._SECTION_TITLES:
                break
            if len(row) < 2 or not str(row[0]).strip():
                continue
            key, value = row[0], row[1]
            if key.startswith("number_champ_"):
                game = key.replace("number_champ_", "")
                meta["numbers_champ"][game] = parse_sheet_int(value, default=0) or 0
            elif key in ("country", "generated_at"):
                meta[key] = value
            elif key == "intro":
                meta["intro"] = str(value or "").strip()
            elif key == "age":
                meta["age"] = normalize_age(value)
            elif key == "cyrillic_name":
                continue
            elif key in ("team_count", "player_count", "tournament_count"):
                meta[key] = parse_sheet_int(value, default=0) or 0
        return meta

    def _find_section(self, all_values: List[List[str]], title: str) -> int:
        for idx, row in enumerate(all_values):
            if row and row[0] == title:
                return idx
        return -1

    def _parse_section_rows(
        self,
        all_values: List[List[str]],
        section_title: str,
        country: str = "",
        drop_country: bool = False,
    ) -> List[Dict[str, Any]]:
        start = self._find_section(all_values, section_title)
        if start < 0:
            return []
        header = [str(h).strip() for h in (all_values[start + 1] if start + 1 < len(all_values) else [])]
        while header and not header[-1]:
            header.pop()
        rows: List[Dict[str, Any]] = []
        for row in all_values[start + 2 :]:
            if row and row[0] in self._SECTION_TITLES:
                break
            # Blank padding between data rows (or before the next section)
            # must not truncate the rest of the table.
            if not row or all(not str(cell).strip() for cell in row):
                continue
            values = list(row)
            if drop_country:
                header_used, values = self._drop_country_column(header, values, country)
            else:
                header_used = header
            rows.append(dict(zip(header_used, values + [""] * (len(header_used) - len(values)))))
        return rows

    @staticmethod
    def _drop_country_column(
        header: List[str], values: List[Any], country: str
    ) -> Tuple[List[str], List[Any]]:
        """Ignore a leftover country cell; country lives only in metadata."""
        if not header:
            return header, values
        values = list(values)
        slug = (country or "").strip().casefold()
        first_header = header[0].casefold()
        first_value = str(values[0]).strip() if values else ""
        first_value_l = first_value.casefold()

        if first_header == "country":
            header = header[1:]
            if not values:
                return header, values
            if first_value_l == slug or first_value == "" or not GoogleSheetsExporter._looks_like_number(first_value):
                values = values[1:]
            return header, values

        if slug and first_value_l == slug:
            values = values[1:]
        return header, values

    @staticmethod
    def _looks_like_number(raw: Any) -> bool:
        text = str(raw or "").strip()
        if not text:
            return False
        if text in ("-", "–", "—", "−"):
            return True
        return parse_sheet_int(raw, default=None) is not None

    def _parse_v2_sections(
        self, all_values: List[List[str]], country: str
    ) -> Dict[str, List[Dict[str, Any]]]:
        return {
            "tournaments": self._parse_section_rows(
                all_values, self.SECTION_TOURNAMENTS, country, drop_country=True
            ),
            "podium": self._parse_section_rows(
                all_values, self.SECTION_PODIUM, country, drop_country=True
            ),
            "rosters": self._parse_section_rows(
                all_values, self.SECTION_ROSTERS, country, drop_country=True
            ),
            "individuals": self._parse_section_rows(
                all_values, self.SECTION_INDIVIDUALS, country, drop_country=True
            ),
            "languages": self._parse_section_rows(
                all_values, self.SECTION_LANGUAGES, country, drop_country=True
            ),
            "names": self._parse_section_rows(all_values, self.SECTION_NAMES),
            "links": self._parse_section_rows(all_values, self.SECTION_LINKS),
            "teams": self._parse_section_rows(all_values, self.SECTION_TEAMS),
            "players": self._parse_section_rows(all_values, self.SECTION_PLAYERS),
        }

    def _parse_errors_section(self, all_values: List[List[str]]) -> Dict[str, Any]:
        """Errors: optional description row, then id | description | critical rows."""
        start = self._find_section(all_values, self.SECTION_ERRORS)
        if start < 0:
            return empty_errors()
        index = start + 1
        description = ""
        while index < len(all_values):
            row = all_values[index]
            if row and str(row[0]).strip() in self._SECTION_TITLES:
                return empty_errors()
            if row and any(str(cell).strip() for cell in row):
                break
            index += 1
        if index >= len(all_values):
            return empty_errors()
        first = [str(cell).strip() for cell in all_values[index]]
        if first and first[0].casefold() != "id":
            if first[0].casefold() == "description":
                description = first[1] if len(first) > 1 else ""
            else:
                description = " ".join(part for part in first if part)
            index += 1
        if index >= len(all_values):
            return {"description": description, "items": []}
        header = [str(h).strip() for h in all_values[index]]
        while header and not header[-1]:
            header.pop()
        index += 1
        items: List[Dict[str, Any]] = []
        for row in all_values[index:]:
            if row and str(row[0]).strip() in self._SECTION_TITLES:
                break
            if not row or all(not str(cell).strip() for cell in row):
                continue
            record = dict(zip(header, list(row) + [""] * (len(header) - len(row))))
            tid = parse_sheet_id(record.get("id", ""))
            text = str(record.get("description", "") or "").strip()
            if tid or text:
                items.append({
                    "id": tid,
                    "description": text,
                    "critical": record.get("critical", ""),
                })
        return normalize_errors({"description": description, "items": items})

    def _parse_sources_section(self, all_values: List[List[str]]) -> Dict[str, Any]:
        """Sources: optional description row, then id | year | link | link_name | comment."""
        start = self._find_section(all_values, self.SECTION_SOURCES)
        if start < 0:
            return empty_sources()
        index = start + 1
        description = ""
        while index < len(all_values):
            row = all_values[index]
            if row and str(row[0]).strip() in self._SECTION_TITLES:
                return empty_sources()
            if row and any(str(cell).strip() for cell in row):
                break
            index += 1
        if index >= len(all_values):
            return empty_sources()
        first = [str(cell).strip() for cell in all_values[index]]
        if first and first[0].casefold() != "id":
            if first[0].casefold() == "description":
                description = first[1] if len(first) > 1 else ""
            else:
                description = " ".join(part for part in first if part)
            index += 1
        if index >= len(all_values):
            return {"description": description, "items": []}
        header = [str(h).strip() for h in all_values[index]]
        while header and not header[-1]:
            header.pop()
        index += 1
        items: List[Dict[str, Any]] = []
        for row in all_values[index:]:
            if row and str(row[0]).strip() in self._SECTION_TITLES:
                break
            if not row or all(not str(cell).strip() for cell in row):
                continue
            record = dict(zip(header, list(row) + [""] * (len(header) - len(row))))
            items.append({
                "id": parse_sheet_id(record.get("id", "")),
                "year": parse_sheet_int(record.get("year"), default=0) or 0,
                "link": str(record.get("link") or "").strip(),
                "link_name": str(
                    record.get("link_name") or record.get("link name") or ""
                ).strip(),
                "comment": str(record.get("comment") or "").strip(),
            })
        return normalize_sources({"description": description, "items": items})

    def _parse_video_section(self, all_values: List[List[str]]) -> List[Dict[str, Any]]:
        """Video: id | name | year | link | link_name | description."""
        start = self._find_section(all_values, self.SECTION_VIDEO)
        if start < 0:
            return empty_videos()
        index = start + 1
        while index < len(all_values):
            row = all_values[index]
            if row and str(row[0]).strip() in self._SECTION_TITLES:
                return empty_videos()
            if row and any(str(cell).strip() for cell in row):
                break
            index += 1
        if index >= len(all_values):
            return empty_videos()
        first = [str(cell).strip() for cell in all_values[index]]
        if first and first[0].casefold() != "id":
            index += 1
        if index >= len(all_values):
            return empty_videos()
        header = [str(h).strip() for h in all_values[index]]
        while header and not header[-1]:
            header.pop()
        index += 1
        items: List[Dict[str, Any]] = []
        for row in all_values[index:]:
            if row and str(row[0]).strip() in self._SECTION_TITLES:
                break
            if not row or all(not str(cell).strip() for cell in row):
                continue
            record = dict(zip(header, list(row) + [""] * (len(header) - len(row))))
            items.append({
                "id": parse_sheet_id(record.get("id", "")),
                "name": str(record.get("name") or "").strip(),
                "year": parse_sheet_int(record.get("year"), default=0) or 0,
                "link": str(record.get("link") or "").strip(),
                "link_name": str(
                    record.get("link_name") or record.get("link name") or ""
                ).strip(),
                "description": str(
                    record.get("description") or record.get("decription") or ""
                ).strip(),
            })
        return normalize_videos(items)

    @staticmethod
    def _v2_row_key(row: Dict[str, Any]) -> Tuple[str, str, str]:
        return (
            str(parse_sheet_int(row.get("number", ""))),
            row.get("game") or constants.DEFAULT_GAME,
            str(parse_sheet_int(row.get("year", ""))),
        )

    @staticmethod
    def _row_tournament_id(row: Dict[str, Any]) -> int:
        return parse_sheet_id(
            row.get("id") or row.get("tournament id") or row.get("tournament_id") or ""
        )

    def _find_tournament(
        self,
        row: Dict[str, Any],
        by_id: Dict[int, TournamentData],
        by_key: Dict[Tuple[str, str, str], TournamentData],
    ) -> Optional[TournamentData]:
        """Join a child row to its Tournaments record.

        Game and year live only on the Tournaments row. Child tables join by
        internal ``id``. Leftover ``number``/``game``/``year`` cells on an old
        sheet are a fallback when ``id`` is blank — but only if those cells
        are actually present, so a v2 Rosters row with a blank id is not
        attached to ``(0, chgk, 0)``.
        """
        tournament_id = self._row_tournament_id(row)
        if tournament_id:
            return by_id.get(tournament_id)
        if str(row.get("number") or "").strip() or str(row.get("year") or "").strip():
            return by_key.get(self._v2_row_key(row))
        return None

    @staticmethod
    def _load_team_registry(rows: List[Dict[str, Any]]) -> Dict[int, Team]:
        registry: Dict[int, Team] = {}
        for row in rows:
            team_id = parse_sheet_id(row.get("id", ""))
            if not team_id:
                continue
            registry[team_id] = Team(
                id=team_id,
                name=row.get("name", ""),
                city=row.get("city", ""),
                external_ids=external_ids_from_row(row),
                non_russian_name=row.get("non_russian_name", ""),
            )
        return registry

    @staticmethod
    def _load_player_registry(rows: List[Dict[str, Any]]) -> Dict[int, Player]:
        registry: Dict[int, Player] = {}
        for row in rows:
            player_id = parse_sheet_id(row.get("id", ""))
            if not player_id:
                continue
            registry[player_id] = Player(
                id=player_id,
                name=row.get("name", ""),
                surname=row.get("surname", ""),
                external_ids=external_ids_from_row(row),
                non_russian_name=row.get("non_russian_name", ""),
                non_russian_surname=row.get("non_russian_surname", ""),
            )
        return registry

    def _join_tables(
        self,
        tournaments: List[Dict[str, Any]],
        podium_rows: List[Dict[str, Any]],
        roster_rows: List[Dict[str, Any]],
        team_registry: Dict[int, Team],
        player_registry: Dict[int, Player],
        language_rows: Optional[List[Dict[str, Any]]] = None,
        name_rows: Optional[List[Dict[str, Any]]] = None,
        link_rows: Optional[List[Dict[str, Any]]] = None,
        individual_rows: Optional[List[Dict[str, Any]]] = None,
    ) -> List[TournamentData]:
        by_key: Dict[Tuple[str, str, str], TournamentData] = {}
        by_id: Dict[int, TournamentData] = {}
        ordered: List[TournamentData] = []

        for row in tournaments:
            game = row.get("game") or constants.DEFAULT_GAME
            key = self._v2_row_key(row)
            # Leftover link columns on old Tournaments rows still load.
            links = merge_links({k: row.get(k, "") for k in LINK_KEYS})
            start_date, end_date, display_date = normalize_tournament_dates(
                row.get("start_date", ""),
                row.get("end_date", ""),
                row.get("date", ""),
            )
            year = parse_sheet_int(row.get("year", ""), default=0) or 0
            if not year:
                year = iso_date_year(end_date or start_date)
            subnumber = parse_sheet_int(row.get("subnumber", ""), default=0) or 0
            tournament = TournamentData(
                id=parse_sheet_id(row.get("id", "")),
                number=parse_sheet_int(row.get("number", ""), default=0) or 0,
                subnumber=subnumber if subnumber > 0 else 0,
                date=display_date,
                start_date=start_date,
                end_date=end_date,
                city=row.get("city", ""),
                year=year,
                game=game,
                links=links,
                external_ids=external_ids_from_row(row),
                countable=parse_bool_flag(row.get("countable"), default=False),
                comment=str(row.get("comment", "") or "").strip(),
            )
            # Index by id first so two editions that share number/game/year
            # (or a repeated key) are not collapsed before podium/rosters join.
            if tournament.id:
                by_id[tournament.id] = tournament
            by_key[key] = tournament
            ordered.append(tournament)

        for row in link_rows or []:
            tournament = self._find_tournament(row, by_id, by_key)
            if not tournament:
                continue
            extra = {
                key: row.get(key, "")
                for key in LINK_KEYS
                if str(row.get(key, "") or "").strip()
            }
            if extra:
                tournament.links = merge_links({**tournament.links, **extra})

        for row in name_rows or []:
            name = str(row.get("name", "") or "").strip()
            if not name:
                continue
            tournament = self._find_tournament(row, by_id, by_key)
            if tournament:
                tournament.display_name = name

        for row in language_rows or []:
            tournament = self._find_tournament(row, by_id, by_key)
            if not tournament:
                continue
            raw = row.get("language", "") or row.get("name", "")
            code = normalize_language(raw)
            if not code:
                if str(raw).strip():
                    print(f"Skipping unknown language {raw!r} for tournament {tournament.number}")
                continue
            if code not in tournament.languages:
                tournament.languages.append(code)

        for row in podium_rows:
            tournament = self._find_tournament(row, by_id, by_key)
            if not tournament:
                print(f"Skipping podium row with unknown tournament id: {row.get('id')!r}")
                continue
            if tournament.game in constants.INDIVIDUAL_GAMES:
                continue
            place = parse_sheet_int(row.get("place"), default=None)
            if place is None:
                print(f"Skipping podium row with unreadable place: {row.get('place')!r}")
                continue
            team_id = parse_sheet_id(row.get("team id", "") or row.get("team_id", ""))
            registered = team_registry.get(team_id)
            team = Team(
                id=team_id,
                name=row.get("team name", "") or (registered.name if registered else ""),
                city=row.get("team city", "") or (registered.city if registered else ""),
                external_ids=dict(registered.external_ids) if registered else {},
                non_russian_name=(registered.non_russian_name if registered else ""),
            )
            tournament.awardees[len(tournament.awardees)] = TournamentAwardee(
                team=team,
                place=place,
                old_name=row.get("old name", "") or row.get("old_name", ""),
                roster_complete=parse_roster_complete(row.get("roster_complete", "")),
            )

        for row in roster_rows:
            tournament = self._find_tournament(row, by_id, by_key)
            if not tournament:
                print(
                    "Skipping roster row with unknown tournament id: "
                    f"{row.get('id')!r}"
                )
                continue
            if tournament.game in constants.INDIVIDUAL_GAMES:
                continue
            place = parse_sheet_int(row.get("place"), default=None)
            team_id = parse_sheet_id(row.get("team id") or row.get("team_id", ""))
            awardee = self._podium_awardee_for_roster(tournament, place, team_id)
            if not awardee:
                print(
                    "Skipping roster row with no matching podium: "
                    f"tournament={row.get('id')!r} place={row.get('place')!r} "
                    f"team_id={row.get('team id') or row.get('team_id')!r} "
                    f"player={row.get('player name', '')} {row.get('player surname', '')}".strip()
                )
                continue
            player_id = parse_sheet_id(row.get("player id") or row.get("player_id", ""))
            registered = player_registry.get(player_id)
            awardee.team.players.append(
                Player(
                    id=player_id,
                    name=row.get("player name", "") or (registered.name if registered else ""),
                    surname=row.get("player surname", "")
                    or (registered.surname if registered else ""),
                    external_ids=dict(registered.external_ids) if registered else {},
                    non_russian_name=registered.non_russian_name if registered else "",
                    non_russian_surname=registered.non_russian_surname if registered else "",
                    old_name=(
                        row.get("old_name", "")
                        or row.get("old name", "")
                    ),
                    old_surname=(
                        row.get("old_surname", "")
                        or row.get("old surname", "")
                    ),
                )
            )

        for row in individual_rows or []:
            tournament = self._find_tournament(row, by_id, by_key)
            if not tournament:
                print(
                    "Skipping individual row with unknown tournament id: "
                    f"{row.get('id')!r}"
                )
                continue
            if tournament.game not in constants.INDIVIDUAL_GAMES:
                print(
                    "Skipping individual row for non-individual game "
                    f"{tournament.game!r} (tournament {tournament.id})"
                )
                continue
            place = parse_sheet_int(row.get("place"), default=None)
            if place is None:
                print(f"Skipping individual row with unreadable place: {row.get('place')!r}")
                continue
            player = self._player_from_sheet_row(row, player_registry)
            display = player.roster_display_name() or f"{player.name} {player.surname}".strip()
            tournament.awardees[len(tournament.awardees)] = TournamentAwardee(
                team=Team(id=0, name=display, city="", players=[player]),
                place=place,
                roster_complete=bool(display or player.id),
                individual=True,
                sex=normalize_sex(row.get("sex", "")),
            )

        return list(ordered)

    @staticmethod
    def _podium_awardee_for_roster(
        tournament: TournamentData,
        place: Optional[int],
        team_id: int,
    ) -> Optional[TournamentAwardee]:
        """Attach a Rosters row to a Podium medalist.

        Prefer place + team id (ties share a place). If place is blank or
        disagrees with the sheet, fall back to a unique team id on this podium.
        """
        awardees = [a for _, a in sorted(tournament.awardees.items())]
        if place is not None:
            at_place = [a for a in awardees if int(a.place) == int(place)]
            if team_id:
                matched = [a for a in at_place if a.team.id == team_id]
                if matched:
                    return matched[0]
            elif at_place:
                return at_place[0]
        if team_id:
            by_team = [a for a in awardees if a.team.id == team_id]
            if len(by_team) == 1:
                return by_team[0]
            if place is None and by_team:
                return by_team[0]
        return None

    @staticmethod
    def _player_from_sheet_row(
        row: Dict[str, Any], player_registry: Dict[int, Player]
    ) -> Player:
        player_id = parse_sheet_id(row.get("player id") or row.get("player_id", ""))
        registered = player_registry.get(player_id)
        return Player(
            id=player_id,
            name=row.get("player name", "") or (registered.name if registered else ""),
            surname=row.get("player surname", "")
            or (registered.surname if registered else ""),
            external_ids=dict(registered.external_ids) if registered else {},
            non_russian_name=registered.non_russian_name if registered else "",
            non_russian_surname=registered.non_russian_surname if registered else "",
            old_name=row.get("old_name", "") or row.get("old name", ""),
            old_surname=row.get("old_surname", "") or row.get("old surname", ""),
        )

    def _collect_registries(
        self, tournaments: Dict[str, Any]
    ) -> Tuple[Dict[int, Team], Dict[int, Player]]:
        teams: Dict[int, Team] = {}
        players: Dict[int, Player] = {}
        if not isinstance(tournaments, dict):
            return teams, players
        for game_list in tournaments.values():
            for tdata in game_list:
                t = tdata if isinstance(tdata, TournamentData) else TournamentData.from_dict(tdata)
                for awardee in t.awardees.values():
                    team = awardee.team
                    if team.id and not awardee.individual:
                        existing = teams.get(team.id)
                        if existing:
                            if not existing.name:
                                existing.name = team.name
                            if not existing.city:
                                existing.city = team.city
                            if not existing.non_russian_name:
                                existing.non_russian_name = team.non_russian_name
                            existing.external_ids = {
                                **normalize_external_ids(existing.external_ids),
                                **normalize_external_ids(team.external_ids),
                            }
                        else:
                            teams[team.id] = Team(
                                id=team.id,
                                name=team.name,
                                city=team.city,
                                external_ids=dict(team.external_ids),
                                non_russian_name=team.non_russian_name,
                            )
                    for player in team.players:
                        if not player.id:
                            continue
                        existing_p = players.get(player.id)
                        if existing_p:
                            if not existing_p.name:
                                existing_p.name = player.name
                            if not existing_p.surname:
                                existing_p.surname = player.surname
                            if not existing_p.non_russian_name:
                                existing_p.non_russian_name = player.non_russian_name
                            if not existing_p.non_russian_surname:
                                existing_p.non_russian_surname = player.non_russian_surname
                            existing_p.external_ids = {
                                **normalize_external_ids(existing_p.external_ids),
                                **normalize_external_ids(player.external_ids),
                            }
                        else:
                            # Players registry never stores roster-only old names.
                            players[player.id] = Player(
                                id=player.id,
                                name=player.name,
                                surname=player.surname,
                                external_ids=dict(player.external_ids),
                                non_russian_name=player.non_russian_name,
                                non_russian_surname=player.non_russian_surname,
                            )
        return teams, players

    def _build_v2_rows(
        self,
        country: str,
        output_data: Dict[str, Any],
    ) -> List[List[Any]]:
        rows: List[List[Any]] = [["metadata"]]
        meta = output_data.get("meta", {})
        if isinstance(meta, MetaData):
            meta_dict = meta.to_dict()
        else:
            meta_dict = meta

        rows.append(["country", meta_dict.get("country", country)])
        rows.append(["age", meta_dict.get("age", constants.DEFAULT_AGE)])
        rows.append(["intro", meta_dict.get("intro", "")])
        rows.append(["generated_at", meta_dict.get("generated_at", "")])
        for game_type in sorted(meta_dict.get("numbers_champ", {}).keys()):
            rows.append([f"number_champ_{game_type}", meta_dict["numbers_champ"][game_type]])
        stats = meta_dict.get("statistics", {})
        rows.append(["team_count", stats.get("team_count", 0)])
        rows.append(["player_count", stats.get("player_count", 0)])
        rows.append(["tournament_count", stats.get("tournament_count", 0)])
        rows.append([])

        tournaments = output_data.get("tournaments", {})
        teams, players = self._collect_registries(tournaments)
        # Prefer explicit registries from output_data when present.
        for raw in (output_data.get("teams") or {}).values():
            team = Team.from_dict(raw) if isinstance(raw, dict) else raw
            teams[team.id] = team
        for raw in (output_data.get("players") or {}).values():
            player = Player.from_dict(raw) if isinstance(raw, dict) else raw
            players[player.id] = player

        rows.append([self.SECTION_TOURNAMENTS])
        rows.append(TOURNAMENT_HEADERS)
        link_rows: List[List[Any]] = [[self.SECTION_LINKS], LINK_HEADERS]
        podium_rows: List[List[Any]] = [[self.SECTION_PODIUM], PODIUM_HEADERS]
        roster_rows: List[List[Any]] = [[self.SECTION_ROSTERS], ROSTER_HEADERS]
        individual_rows: List[List[Any]] = [[self.SECTION_INDIVIDUALS], INDIVIDUAL_HEADERS]
        language_rows: List[List[Any]] = [[self.SECTION_LANGUAGES], LANGUAGE_HEADERS]
        name_rows: List[List[Any]] = [[self.SECTION_NAMES], NAME_HEADERS]

        if isinstance(tournaments, dict):
            game_types = sorted(tournaments.keys())
            if constants.DEFAULT_GAME in game_types:
                game_types.remove(constants.DEFAULT_GAME)
                game_types.insert(0, constants.DEFAULT_GAME)
            for game in game_types:
                for tdata in tournaments[game]:
                    if isinstance(tdata, TournamentData):
                        t = tdata
                    else:
                        t = TournamentData.from_dict(tdata)
                    start_date, end_date, _ = normalize_tournament_dates(
                        t.start_date, t.end_date, t.date
                    )
                    rows.append([
                        format_sheet_id(t.id),
                        t.number,
                        t.subnumber if t.subnumber else "",
                        t.game,
                        start_date,
                        end_date,
                        t.city,
                        t.year,
                        format_bool_flag(t.countable),
                        *external_id_row_values(t.external_ids),
                        t.comment,
                    ])
                    if t.id and has_links(t.links):
                        link_rows.append([
                            format_sheet_id(t.id),
                            *[t.links.get(k, "") for k in LINK_KEYS],
                        ])
                    for code in t.languages:
                        language_rows.append([
                            format_sheet_id(t.id), code, language_name(code),
                        ])
                    if t.display_name and t.id:
                        name_rows.append([format_sheet_id(t.id), t.display_name])
                    for _, awardee in sorted(t.awardees.items()):
                        if awardee.individual or t.game in constants.INDIVIDUAL_GAMES:
                            player = awardee.individual_player()
                            if player:
                                individual_rows.append([
                                    format_sheet_id(t.id), awardee.place,
                                    format_sheet_id(player.id), player.name, player.surname,
                                    player.old_name, player.old_surname,
                                    normalize_sex(awardee.sex),
                                ])
                            continue
                        podium_rows.append([
                            format_sheet_id(t.id), awardee.place,
                            format_sheet_id(awardee.team.id), awardee.team.name, awardee.old_name,
                            awardee.team.city, format_roster_complete(awardee.roster_complete),
                        ])
                        for player in awardee.team.players:
                            roster_rows.append([
                                format_sheet_id(t.id), awardee.place,
                                format_sheet_id(awardee.team.id),
                                format_sheet_id(player.id), player.name, player.surname,
                                player.old_name, player.old_surname,
                            ])

        rows.append([])
        rows.extend(link_rows)
        rows.append([])
        rows.extend(podium_rows)
        rows.append([])
        rows.extend(roster_rows)
        rows.append([])
        rows.extend(individual_rows)
        rows.append([])
        rows.extend(language_rows)
        rows.append([])
        rows.extend(name_rows)
        rows.append([])
        sources = normalize_sources(output_data.get("sources"))
        rows.append([self.SECTION_SOURCES])
        rows.append(["description", sources.get("description", "")])
        rows.append(SOURCE_HEADERS)
        for item in sources.get("items") or []:
            year = item.get("year") or ""
            rows.append([
                format_sheet_id(item.get("id") or 0),
                year if year else "",
                item.get("link", ""),
                item.get("link_name", ""),
                item.get("comment", ""),
            ])
        rows.append([])
        videos = normalize_videos(output_data.get("videos"))
        rows.append([self.SECTION_VIDEO])
        rows.append(VIDEO_HEADERS)
        for item in videos:
            year = item.get("year") or ""
            rows.append([
                format_sheet_id(item.get("id") or 0),
                item.get("name", ""),
                year if year else "",
                item.get("link", ""),
                item.get("link_name", ""),
                item.get("description", ""),
            ])
        rows.append([])
        rows.append([self.SECTION_TEAMS])
        rows.append(TEAM_REGISTRY_HEADERS)
        for team in sorted(teams.values(), key=lambda t: t.id):
            rows.append([
                format_sheet_id(team.id), team.name, team.non_russian_name, team.city,
                *external_id_row_values(team.external_ids),
            ])
        rows.append([])
        rows.append([self.SECTION_PLAYERS])
        rows.append(PLAYER_REGISTRY_HEADERS)
        for player in sorted(players.values(), key=lambda p: p.id):
            rows.append([
                format_sheet_id(player.id), player.name, player.surname,
                player.non_russian_name, player.non_russian_surname,
                *external_id_row_values(player.external_ids),
            ])
        rows.append([])
        errors = normalize_errors(output_data.get("errors"))
        rows.append([self.SECTION_ERRORS])
        rows.append(["description", errors.get("description", "")])
        rows.append(ERROR_HEADERS)
        for item in errors.get("items") or []:
            rows.append([
                format_sheet_id(item.get("id") or 0),
                item.get("description", ""),
                item.get("critical", "yes"),
            ])
        return rows

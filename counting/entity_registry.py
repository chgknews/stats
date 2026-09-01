"""Internal entity IDs and external-id deduplication."""
from __future__ import annotations

from typing import Dict, List, Optional, TYPE_CHECKING

from counting import constants
from counting.external_ids import merge_external_ids, normalize_external_ids
from counting.models import Player, Team

if TYPE_CHECKING:
    from counting.google_sheets_exporter import GoogleSheetsExporter


class EntityIdAllocator:
    """Global auto-increment IDs shared across country worksheets."""

    KINDS = ("team", "player", "tournament")

    def __init__(self) -> None:
        self._next = {kind: 1 for kind in self.KINDS}

    def observe(self, kind: str, entity_id: int) -> None:
        if kind not in self._next or not entity_id:
            return
        if entity_id >= self._next[kind]:
            self._next[kind] = entity_id + 1

    def allocate(self, kind: str) -> int:
        if kind not in self._next:
            raise ValueError(f"Unknown entity kind: {kind}")
        value = self._next[kind]
        self._next[kind] = value + 1
        return value

    def load_from_exporter(self, exporter: "GoogleSheetsExporter") -> None:
        if not exporter.is_available():
            return
        try:
            worksheet = exporter.spreadsheet.worksheet_by_title(constants.ENTITY_IDS_WORKSHEET)
        except Exception:
            return
        for row in worksheet.get_all_values():
            if len(row) < 2 or not row[0]:
                continue
            key, raw = row[0].strip(), row[1]
            if not key.startswith("next_") or not key.endswith("_id"):
                continue
            kind = key[len("next_") : -len("_id")]
            try:
                value = int(raw)
            except (TypeError, ValueError):
                continue
            if kind in self._next and value > self._next[kind]:
                self._next[kind] = value

    def persist_to_exporter(self, exporter: "GoogleSheetsExporter") -> None:
        if not exporter.is_available():
            return
        try:
            try:
                worksheet = exporter.spreadsheet.worksheet_by_title(constants.ENTITY_IDS_WORKSHEET)
            except Exception:
                worksheet = exporter.spreadsheet.add_worksheet(constants.ENTITY_IDS_WORKSHEET)
            rows = [[f"next_{kind}_id", self._next[kind]] for kind in self.KINDS]
            worksheet.clear(fields="*")
            worksheet.update_values("A1", rows, parse=False)
        except Exception as exc:
            print(f"Warning: failed to persist {constants.ENTITY_IDS_WORKSHEET}: {exc}")


class EntityRegistry:
    """Resolve entities by external id; allocate internal ids when unknown."""

    def __init__(self, allocator: Optional[EntityIdAllocator] = None) -> None:
        self.allocator = allocator or EntityIdAllocator()
        self.teams: Dict[int, Team] = {}
        self.players: Dict[int, Player] = {}
        self._team_by_external: Dict[str, Dict[str, int]] = {
            s: {} for s in constants.EXTERNAL_ID_SOURCES
        }
        self._player_by_external: Dict[str, Dict[str, int]] = {
            s: {} for s in constants.EXTERNAL_ID_SOURCES
        }
        self._tournament_by_external: Dict[str, Dict[str, int]] = {
            s: {} for s in constants.EXTERNAL_ID_SOURCES
        }
        self.tournament_ids: Dict[int, Dict[str, str]] = {}

    def observe_team(self, team: Team) -> Team:
        if not team.id:
            team.id = self.allocator.allocate("team")
        else:
            self.allocator.observe("team", team.id)
        team.external_ids = normalize_external_ids(team.external_ids)
        existing = self.teams.get(team.id)
        if existing:
            existing.name = team.name or existing.name
            existing.city = team.city or existing.city
            existing.non_russian_name = team.non_russian_name or existing.non_russian_name
            existing.external_ids = merge_external_ids(existing.external_ids, team.external_ids)
            # Do not attach tournament rosters to the registry Team — players are
            # per-event and carry old_name/old_surname that must not be shared.
            team = existing
        else:
            # Registry copy without roster players.
            self.teams[team.id] = Team(
                id=team.id,
                name=team.name,
                city=team.city,
                external_ids=dict(team.external_ids),
                non_russian_name=team.non_russian_name,
            )
            team = self.teams[team.id]
        self._index_entity(self._team_by_external, team.id, team.external_ids)
        return team

    def observe_player(self, player: Player) -> Player:
        if not player.id:
            player.id = self.allocator.allocate("player")
        else:
            self.allocator.observe("player", player.id)
        player.external_ids = normalize_external_ids(player.external_ids)
        existing = self.players.get(player.id)
        if existing:
            existing.name = player.name or existing.name
            existing.surname = player.surname or existing.surname
            existing.non_russian_name = player.non_russian_name or existing.non_russian_name
            existing.non_russian_surname = (
                player.non_russian_surname or existing.non_russian_surname
            )
            existing.external_ids = merge_external_ids(existing.external_ids, player.external_ids)
            # Registry must not keep per-tournament old names.
            existing.old_name = ""
            existing.old_surname = ""
            player = existing
        else:
            # Store a registry copy without roster-only fields.
            self.players[player.id] = Player(
                id=player.id,
                name=player.name,
                surname=player.surname,
                external_ids=dict(player.external_ids),
                non_russian_name=player.non_russian_name,
                non_russian_surname=player.non_russian_surname,
            )
        self._index_entity(self._player_by_external, player.id, player.external_ids)
        return player

    def observe_tournament_ids(self, tournament_id: int, external_ids: Dict[str, str]) -> int:
        if not tournament_id:
            tournament_id = self.allocator.allocate("tournament")
        else:
            self.allocator.observe("tournament", tournament_id)
        ids = normalize_external_ids(external_ids)
        existing = self.tournament_ids.get(tournament_id, {})
        self.tournament_ids[tournament_id] = merge_external_ids(existing, ids)
        self._index_entity(
            self._tournament_by_external, tournament_id, self.tournament_ids[tournament_id]
        )
        return tournament_id

    def resolve_team(
        self,
        *,
        name: str,
        city: str,
        external_ids: Optional[Dict[str, str]] = None,
        players: Optional[List[Player]] = None,
    ) -> Team:
        ids = normalize_external_ids(external_ids)
        matched = self._find_by_external(self._team_by_external, ids)
        if matched is not None:
            team = self.teams[matched]
            team.name = name or team.name
            team.city = city or team.city
            team.external_ids = merge_external_ids(team.external_ids, ids)
            if players is not None:
                team.players = players
            self._index_entity(self._team_by_external, team.id, team.external_ids)
            return team
        team = Team(
            id=self.allocator.allocate("team"),
            name=name,
            city=city,
            players=players or [],
            external_ids=ids,
        )
        self.teams[team.id] = team
        self._index_entity(self._team_by_external, team.id, ids)
        return team

    def resolve_player(
        self,
        *,
        name: str,
        surname: str,
        external_ids: Optional[Dict[str, str]] = None,
    ) -> Player:
        ids = normalize_external_ids(external_ids)
        matched = self._find_by_external(self._player_by_external, ids)
        if matched is not None:
            player = self.players[matched]
            player.name = name or player.name
            player.surname = surname or player.surname
            player.external_ids = merge_external_ids(player.external_ids, ids)
            self._index_entity(self._player_by_external, player.id, player.external_ids)
            return player
        player = Player(
            id=self.allocator.allocate("player"),
            name=name,
            surname=surname,
            external_ids=ids,
        )
        self.players[player.id] = player
        self._index_entity(self._player_by_external, player.id, ids)
        return player

    def resolve_tournament_id(self, external_ids: Optional[Dict[str, str]] = None) -> int:
        ids = normalize_external_ids(external_ids)
        matched = self._find_by_external(self._tournament_by_external, ids)
        if matched is not None:
            self.tournament_ids[matched] = merge_external_ids(
                self.tournament_ids.get(matched), ids
            )
            self._index_entity(
                self._tournament_by_external, matched, self.tournament_ids[matched]
            )
            return matched
        tournament_id = self.allocator.allocate("tournament")
        self.tournament_ids[tournament_id] = ids
        self._index_entity(self._tournament_by_external, tournament_id, ids)
        return tournament_id

    @staticmethod
    def _find_by_external(
        index: Dict[str, Dict[str, int]], external_ids: Dict[str, str]
    ) -> Optional[int]:
        for source, value in external_ids.items():
            if value and value in index.get(source, {}):
                return index[source][value]
        return None

    @staticmethod
    def _index_entity(
        index: Dict[str, Dict[str, int]], entity_id: int, external_ids: Dict[str, str]
    ) -> None:
        for source, value in normalize_external_ids(external_ids).items():
            index[source][value] = entity_id
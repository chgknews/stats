"""Cross-country duplicate detection and ID replacement by external ids."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from itertools import combinations
from typing import Any, Dict, Iterable, List, Optional, Tuple

from counting import constants
from counting.external_ids import (
    empty_external_ids,
    merge_external_ids,
    normalize_external_ids,
)
from counting.google_sheets_exporter import GoogleSheetsExporter
from counting.models import Player, Team, TournamentData
from counting.sheet_utils import (
    DOUBLES_HEADERS,
    entity_set_headers,
    format_sheet_id,
    parse_bool_flag,
    parse_sheet_id,
)

KIND_TOURNAMENT = constants.KIND_TOURNAMENT
KIND_TEAM = constants.KIND_TEAM
KIND_PLAYER = constants.KIND_PLAYER

DoubleKey = Tuple[str, int, int]


@dataclass
class EntityRecord:
    """One internal id as seen across country tabs."""
    kind: str
    id: int
    name: str = ""
    surname: str = ""
    ts_id: str = ""
    uz_id: str = ""
    ua_id: str = ""
    countries: List[str] = field(default_factory=list)

    def external_ids(self) -> Dict[str, str]:
        return normalize_external_ids({
            constants.EXTERNAL_ID_TS: self.ts_id,
            constants.EXTERNAL_ID_UZ: self.uz_id,
            constants.EXTERNAL_ID_UA: self.ua_id,
        })

    def merge(self, other: "EntityRecord") -> None:
        self.name = self.name or other.name
        self.surname = self.surname or other.surname
        self.ts_id = self.ts_id or other.ts_id
        self.uz_id = self.uz_id or other.uz_id
        self.ua_id = self.ua_id or other.ua_id
        self.countries = sorted(set(self.countries) | set(other.countries))

    def to_set_row(self) -> List[Any]:
        row = [format_sheet_id(self.id), self.name]
        if self.kind == KIND_PLAYER:
            row.append(self.surname)
        row.extend([self.ts_id, self.uz_id, self.ua_id])
        return row


@dataclass
class EntitySets:
    """All tournaments, teams and players keyed by internal id."""
    tournaments: Dict[int, EntityRecord] = field(default_factory=dict)
    teams: Dict[int, EntityRecord] = field(default_factory=dict)
    players: Dict[int, EntityRecord] = field(default_factory=dict)

    def bucket(self, kind: str) -> Dict[int, EntityRecord]:
        if kind == KIND_TOURNAMENT:
            return self.tournaments
        if kind == KIND_TEAM:
            return self.teams
        if kind == KIND_PLAYER:
            return self.players
        raise ValueError(f"Unknown entity kind: {kind}")


@dataclass
class DoubleRow:
    kind: str
    ts_id: str = ""
    uz_id: str = ""
    ua_id: str = ""
    id1: int = 0
    name1: str = ""
    surname1: str = ""
    id2: int = 0
    name2: str = ""
    surname2: str = ""
    replace: str = ""

    @property
    def key(self) -> DoubleKey:
        return (self.kind, self.id1, self.id2)

    def to_sheet_row(self) -> List[Any]:
        return [
            self.kind,
            self.ts_id,
            self.uz_id,
            self.ua_id,
            format_sheet_id(self.id1),
            self.name1,
            self.surname1,
            format_sheet_id(self.id2),
            self.name2,
            self.surname2,
            self.replace,
        ]


def _put(bucket: Dict[int, EntityRecord], record: EntityRecord) -> None:
    existing = bucket.get(record.id)
    if existing:
        existing.merge(record)
        return
    bucket[record.id] = record


def _record_from_row(kind: str, row: Dict[str, Any], country: str, **extra: str) -> Optional[EntityRecord]:
    entity_id = parse_sheet_id(row.get("id", ""))
    if not entity_id:
        return None
    ids = normalize_external_ids({
        source: row.get(source, "") for source in constants.EXTERNAL_ID_SOURCES
    })
    return EntityRecord(
        kind=kind,
        id=entity_id,
        name=str(extra.get("name") or row.get("name") or "").strip(),
        surname=str(extra.get("surname") or row.get("surname") or "").strip(),
        ts_id=ids.get(constants.EXTERNAL_ID_TS, ""),
        uz_id=ids.get(constants.EXTERNAL_ID_UZ, ""),
        ua_id=ids.get(constants.EXTERNAL_ID_UA, ""),
        countries=[country],
    )


def collect_entity_sets(
    exporter: Optional[GoogleSheetsExporter] = None,
) -> EntitySets:
    """Build tournament / team / player sets from every country tab."""
    exporter = exporter or GoogleSheetsExporter()
    sets = EntitySets()
    if not exporter.is_available():
        return sets
    snapshot = exporter.public_workbook_snapshot()
    for country, data in snapshot.items():
        names = {}
        for row in data.get("names") or []:
            tid = parse_sheet_id(row.get("id", ""))
            title = str(row.get("name") or "").strip()
            if tid and title:
                names[tid] = title
        for row in data.get("tournaments") or []:
            year = str(row.get("year") or "").strip()
            game = str(row.get("game") or "").strip()
            fallback = " ".join(part for part in (year, game) if part)
            record = _record_from_row(
                KIND_TOURNAMENT,
                row,
                country,
                name=names.get(parse_sheet_id(row.get("id", "")), fallback),
            )
            if record:
                _put(sets.tournaments, record)
        for row in data.get("teams") or []:
            record = _record_from_row(KIND_TEAM, row, country)
            if record:
                _put(sets.teams, record)
        for row in data.get("players") or []:
            record = _record_from_row(KIND_PLAYER, row, country)
            if record:
                _put(sets.players, record)
    return sets


def _records_from_sheet_values(
    kind: str, values: List[List[Any]]
) -> Dict[int, EntityRecord]:
    bucket: Dict[int, EntityRecord] = {}
    if not values:
        return bucket
    header = [str(cell).strip() for cell in values[0]]
    for raw in values[1:]:
        if not raw or all(not str(cell).strip() for cell in raw):
            continue
        record_row = dict(zip(header, list(raw) + [""] * (len(header) - len(raw))))
        parsed = _record_from_row(kind, record_row, "")
        if not parsed:
            continue
        parsed.countries = []
        _put(bucket, parsed)
    return bucket


def read_entity_sets(exporter: GoogleSheetsExporter) -> EntitySets:
    """Load the tournament / team / player catalog tabs."""
    sets = EntitySets()
    if not exporter.is_available():
        return sets
    for kind, title in constants.ENTITY_SET_WORKSHEETS.items():
        try:
            worksheet = exporter.spreadsheet.worksheet_by_title(title)
        except Exception:
            continue
        try:
            values = worksheet.get_all_values()
        except Exception as exc:
            print(f"Warning: failed to read '{title}': {exc}")
            continue
        for entity_id, record in _records_from_sheet_values(kind, values).items():
            sets.bucket(kind)[entity_id] = record
    return sets


def write_entity_sets(exporter: GoogleSheetsExporter, sets: EntitySets) -> bool:
    """Rewrite the tournament / team / player catalog tabs from ``sets``."""
    if not exporter.is_available():
        return False
    ok = True
    for kind, title in constants.ENTITY_SET_WORKSHEETS.items():
        records = sorted(sets.bucket(kind).values(), key=lambda item: item.id)
        payload: List[List[Any]] = [entity_set_headers(kind)]
        payload.extend(record.to_set_row() for record in records)
        try:
            try:
                worksheet = exporter.spreadsheet.worksheet_by_title(title)
            except Exception:
                worksheet = exporter.spreadsheet.add_worksheet(title)
            worksheet.clear(fields="*")
            worksheet.update_values("A1", payload, parse=False)
            print(f"Wrote {len(records)} row(s) to '{title}'")
        except Exception as exc:
            print(f"Warning: failed to write '{title}': {exc}")
            ok = False
    return ok


def merge_entity_sets(primary: EntitySets, extra: EntitySets) -> EntitySets:
    """Keep ``primary`` rows; fill missing names/ids from ``extra``."""
    merged = EntitySets()
    for kind in constants.ENTITY_KINDS:
        bucket = merged.bucket(kind)
        for record in primary.bucket(kind).values():
            bucket[record.id] = record
        for record in extra.bucket(kind).values():
            _put(bucket, record)
    return merged


def load_entity_sets(exporter: GoogleSheetsExporter) -> EntitySets:
    """Prefer catalog tabs; scan country tabs when those sheets are empty."""
    stored = read_entity_sets(exporter)
    if stored.tournaments or stored.teams or stored.players:
        return stored
    return collect_entity_sets(exporter)


def refresh_entity_sets(
    exporter: GoogleSheetsExporter,
    *,
    write: bool = True,
    id_maps: Optional[Dict[str, Dict[int, int]]] = None,
) -> EntitySets:
    """Scan country tabs, merge with stored catalogs, optionally write them back."""
    stored = read_entity_sets(exporter)
    if id_maps:
        apply_id_maps_to_sets(stored, id_maps)
    scanned = collect_entity_sets(exporter)
    sets = merge_entity_sets(scanned, stored)
    if write:
        write_entity_sets(exporter, sets)
    return sets


def find_duplicate_pairs(sets: EntitySets) -> List[DoubleRow]:
    """Pairs of internal ids that share ts_id, uz_id or ua_id."""
    rows: List[DoubleRow] = []
    for kind in constants.ENTITY_KINDS:
        rows.extend(_pairs_for_kind(kind, sets.bucket(kind)))
    rows.sort(key=lambda row: (row.kind, row.id1, row.id2))
    return rows


def _pairs_for_kind(kind: str, records: Dict[int, EntityRecord]) -> List[DoubleRow]:
    by_source: Dict[str, Dict[str, set]] = {
        source: defaultdict(set) for source in constants.EXTERNAL_ID_SOURCES
    }
    for record in records.values():
        ids = record.external_ids()
        if not ids:
            continue
        for source, value in ids.items():
            by_source[source][value].add(record.id)
    shared: Dict[Tuple[int, int], Dict[str, str]] = {}
    for source, values in by_source.items():
        for value, entity_ids in values.items():
            if len(entity_ids) < 2:
                continue
            for left, right in combinations(sorted(entity_ids), 2):
                shared.setdefault((left, right), empty_external_ids())[source] = value
    rows: List[DoubleRow] = []
    for (id1, id2), ids in shared.items():
        first, second = records[id1], records[id2]
        rows.append(DoubleRow(
            kind=kind,
            ts_id=ids.get(constants.EXTERNAL_ID_TS, ""),
            uz_id=ids.get(constants.EXTERNAL_ID_UZ, ""),
            ua_id=ids.get(constants.EXTERNAL_ID_UA, ""),
            id1=id1,
            name1=first.name,
            surname1=first.surname,
            id2=id2,
            name2=second.name,
            surname2=second.surname,
        ))
    return rows


def _replace_value(raw: Any) -> str:
    """Keep the cell as typed; only 'yes' is treated as a merge request later."""
    return "" if raw is None else str(raw).strip()


def read_doubles_sheet(exporter: GoogleSheetsExporter) -> List[DoubleRow]:
    if not exporter.is_available():
        return []
    try:
        worksheet = exporter.spreadsheet.worksheet_by_title(constants.DOUBLES_WORKSHEET)
    except Exception:
        return []
    values = worksheet.get_all_values()
    if not values:
        return []
    header = [str(cell).strip() for cell in values[0]]
    rows: List[DoubleRow] = []
    for raw in values[1:]:
        if not raw or all(not str(cell).strip() for cell in raw):
            continue
        record = dict(zip(header, list(raw) + [""] * (len(header) - len(raw))))
        kind = str(record.get("kind") or "").strip()
        id1 = parse_sheet_id(record.get("id1", ""))
        id2 = parse_sheet_id(record.get("id2", ""))
        if not kind or not id1 or not id2 or id1 == id2:
            continue
        if id1 > id2:
            id1, id2 = id2, id1
            record["name1"], record["name2"] = record.get("name2", ""), record.get("name1", "")
            record["surname1"], record["surname2"] = (
                record.get("surname2", ""), record.get("surname1", "")
            )
        rows.append(DoubleRow(
            kind=kind,
            ts_id=str(record.get("ts_id") or "").strip(),
            uz_id=str(record.get("uz_id") or "").strip(),
            ua_id=str(record.get("ua_id") or "").strip(),
            id1=id1,
            name1=str(record.get("name1") or "").strip(),
            surname1=str(record.get("surname1") or "").strip(),
            id2=id2,
            name2=str(record.get("name2") or "").strip(),
            surname2=str(record.get("surname2") or "").strip(),
            replace=_replace_value(record.get("replace?")),
        ))
    return rows


def _sort_double_rows(rows: Iterable[DoubleRow]) -> List[DoubleRow]:
    def key(row: DoubleRow) -> tuple:
        confirmed = parse_bool_flag(row.replace, default=False)
        return (1 if confirmed else 0, row.kind, row.id1, row.id2)
    return sorted(rows, key=key)


def merge_double_rows(
    detected: List[DoubleRow],
    existing: List[DoubleRow],
) -> List[DoubleRow]:
    """Keep manual replace? values; add new pairs; keep old yes-rows at the end."""
    by_key = {row.key: row for row in existing}
    merged: Dict[DoubleKey, DoubleRow] = {}
    for row in detected:
        previous = by_key.get(row.key)
        if previous:
            row.replace = previous.replace
        merged[row.key] = row
    for row in existing:
        merged.setdefault(row.key, row)
    return _sort_double_rows(merged.values())


def write_doubles_sheet(
    exporter: GoogleSheetsExporter,
    rows: List[DoubleRow],
) -> bool:
    if not exporter.is_available():
        return False
    try:
        try:
            worksheet = exporter.spreadsheet.worksheet_by_title(constants.DOUBLES_WORKSHEET)
        except Exception:
            worksheet = exporter.spreadsheet.add_worksheet(constants.DOUBLES_WORKSHEET)
        payload: List[List[Any]] = [list(DOUBLES_HEADERS)]
        payload.extend(row.to_sheet_row() for row in _sort_double_rows(rows))
        worksheet.clear(fields="*")
        worksheet.update_values("A1", payload, parse=False)
        print(f"Wrote {len(rows)} row(s) to '{constants.DOUBLES_WORKSHEET}'")
        return True
    except Exception as exc:
        print(f"Warning: failed to write {constants.DOUBLES_WORKSHEET}: {exc}")
        return False


def sync_doubles_sheet(
    exporter: Optional[GoogleSheetsExporter] = None,
    *,
    write: bool = True,
) -> List[DoubleRow]:
    """Scan country tabs and refresh the doubles sheet (preserving replace?).

    Tournament / team / player catalogs are loaded from their own tabs, rebuilt
    from country worksheets, and written back when ``write`` is true.
    """
    exporter = exporter or GoogleSheetsExporter()
    sets = refresh_entity_sets(exporter, write=write)
    detected = find_duplicate_pairs(sets)
    existing = read_doubles_sheet(exporter) if exporter.is_available() else []
    rows = merge_double_rows(detected, existing)
    print(
        f"Duplicate check: {len(detected)} pair(s) by ts_id/uz_id/ua_id "
        f"({len(sets.tournaments)} tournaments, {len(sets.teams)} teams, "
        f"{len(sets.players)} players)."
    )
    if write:
        write_doubles_sheet(exporter, rows)
    elif detected:
        for row in detected:
            print(
                f"  {row.kind}: {row.id1} {row.name1} {row.surname1}".rstrip()
                + f" <-> {row.id2} {row.name2} {row.surname2}".rstrip()
                + f" (ts={row.ts_id or '-'} uz={row.uz_id or '-'} ua={row.ua_id or '-'})"
            )
    return rows


def check_doubles_cli(
    *,
    read_only: bool = False,
    spreadsheet_id: Optional[str] = None,
) -> bool:
    exporter = GoogleSheetsExporter(spreadsheet_id=spreadsheet_id)
    if not exporter.is_available():
        print("Google Sheets is not available.")
        return False
    sync_doubles_sheet(exporter, write=not read_only)
    return True


def _transitive_map(mapping: Dict[int, int]) -> Dict[int, int]:
    resolved: Dict[int, int] = {}

    def root(value: int) -> int:
        seen = set()
        current = value
        while current in mapping and current not in seen:
            seen.add(current)
            current = mapping[current]
        return current

    for source in mapping:
        resolved[source] = root(source)
    return {old: new for old, new in resolved.items() if old != new}


def _merge_team(keep: Team, incoming: Team) -> Team:
    keep.name = keep.name or incoming.name
    keep.city = keep.city or incoming.city
    keep.non_russian_name = keep.non_russian_name or incoming.non_russian_name
    keep.external_ids = merge_external_ids(keep.external_ids, incoming.external_ids)
    return keep


def _merge_player(keep: Player, incoming: Player) -> Player:
    keep.name = keep.name or incoming.name
    keep.surname = keep.surname or incoming.surname
    keep.non_russian_name = keep.non_russian_name or incoming.non_russian_name
    keep.non_russian_surname = keep.non_russian_surname or incoming.non_russian_surname
    keep.external_ids = merge_external_ids(keep.external_ids, incoming.external_ids)
    return keep


def _as_team(raw: Any) -> Team:
    return raw if isinstance(raw, Team) else Team.from_dict(raw)


def _as_player(raw: Any) -> Player:
    return raw if isinstance(raw, Player) else Player.from_dict(raw)


def apply_id_maps(data: Dict[str, Any], maps: Dict[str, Dict[int, int]]) -> bool:
    """Rewrite id2 → id1 in one country payload. Returns True when something changed."""
    team_map = _transitive_map(maps.get(KIND_TEAM) or {})
    player_map = _transitive_map(maps.get(KIND_PLAYER) or {})
    tournament_map = _transitive_map(maps.get(KIND_TOURNAMENT) or {})
    if not team_map and not player_map and not tournament_map:
        return False
    changed = False

    teams: Dict[int, Team] = {}
    team_rows = [_as_team(raw) for raw in (data.get("teams") or {}).values()]
    team_rows.sort(key=lambda team: 1 if team.id in team_map else 0)
    for team in team_rows:
        new_id = team_map.get(team.id, team.id)
        if new_id != team.id:
            team.id = new_id
            changed = True
        if new_id in teams:
            teams[new_id] = _merge_team(teams[new_id], team)
            changed = True
        else:
            teams[new_id] = team
    data["teams"] = {str(team.id): team.to_dict() for team in teams.values()}

    players: Dict[int, Player] = {}
    player_rows = [_as_player(raw) for raw in (data.get("players") or {}).values()]
    player_rows.sort(key=lambda player: 1 if player.id in player_map else 0)
    for player in player_rows:
        new_id = player_map.get(player.id, player.id)
        if new_id != player.id:
            player.id = new_id
            changed = True
        if new_id in players:
            players[new_id] = _merge_player(players[new_id], player)
            changed = True
        else:
            players[new_id] = player
    data["players"] = {str(player.id): player.to_dict() for player in players.values()}

    tournaments = data.get("tournaments") or {}
    collapsed: Dict[str, List[TournamentData]] = {}
    for game, rows in tournaments.items():
        by_id: Dict[int, TournamentData] = {}
        for tournament in rows:
            new_tid = tournament_map.get(tournament.id, tournament.id)
            if new_tid != tournament.id:
                tournament.id = new_tid
                changed = True
            for awardee in tournament.awardees.values():
                if not awardee.individual:
                    new_team = team_map.get(awardee.team.id, awardee.team.id)
                    if new_team != awardee.team.id:
                        awardee.team.id = new_team
                        changed = True
                for player in awardee.team.players:
                    new_player = player_map.get(player.id, player.id)
                    if new_player != player.id:
                        player.id = new_player
                        changed = True
            previous = by_id.get(tournament.id)
            if previous is None:
                by_id[tournament.id] = tournament
            elif len(tournament.awardees) > len(previous.awardees):
                by_id[tournament.id] = tournament
                changed = True
        collapsed[game] = list(by_id.values())
    data["tournaments"] = collapsed

    errors = data.get("errors") or {}
    for item in errors.get("items") or []:
        old = int(item.get("id") or 0)
        new = tournament_map.get(old, old)
        if new != old:
            item["id"] = new
            changed = True
    for item in (data.get("sources") or {}).get("items") or []:
        old = int(item.get("id") or 0)
        new = tournament_map.get(old, old)
        if new != old:
            item["id"] = new
            changed = True
    return changed


def apply_id_maps_to_sets(
    sets: EntitySets, maps: Dict[str, Dict[int, int]]
) -> bool:
    """Rewrite id2 → id1 on the in-memory tournament / team / player catalogs."""
    changed = False
    for kind in constants.ENTITY_KINDS:
        mapping = _transitive_map(maps.get(kind) or {})
        if not mapping:
            continue
        bucket = sets.bucket(kind)
        for old_id, new_id in mapping.items():
            incoming = bucket.pop(old_id, None)
            if incoming is None:
                continue
            incoming.id = new_id
            _put(bucket, incoming)
            changed = True
    return changed


def _replacement_maps(rows: List[DoubleRow]) -> Dict[str, Dict[int, int]]:
    maps: Dict[str, Dict[int, int]] = {
        KIND_TOURNAMENT: {},
        KIND_TEAM: {},
        KIND_PLAYER: {},
    }
    for row in rows:
        if not parse_bool_flag(row.replace, default=False):
            continue
        if row.kind not in maps or not row.id1 or not row.id2 or row.id1 == row.id2:
            continue
        maps[row.kind][row.id2] = row.id1
    return maps


def replace_doubles_cli(
    *,
    read_only: bool = False,
    spreadsheet_id: Optional[str] = None,
    test: bool = False,
) -> bool:
    """Replace id2 with id1 where replace? is yes, then put those rows at the bottom."""
    from counting.stats_generator import StatsGenerator

    test = test or spreadsheet_id == constants.GOOGLE_SHEETS_TEST_SPREADSHEET_ID
    exporter = GoogleSheetsExporter(spreadsheet_id=spreadsheet_id)
    if not exporter.is_available():
        print("Google Sheets is not available.")
        return False
    rows = read_doubles_sheet(exporter)
    maps = _replacement_maps(rows)
    pending = sum(len(mapping) for mapping in maps.values())
    if not pending:
        print("No doubles marked replace?=yes.")
        write_doubles_sheet(exporter, rows)
        return True
    affected: List[str] = []
    for country in exporter.list_country_worksheets():
        data = exporter.load_data(country)
        if not data:
            continue
        if not apply_id_maps(data, maps):
            continue
        affected.append(country)
        print(f"Replacing duplicate ids in {country}")
        if read_only:
            continue
        generator = StatsGenerator(
            country,
            read_only_sheets=False,
            skip_doubles_check=True,
            spreadsheet_id=exporter.spreadsheet_id,
            test=test,
        )
        meta = data["meta"]
        generator._seed_registry_from_loaded(data)
        team_stats, player_stats, tournaments, errors = (
            generator.recalculate_from_tournaments(data["tournaments"])
        )
        generator._save_results(
            meta.numbers_champ,
            team_stats,
            player_stats,
            tournaments,
            data.get("errors"),
            meta=meta,
            sources=data.get("sources"),
        )
    if not affected:
        print("No country tabs contained the marked duplicate ids.")
    else:
        print("Updated countries: " + ", ".join(affected))
    if not read_only:
        refresh_entity_sets(exporter, write=True, id_maps=maps)
    write_doubles_sheet(exporter, rows)
    return True

"""Multi-stage championships: playing phases plus a combined (sum) row."""
from __future__ import annotations

from datetime import date
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from counting import constants
from counting.models import TournamentData
from counting.sheet_utils import parse_sheet_int
from counting.t_fashion import iso_date_is_past


PHASE_ORDINAL_NOM = {
    1: "первый",
    2: "второй",
    3: "третий",
    4: "четвёртый",
    5: "пятый",
    6: "шестой",
    7: "седьмой",
    8: "восьмой",
    9: "девятый",
    10: "десятый",
}

PHASE_CARDINAL = {
    1: "один",
    2: "два",
    3: "три",
    4: "четыре",
    5: "пять",
    6: "шесть",
    7: "семь",
    8: "восемь",
    9: "девять",
    10: "десять",
    11: "одиннадцать",
    12: "двенадцать",
    13: "тринадцать",
    14: "четырнадцать",
    15: "пятнадцать",
    16: "шестнадцать",
    17: "семнадцать",
    18: "восемнадцать",
    19: "девятнадцать",
    20: "двадцать",
}

PHASE_ORDINAL_GEN = {
    1: "первого",
    2: "второго",
    3: "третьего",
    4: "четвёртого",
    5: "пятого",
    6: "шестого",
    7: "седьмого",
    8: "восьмого",
    9: "девятого",
    10: "десятого",
}


def parse_subnumber(raw: object) -> int:
    """Return a positive stage index, or 0 when the cell is blank."""
    value = parse_sheet_int(raw, default=0) or 0
    return value if value > 0 else 0


def edition_key(tournament: TournamentData) -> Tuple[str, int, int]:
    return (
        tournament.game or constants.DEFAULT_GAME,
        int(tournament.number or 0),
        int(tournament.year or 0),
    )


def sort_tournament_rows(rows: Sequence[TournamentData]) -> List[TournamentData]:
    """Newest championship first; within one number, rising subnumber."""
    return sorted(
        rows,
        key=lambda t: (-int(t.number or 0), parse_subnumber(getattr(t, "subnumber", 0))),
    )


def group_editions(rows: Sequence[TournamentData]) -> List[List[TournamentData]]:
    """Keep list order. Subnumbered siblings that share game+number+year are one edition."""
    keyed: Dict[Tuple[str, int, int], List[TournamentData]] = {}
    for tournament in rows:
        if parse_subnumber(getattr(tournament, "subnumber", 0)) <= 0:
            continue
        keyed.setdefault(edition_key(tournament), []).append(tournament)
    multi = {key for key, group in keyed.items() if len(group) >= 2}
    seen = set()
    groups: List[List[TournamentData]] = []
    for tournament in rows:
        key = edition_key(tournament)
        if parse_subnumber(getattr(tournament, "subnumber", 0)) > 0 and key in multi:
            if key in seen:
                continue
            seen.add(key)
            groups.append(
                sorted(keyed[key], key=lambda t: parse_subnumber(t.subnumber))
            )
        else:
            groups.append([tournament])
    return groups


def split_edition_group(
    group: Sequence[TournamentData],
) -> Tuple[List[TournamentData], Optional[TournamentData]]:
    """Playing stages and the combined row. Empty phases means a single-stage edition."""
    if len(group) < 2:
        return [], None
    ordered = sorted(group, key=lambda t: parse_subnumber(getattr(t, "subnumber", 0)))
    return list(ordered[:-1]), ordered[-1]


def flatten_edition_rows(
    tournaments_data: Dict[str, List[TournamentData]],
) -> List[TournamentData]:
    rows: List[TournamentData] = []
    for tournament_list in tournaments_data.values():
        rows.extend(tournament_list)
    return rows


def _multi_groups(
    rows: Sequence[TournamentData],
) -> Dict[Tuple[str, int, int], List[TournamentData]]:
    keyed: Dict[Tuple[str, int, int], List[TournamentData]] = {}
    for tournament in rows:
        if parse_subnumber(getattr(tournament, "subnumber", 0)) <= 0:
            continue
        keyed.setdefault(edition_key(tournament), []).append(tournament)
    return {key: group for key, group in keyed.items() if len(group) >= 2}


def is_non_summary_phase(
    tournament: TournamentData,
    rows: Sequence[TournamentData],
) -> bool:
    """True for a playing stage that has a later combined (sum) sibling."""
    if parse_subnumber(getattr(tournament, "subnumber", 0)) <= 0:
        return False
    group = _multi_groups(rows).get(edition_key(tournament))
    if not group:
        return False
    _, summary = split_edition_group(group)
    return bool(summary and tournament.id and tournament.id != summary.id)


def playing_phases(
    tournament: TournamentData,
    rows: Sequence[TournamentData],
) -> List[TournamentData]:
    """Playing stages of the combined row ``tournament``, otherwise empty."""
    group = _multi_groups(rows).get(edition_key(tournament))
    if not group:
        return []
    phases, summary = split_edition_group(group)
    if summary and tournament.id and tournament.id == summary.id:
        return phases
    return []


def is_multi_phase_summary(
    tournament: TournamentData,
    rows: Sequence[TournamentData],
) -> bool:
    if parse_subnumber(getattr(tournament, "subnumber", 0)) <= 0:
        return False
    group = _multi_groups(rows).get(edition_key(tournament))
    if not group:
        return False
    _, summary = split_edition_group(group)
    return bool(summary and tournament.id and tournament.id == summary.id)


def non_summary_phase_ids(
    tournaments_data: Dict[str, List[TournamentData]],
) -> set[int]:
    rows = flatten_edition_rows(tournaments_data)
    return {
        tournament.id
        for tournament in rows
        if tournament.id and is_non_summary_phase(tournament, rows)
    }


def edition_count(tournaments_data: Dict[str, List[TournamentData]]) -> int:
    """Championships, not raw Tournaments rows (a three-row event counts as one)."""
    total = 0
    for tournament_list in tournaments_data.values():
        total += len(group_editions(tournament_list))
    return total


def phase_noun(count: int) -> str:
    """этап / этапа / этапов after a cardinal."""
    n = abs(int(count)) % 100
    if 11 <= n <= 14:
        return "этапов"
    last = n % 10
    if last == 1:
        return "этап"
    if last in (2, 3, 4):
        return "этапа"
    return "этапов"


def phase_cardinal(count: int) -> str:
    """два, три, … — words, not digits."""
    n = abs(int(count))
    if n in PHASE_CARDINAL:
        return PHASE_CARDINAL[n]
    if n > 20 and n < 100:
        tens = (n // 10) * 10
        ones = n % 10
        ten_word = {
            30: "тридцать",
            40: "сорок",
            50: "пятьдесят",
            60: "шестьдесят",
            70: "семьдесят",
            80: "восемьдесят",
            90: "девяносто",
        }.get(tens)
        if ten_word and ones == 0:
            return ten_word
        if ten_word and ones in PHASE_CARDINAL:
            return f"{ten_word} {PHASE_CARDINAL[ones]}"
    return str(n)


def phase_count_phrase(count: int) -> str:
    """«два этапа», «пять этапов»."""
    n = abs(int(count))
    return f"{phase_cardinal(n)} {phase_noun(n)}"


def phase_ordinal_nominative(index: int, *, capitalize: bool = False) -> str:
    word = PHASE_ORDINAL_NOM.get(index) or f"{index}-й"
    if capitalize:
        return word[:1].upper() + word[1:]
    return word


def phase_ordinal_genitive(index: int) -> str:
    return PHASE_ORDINAL_GEN.get(index) or f"{index}-го"


def edition_is_finished(
    phases: Sequence[TournamentData],
    summary: Optional[TournamentData],
    *,
    today: Optional[date] = None,
) -> bool:
    """True when every dated stage is over, or the year is already past."""
    today = today or date.today()
    dated = [row for row in phases if (row.end_date or row.start_date or "").strip()]
    if dated:
        return all(iso_date_is_past(row.end_date or row.start_date, today) for row in dated)
    year = 0
    if summary:
        year = int(summary.year or 0)
    if not year and phases:
        year = int(phases[0].year or 0)
    return bool(year) and year < today.year


def representative(group: Sequence[TournamentData]) -> TournamentData:
    phases, summary = split_edition_group(group)
    if summary:
        return summary
    return group[0]

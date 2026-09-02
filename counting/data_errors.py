"""Missing-data phrases and the Errors sheet payload."""
from __future__ import annotations

from datetime import date
from typing import Any, Callable, Dict, Iterable, List, Optional

from counting import constants
from counting.models import TournamentAwardee, TournamentData
from counting.sheet_utils import format_bool_flag, parse_bool_flag
from counting.t_fashion import iso_date_is_past, parse_iso_date_parts

CRITICAL_YES = "yes"
CRITICAL_NO = "no"


def empty_errors() -> Dict[str, Any]:
    return {"description": "", "items": []}


def normalize_critical(value: Any) -> str:
    """Errors.critical: yes or no; blank or unknown defaults to yes."""
    return format_bool_flag(parse_bool_flag(value, default=True))


def is_critical_error(item: Dict[str, Any]) -> bool:
    return normalize_critical(item.get("critical")) == CRITICAL_YES


def normalize_errors(errors_data: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """Normalize the Errors payload; ignore the old first/second/third lists."""
    if not errors_data:
        return empty_errors()
    if "items" not in errors_data and "description" not in errors_data:
        return empty_errors()
    items: List[Dict[str, Any]] = []
    for raw in errors_data.get("items") or []:
        if not isinstance(raw, dict):
            continue
        try:
            tid = int(raw.get("id") or 0)
        except (TypeError, ValueError):
            tid = 0
        description = str(raw.get("description") or "").strip()
        if tid or description:
            items.append({
                "id": tid,
                "description": description,
                "critical": normalize_critical(raw.get("critical")),
            })
    return {
        "description": str(errors_data.get("description") or "").strip(),
        "items": items,
    }


def tournament_is_past(tournament: TournamentData, today: Optional[date] = None) -> bool:
    """True when the edition is already over (future editions are not errors).

    If dates are missing, a year before the current calendar year still counts
    as past so 1995 with a blank date is reported.
    """
    today = today or date.today()
    raw = (tournament.end_date or tournament.start_date or "").strip()
    if raw:
        return iso_date_is_past(raw, today)
    year = int(tournament.year or 0)
    return bool(year) and year < today.year


def iso_date_is_complete(value: str) -> bool:
    parts = parse_iso_date_parts((value or "").strip())
    return bool(parts) and parts[1] != 0 and parts[2] != 0


def tournament_date_is_incomplete(tournament: TournamentData) -> bool:
    start = (tournament.start_date or "").strip()
    end = (tournament.end_date or "").strip()
    if iso_date_is_complete(end) and (not start or iso_date_is_complete(start)):
        return False
    if iso_date_is_complete(start) and not end:
        return False
    return True


def _place_incomplete(
    tournament: TournamentData,
    place: int,
    needs_roster_error: Callable[[TournamentAwardee], bool],
) -> bool:
    awardees = [
        awardee for awardee in tournament.awardees.values() if awardee.place == place
    ]
    if not awardees:
        return True
    return any(needs_roster_error(awardee) for awardee in awardees)


def _roster_phrase(winner: bool, second: bool, third: bool, individual: bool) -> str:
    if not (winner or second or third):
        return ""
    if individual:
        if winner and second and third:
            return "неизвестны победитель и обладатели второго и третьего мест"
        if winner and second:
            return "неизвестны победитель и обладатель второго места"
        if winner and third:
            return "неизвестны победитель и обладатель третьего места"
        if second and third:
            return "неизвестны обладатели второго и третьего мест"
        if winner:
            return "неизвестен победитель"
        if second:
            return "неизвестен обладатель второго места"
        return "неизвестен обладатель третьего места"
    if winner and second and third:
        return "неизвестны составы победителя и обладателей второго и третьего мест"
    if winner and second:
        return "неизвестны составы победителя и обладателей второго места"
    if winner and third:
        return "неизвестны составы победителя и обладателей третьего места"
    if second and third:
        return "неизвестны составы обладателей второго и третьего мест"
    if winner:
        return "неизвестен состав победителя"
    if second:
        return "неизвестен состав обладателей второго места"
    return "неизвестен состав обладателей третьего места"


def _strip_verb(phrase: str) -> str:
    for prefix in ("неизвестен ", "неизвестна ", "неизвестно ", "неизвестны "):
        if phrase.startswith(prefix):
            return phrase[len(prefix):]
    return phrase


def format_missing_description(
    *,
    winner: bool = False,
    second: bool = False,
    third: bool = False,
    individual: bool = False,
    city: bool = False,
    date: bool = False,
) -> str:
    """One sentence ending with a period."""
    roster = _roster_phrase(winner, second, third, individual)
    groups: List[tuple[str, str]] = []
    if roster:
        groups.append(("roster", roster))
    if city:
        groups.append(("city", "неизвестно место проведения"))
    if date:
        groups.append(("date", "неизвестна точная дата проведения"))
    if not groups:
        return ""
    if len(groups) == 1:
        return f"{groups[0][1]}."
    nouns: List[str] = []
    for kind, phrase in groups:
        if kind == "city":
            nouns.append("место проведения турнира")
        elif kind == "date":
            nouns.append("точная дата проведения турнира")
        else:
            nouns.append(_strip_verb(phrase))
    return "неизвестны " + ", ".join(nouns) + "."


def collect_computed_errors(
    tournaments_data: Dict[str, List[TournamentData]],
    *,
    needs_roster_error: Callable[[TournamentAwardee], bool],
) -> Dict[str, Any]:
    items: List[Dict[str, Any]] = []
    for tournament_list in tournaments_data.values():
        for tournament in tournament_list:
            if not tournament.id or not tournament_is_past(tournament):
                continue
            individual = tournament.game in constants.INDIVIDUAL_GAMES
            winner = _place_incomplete(tournament, 0, needs_roster_error)
            second = _place_incomplete(tournament, 1, needs_roster_error)
            third = _place_incomplete(tournament, 2, needs_roster_error)
            city = not (tournament.city or "").strip()
            date = tournament_date_is_incomplete(tournament)
            description = format_missing_description(
                winner=winner,
                second=second,
                third=third,
                individual=individual,
                city=city,
                date=date,
            )
            if description:
                items.append({
                    "id": tournament.id,
                    "description": description,
                    "critical": CRITICAL_YES,
                })
    items.sort(key=lambda item: item["id"])
    return {"description": "", "items": items}


def merge_data_errors(
    existing: Optional[Dict[str, Any]],
    computed: Optional[Dict[str, Any]],
    tournaments_data: Optional[Dict[str, List[TournamentData]]] = None,
) -> Dict[str, Any]:
    """Keep sheet description, edited row text, and critical; add new ids.

    Rows for past editions that are now complete are dropped. Rows whose id
    is not in the tournament list are kept (editor notes). Newly detected
    rows default to critical=yes. An editor-set critical=no is preserved.
    """
    sheet = normalize_errors(existing)
    auto = normalize_errors(computed)
    auto_by_id = {item["id"]: item for item in auto["items"] if item.get("id")}
    by_id = flatten_tournaments(tournaments_data or {})
    seen = set()
    items: List[Dict[str, Any]] = []
    for item in sheet["items"]:
        tid = int(item.get("id") or 0)
        description = str(item.get("description") or "").strip()
        critical = normalize_critical(item.get("critical"))
        if tid:
            tournament = by_id.get(tid)
            if tournament and tournament_is_past(tournament) and tid not in auto_by_id:
                continue
            seen.add(tid)
            if not description and tid in auto_by_id:
                description = auto_by_id[tid]["description"]
            items.append({
                "id": tid,
                "description": description,
                "critical": critical,
            })
        elif description:
            items.append({
                "id": 0,
                "description": description,
                "critical": critical,
            })
    for item in auto["items"]:
        tid = int(item.get("id") or 0)
        if tid and tid not in seen:
            items.append({
                "id": tid,
                "description": item["description"],
                "critical": normalize_critical(item.get("critical")),
            })
    return {"description": sheet["description"], "items": items}


def flatten_tournaments(
    tournaments_data: Dict[str, List[TournamentData]],
) -> Dict[int, TournamentData]:
    found: Dict[int, TournamentData] = {}
    for tournament_list in tournaments_data.values():
        for tournament in tournament_list:
            if tournament.id:
                found[tournament.id] = tournament
    return found


def sort_error_items(
    items: Iterable[Dict[str, Any]],
    by_id: Dict[int, TournamentData],
) -> List[Dict[str, Any]]:
    def key(item: Dict[str, Any]) -> tuple:
        tournament = by_id.get(int(item.get("id") or 0))
        if tournament:
            return (0, -int(tournament.year or 0), -int(tournament.number or 0))
        return (1, 0, 0)

    return sorted(items, key=key)

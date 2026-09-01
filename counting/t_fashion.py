import calendar
import re
from datetime import date, datetime
from typing import Dict, Optional, Tuple

import requests
from requests.exceptions import RequestException

MONTHS_RU: Dict[int, str] = {
    1: "января", 2: "февраля", 3: "марта", 4: "апреля",
    5: "мая", 6: "июня", 7: "июля", 8: "августа",
    9: "сентября", 10: "октября", 11: "ноября", 12: "декабря",
}

MONTHS_RU_PREP: Dict[int, str] = {
    1: "январе", 2: "феврале", 3: "марте", 4: "апреле",
    5: "мае", 6: "июне", 7: "июле", 8: "августе",
    9: "сентябре", 10: "октябре", 11: "ноябре", 12: "декабре",
}

ISO_DATE_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")


def transform_date(date_str: str) -> datetime:
    return datetime.strptime(date_str[:10], "%Y-%m-%d")


def parse_iso_date_parts(value: str) -> Optional[Tuple[int, int, int]]:
    """Parse YYYY-MM-DD. Month or day may be 0 (unknown). Returns (year, month, day) or None."""
    value = (value or "").strip()
    match = ISO_DATE_RE.fullmatch(value)
    if not match:
        return None
    year, month, day = int(match.group(1)), int(match.group(2)), int(match.group(3))
    if month == 0:
        return (year, 0, 0) if day == 0 else None
    if month > 12:
        return None
    if day == 0:
        return year, month, 0
    try:
        datetime(year, month, day)
    except ValueError:
        return None
    return year, month, day


def is_iso_date(value: str) -> bool:
    """True for ISO YYYY-MM-DD, including incomplete 1995-00-00 / 1995-08-00."""
    return parse_iso_date_parts(value) is not None


def iso_date_is_incomplete(value: str) -> bool:
    """True when month or day is unknown (00)."""
    parts = parse_iso_date_parts(value)
    return bool(parts) and (parts[1] == 0 or parts[2] == 0)


def iso_date_year(value: str) -> int:
    """Calendar year from an ISO date (complete or incomplete). 0 if unparseable."""
    parts = parse_iso_date_parts(value)
    if parts:
        return parts[0]
    try:
        return transform_date(value).year
    except ValueError:
        return 0


def iso_date_is_past(value: str, today: Optional[date] = None) -> bool:
    """True if this ISO date is already over.

    Year-only (1995-00-00): after that calendar year.
    Month-only (1995-08-00): after the last day of that month.
    Unreadable values are not treated as past.
    """
    today = today or datetime.now().date()
    parts = parse_iso_date_parts(value)
    if parts:
        year, month, day = parts
        if month == 0:
            return year < today.year
        if day == 0:
            last = calendar.monthrange(year, month)[1]
            return date(year, month, last) < today
        return date(year, month, day) < today
    try:
        return transform_date(value).date() < today
    except ValueError:
        return False


def format_iso_date_prepositional(start_date: str, end_date: Optional[str] = None) -> str:
    """«в 1995 году» / «в августе 1995 года» (and ranges). Empty if start is not ISO."""
    start_p = parse_iso_date_parts(start_date)
    end_p = parse_iso_date_parts(end_date or start_date) or start_p
    if not start_p:
        return ""
    sy, sm, _sd = start_p
    ey, em, _ed = end_p
    if sm == 0 or em == 0:
        if sy == ey:
            return f"в {sy} году"
        lo, hi = min(sy, ey), max(sy, ey)
        return f"в {lo}–{hi} годах"
    if sy == ey and sm == em:
        return f"в {MONTHS_RU_PREP[sm]} {sy} года"
    if sy == ey:
        return f"в {MONTHS_RU_PREP[sm]}–{MONTHS_RU_PREP[em]} {sy} года"
    return f"в {MONTHS_RU_PREP[sm]} {sy} года – {MONTHS_RU_PREP[em]} {ey} года"


def to_iso_date(day: int, month: int, year: int) -> str:
    return f"{year:04d}-{month:02d}-{day:02d}"


def get_month(date: datetime) -> str:
    return MONTHS_RU[date.month]


def get_day(date: datetime) -> int:
    return date.day


def get_year(date: datetime) -> int:
    return date.year


def get_tournament_date(date_start: str, date_end: str) -> str:
    start = transform_date(date_start)
    end = transform_date(date_end)
    return prepare_tournament_date(
        get_day(start), get_day(end),
        get_month(start), get_month(end),
        get_year(start), get_year(end),
    )


def format_tournament_date_from_iso(start_date: str, end_date: str = "") -> str:
    """Format YYYY-MM-DD range as Russian text for markdown.

    Incomplete dates (1995-00-00 / 1995-08-00) become a prepositional phrase
    («в 1995 году» / «в августе 1995 года»). Complete dates stay genitive
    («21 августа 1995 года»).
    """
    start = (start_date or "").strip()
    end = (end_date or start).strip() or start
    if not start:
        return ""
    if iso_date_is_incomplete(start) or iso_date_is_incomplete(end):
        return format_iso_date_prepositional(start, end)
    return get_tournament_date(start, end)


def _months_name_to_number() -> Dict[str, int]:
    return {name.lower(): month for month, name in MONTHS_RU.items()}


def _parse_single_russian_date(text: str, months_map: Dict[str, int]) -> Tuple[int, int, int]:
    parts = text.split()
    if len(parts) < 3:
        raise ValueError(f"Invalid date format: {text}")
    day = int(parts[0])
    month_name = parts[1].lower()
    if month_name not in months_map:
        raise ValueError(f"Unknown month name: {parts[1]}")
    year = int(parts[2])
    return day, months_map[month_name], year


def parse_russian_date_range(date_str: str) -> Tuple[str, str]:
    """Parse Russian text or ISO date to (start_iso, end_iso)."""
    date_str = date_str.strip()
    if not date_str:
        return "", ""
    if is_iso_date(date_str):
        return date_str, date_str

    cleaned = date_str.replace("года", "").strip()
    months_map = _months_name_to_number()

    for sep in (" – ", " — "):
        if sep in cleaned:
            left, right = cleaned.split(sep, 1)
            sd, sm, sy = _parse_single_russian_date(left.strip(), months_map)
            ed, em, ey = _parse_single_russian_date(right.strip(), months_map)
            return to_iso_date(sd, sm, sy), to_iso_date(ed, em, ey)

    same_month = re.match(r"^(\d{1,2})[-–—](\d{1,2})\s+(\S+)\s+(\d{4})$", cleaned)
    if same_month:
        sd, ed, month_name, year = same_month.groups()
        month = months_map[month_name.lower()]
        y = int(year)
        return to_iso_date(int(sd), month, y), to_iso_date(int(ed), month, y)

    cross_month = re.match(
        r"^(\d{1,2})\s+(\S+)[-–—](\d{1,2})\s+(\S+)\s+(\d{4})$", cleaned
    )
    if cross_month:
        sd, sm_name, ed, em_name, year = cross_month.groups()
        y = int(year)
        return (
            to_iso_date(int(sd), months_map[sm_name.lower()], y),
            to_iso_date(int(ed), months_map[em_name.lower()], y),
        )

    day, month, year = _parse_single_russian_date(cleaned, months_map)
    iso = to_iso_date(day, month, year)
    return iso, iso


def parse_date_field(value: str) -> Tuple[str, str]:
    """Parse a sheet or legacy date field to ISO start/end."""
    return parse_russian_date_range(value)


def normalize_tournament_dates(
    start_date: str, end_date: str, legacy_date: str = ""
) -> Tuple[str, str, str]:
    """Return (start_iso, end_iso, display_date)."""
    start = (start_date or "").strip()
    end = (end_date or "").strip()
    if not start and not end and legacy_date:
        try:
            start, end = parse_date_field(legacy_date)
        except ValueError:
            return "", "", legacy_date
    if start and not end:
        end = start
    if end and not start:
        start = end
    display = format_tournament_date_from_iso(start, end) if start else (legacy_date or "")
    return start, end, display


def tournament_display_date(start_date: str, end_date: str, legacy_date: str = "") -> str:
    """Preferred Russian date string for markdown output."""
    _, _, display = normalize_tournament_dates(start_date, end_date, legacy_date)
    return display


def inflect_town(town_name: str) -> str:
    if not town_name:
        return town_name
    last_char = town_name[-1].lower()
    if last_char in "бвгджзклмнпрстфхцчшщ":
        return town_name + "е"
    if last_char == "ь":
        return town_name[:-1] + "и"
    if last_char in "ая":
        return town_name[:-1] + "е"
    return town_name


def prepare_tournament_date(sd: int, ed: int, sm: str, em: str, sy: int, ey: int) -> str:
    if sy == ey:
        if sm == em:
            return f"{sd}–{ed} {sm} {sy} года" if sd != ed else f"{sd} {sm} {sy} года"
        return f"{sd} {sm}–{ed} {em} {ey} года"
    return f"{sd} {sm} {sy} года – {ed} {em} {ey} года"


def get_city_tournament(city_id: int) -> str:
    url = f"https://api.rating.chgk.net/towns/{city_id}.json"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()["name"]
    except RequestException as exc:
        print(f"Error fetching city {city_id}: {exc}")
        return ""


def parse_russian_date(date_str: str) -> Tuple[int, int, int]:
    """Parse a single-day Russian date."""
    cleaned = date_str.replace("года", "").strip()
    return _parse_single_russian_date(cleaned, _months_name_to_number())


def format_date_for_tournament(day: int, month: int, year: int) -> str:
    return f"{day} {MONTHS_RU[month]} {year} года"

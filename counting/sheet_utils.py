"""Shared helpers for Google Sheets and tournament link/error handling."""
from datetime import datetime
from typing import Any, Dict, List, Optional

from counting import constants
from counting.external_ids import get_external_id

LINK_KEYS = (
    "results", "announce", "site", "tg", "fb", "vk", "lj", "recap", "letopis",
    "photos", "questions",
)

TOURNAMENT_HEADERS = [
    "id", "number", "game", "start_date", "end_date", "city", "year",
    "countable",
    *constants.EXTERNAL_ID_SOURCES,
    "comment",
]

# One row per tournament that has any URL; keyed by tournament internal id.
LINK_HEADERS = ["id", *LINK_KEYS]

TEAM_REGISTRY_HEADERS = [
    "id", "name", "non_russian_name", "city", *constants.EXTERNAL_ID_SOURCES,
]

PLAYER_REGISTRY_HEADERS = [
    "id", "name", "surname", "non_russian_name", "non_russian_surname",
    *constants.EXTERNAL_ID_SOURCES,
]

PODIUM_HEADERS = [
    "id", "place",
    "team id", "team name", "old name", "team city", "roster_complete",
]

ROSTER_HEADERS = [
    "id", "place", "team id",
    "player id", "player name", "player surname", "old_name", "old_surname",
]

# Individual-game podium (SSI): one player per place, no team.
INDIVIDUAL_HEADERS = [
    "id", "place", "player id", "player name", "player surname",
    "old_name", "old_surname", "sex",
]

# One row per language, so a tournament can list several.
LANGUAGE_HEADERS = ["id", "language", "name"]

# Title override for a single edition, keyed by tournament internal id.
NAME_HEADERS = ["id", "name"]

# Manual bibliography; several rows may share a tournament id.
SOURCE_HEADERS = ["id", "year", "link", "link_name", "comment"]

# Tournament videos; several rows may share a tournament id.
VIDEO_HEADERS = ["id", "name", "year", "link", "link_name", "description"]

# Missing-data rows in the Errors section; keyed by tournament internal id.
ERROR_HEADERS = ["id", "description", "critical"]

# Cross-country duplicate pairs on the doubles tab.
DOUBLES_HEADERS = [
    "kind",
    "ts_id",
    "uz_id",
    "ua_id",
    "id1",
    "name1",
    "surname1",
    "id2",
    "name2",
    "surname2",
    "replace?",
]

# Global catalogs on the tournament / team / player tabs.
ENTITY_SET_HEADERS = ["id", "name", *constants.EXTERNAL_ID_SOURCES]
PLAYER_SET_HEADERS = ["id", "name", "surname", *constants.EXTERNAL_ID_SOURCES]


def entity_set_headers(kind: str) -> List[str]:
    """Column headers for a catalog tab; only players have ``surname``."""
    if kind == constants.KIND_PLAYER:
        return list(PLAYER_SET_HEADERS)
    return list(ENTITY_SET_HEADERS)


def default_links() -> Dict[str, str]:
    """Return empty links dict with all expected keys."""
    return {key: "" for key in LINK_KEYS}


def merge_links(links: Dict[str, str] | None) -> Dict[str, str]:
    """Merge partial links with defaults."""
    merged = default_links()
    if links:
        for key in LINK_KEYS:
            if key in links and links[key]:
                merged[key] = links[key]
    return merged


def has_links(links: Dict[str, str] | None) -> bool:
    """True when at least one URL column is filled."""
    if not links:
        return False
    return any(str(links.get(key) or "").strip() for key in LINK_KEYS)


_TRUE_VALUES = ("yes", "y", "true", "1", "да")
_FALSE_VALUES = ("no", "n", "false", "0", "нет")


def normalize_age(value: Any) -> str:
    """Normalize an age category; blank or unknown values become adult."""
    text = "" if value is None else str(value).strip().lower()
    if text in constants.AGES:
        return text
    return constants.DEFAULT_AGE


def normalize_sex(value: Any) -> str:
    """Normalize Individuals ``sex``; blank or unknown values become male."""
    text = "" if value is None else str(value).strip().lower()
    if text in constants.SEXES:
        return text
    return constants.DEFAULT_SEX


def parse_bool_flag(value: Any, default: bool = False) -> bool:
    """Parse a boolean column; blank or unrecognized cells fall back to default."""
    if isinstance(value, bool):
        return value
    text = "" if value is None else str(value).strip().lower()
    if text in _TRUE_VALUES:
        return True
    if text in _FALSE_VALUES:
        return False
    return default


def format_bool_flag(value: bool) -> str:
    """Format a boolean column for sheet export."""
    return "yes" if value else "no"


def parse_roster_complete(value: str) -> bool:
    """Parse roster_complete column (yes/no, true/false, 1/0)."""
    return parse_bool_flag(value, default=False)


def format_roster_complete(complete: bool) -> str:
    """Format roster_complete for sheet export."""
    return format_bool_flag(complete)


# Day zero of Google Sheets' date serial numbers.
SHEETS_EPOCH = datetime(1899, 12, 30)
_SHEET_DATE_FORMATS = ("%m/%d/%Y", "%d/%m/%Y", "%d.%m.%Y", "%Y-%m-%d")


def parse_sheet_int(raw: Any, default: Optional[int] = 0) -> Optional[int]:
    """Parse an integer cell that Google Sheets may have rendered as a date.

    Cells that inherited a date number format display their integer value as
    a date (serial days since 1899-12-30, e.g. place ``1`` → ``12/31/1899``).
    Such strings are converted back to the underlying integer.
    """
    if isinstance(raw, bool):
        return default
    if isinstance(raw, (int, float)):
        return int(raw)
    text = str(raw or "").strip()
    if not text:
        return default
    try:
        return int(float(text))
    except ValueError:
        pass
    for fmt in _SHEET_DATE_FORMATS:
        try:
            return (datetime.strptime(text, fmt) - SHEETS_EPOCH).days
        except ValueError:
            continue
    return default


def parse_sheet_id(raw: str | int | None) -> int:
    """Parse id from sheet cell; 0 if blank or zero.

    Accepts ints, ``147.0`` from Sheets number cells, and date-formatted
    serials the same way ``parse_sheet_int`` does. ``int("147.0")`` would
    raise and abort a country load.
    """
    if raw is None or str(raw).strip() == "":
        return 0
    value = parse_sheet_int(raw, default=None)
    if value is None or value == 0:
        return 0
    return int(value)


def format_sheet_id(entity_id: int) -> str | int:
    """Format id for sheet export; blank cell when missing."""
    return "" if not entity_id else entity_id


def player_profile_url(external_ids: Optional[Dict[str, str]] = None) -> str:
    """Return rating.chgk.info player URL when ts_id is present."""
    ts_id = get_external_id(external_ids, constants.EXTERNAL_ID_TS)
    if ts_id:
        return f"https://rating.chgk.info/player/{ts_id}"
    return ""


def team_profile_url(external_ids: Optional[Dict[str, str]] = None) -> str:
    """Return rating.chgk.info team URL when ts_id is present."""
    ts_id = get_external_id(external_ids, constants.EXTERNAL_ID_TS)
    if ts_id:
        return f"https://rating.chgk.info/teams/{ts_id}"
    return ""

"""External identity map helpers (no model imports)."""
from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse

from counting import constants

# Hosts used to classify a free-form results URL.
RESULTS_HOST_TS = ("rating.chgk.info", "www.rating.chgk.info")
RESULTS_HOST_UZ = ("turnirlar.uz", "www.turnirlar.uz")
RESULTS_HOST_SHEETS = ("docs.google.com", "sheets.google.com")


def empty_external_ids() -> Dict[str, str]:
    return {source: "" for source in constants.EXTERNAL_ID_SOURCES}


def normalize_external_ids(raw: Optional[Dict[str, Any]]) -> Dict[str, str]:
    """Keep known sources only; one string value per source; drop blanks."""
    if not raw:
        return {}
    result: Dict[str, str] = {}
    for source in constants.EXTERNAL_ID_SOURCES:
        value = raw.get(source, "")
        text = str(value).strip() if value is not None else ""
        if text and text != "0":
            result[source] = text
    return result


def merge_external_ids(
    existing: Optional[Dict[str, Any]],
    incoming: Optional[Dict[str, Any]],
) -> Dict[str, str]:
    """Merge maps; existing values win on conflict for the same source."""
    merged = dict(normalize_external_ids(existing))
    for source, value in normalize_external_ids(incoming).items():
        merged.setdefault(source, value)
    return merged


def get_external_id(external_ids: Optional[Dict[str, str]], source: str) -> str:
    if not external_ids:
        return ""
    return str(external_ids.get(source, "") or "").strip()


def external_ids_from_row(row: Dict[str, Any]) -> Dict[str, str]:
    return normalize_external_ids(
        {source: row.get(source, "") for source in constants.EXTERNAL_ID_SOURCES}
    )


def external_id_row_values(external_ids: Optional[Dict[str, str]]) -> List[str]:
    ids = normalize_external_ids(external_ids)
    return [ids.get(source, "") for source in constants.EXTERNAL_ID_SOURCES]


def results_url_from_external_ids(external_ids: Optional[Dict[str, str]]) -> str:
    """Build a results page URL from known external tournament ids."""
    ts_id = get_external_id(external_ids, constants.EXTERNAL_ID_TS)
    if ts_id:
        return f"https://rating.chgk.info/tournament/{ts_id}"
    uz_id = get_external_id(external_ids, constants.EXTERNAL_ID_UZ)
    if uz_id:
        return f"https://turnirlar.uz/tournament/{uz_id}"
    return ""


def resolve_results_url(
    results_link: Optional[str] = None,
    external_ids: Optional[Dict[str, str]] = None,
) -> str:
    """Prefer an explicit results URL; else derive from ts_id / uz_id."""
    explicit = (results_link or "").strip()
    if explicit:
        return explicit
    return results_url_from_external_ids(external_ids)


def missing_data_tournament_url(
    results_link: Optional[str] = None,
    external_ids: Optional[Dict[str, str]] = None,
) -> str:
    """Name link in the Нет данных table: rating.chgk.info, else ts_id, else ua_id."""
    explicit = (results_link or "").strip()
    if explicit and classify_results_url(explicit) == "ts":
        return explicit
    ts_id = get_external_id(external_ids, constants.EXTERNAL_ID_TS)
    if ts_id:
        return f"https://rating.chgk.info/tournament/{ts_id}"
    ua_id = get_external_id(external_ids, constants.EXTERNAL_ID_UA)
    template = (constants.UA_TOURNAMENT_URL_TEMPLATE or "").strip()
    if ua_id and template:
        return template.format(id=ua_id)
    return ""


def classify_results_url(url: str) -> str:
    """Return a short source tag: ts, uz, sheets, or other."""
    host = urlparse(url).netloc.lower()
    if host in RESULTS_HOST_TS:
        return "ts"
    if host in RESULTS_HOST_UZ:
        return "uz"
    if host in RESULTS_HOST_SHEETS or "spreadsheets" in url.lower():
        return "sheets"
    return "other"


def results_markdown_label(url: str) -> str:
    """Human-readable link label for the results line in markdown."""
    kind = classify_results_url(url)
    if kind == "ts":
        return "на турнирном сайте"
    if kind == "uz":
        return "на сайте turnirlar.uz"
    if kind == "sheets":
        return "в этой гуглтаблице"
    return "на этой странице"


def parse_external_id_from_results_url(url: str) -> Dict[str, str]:
    """Extract ts_id / uz_id from a known results URL when possible."""
    text = (url or "").strip()
    if not text:
        return {}
    kind = classify_results_url(text)
    path = urlparse(text).path.rstrip("/")
    if "/tournament/" not in path:
        return {}
    tournament_key = path.split("/tournament/")[-1].split("/")[0].strip()
    if not tournament_key:
        return {}
    if kind == "ts":
        return {constants.EXTERNAL_ID_TS: tournament_key}
    if kind == "uz":
        return {constants.EXTERNAL_ID_UZ: tournament_key}
    return {}

"""Manual Sources sheet payload and markdown/HTML formatting."""
from __future__ import annotations

import html
from typing import Any, Dict, Iterable, List, Optional, Tuple

from counting.sheet_utils import parse_sheet_id, parse_sheet_int


def empty_sources() -> Dict[str, Any]:
    return {"description": "", "items": []}


def normalize_sources(data: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """Keep editor-entered Sources rows; never invent them."""
    if not data:
        return empty_sources()
    items: List[Dict[str, Any]] = []
    for raw in data.get("items") or []:
        if not isinstance(raw, dict):
            continue
        item = _normalize_source_item(raw)
        if item:
            items.append(item)
    return {
        "description": str(data.get("description") or "").strip(),
        "items": items,
    }


def _normalize_source_item(raw: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    tid = parse_sheet_id(raw.get("id"))
    if not tid:
        return None
    link = str(raw.get("link") or "").strip()
    name = str(raw.get("link_name") or raw.get("link name") or "").strip()
    comment = str(raw.get("comment") or "").strip()
    if not (link or name or comment):
        return None
    year = parse_sheet_int(raw.get("year"), default=0) or 0
    return {
        "id": tid,
        "year": year,
        "link": link,
        "link_name": name,
        "comment": comment,
    }


def group_sources_by_id(
    items: Iterable[Dict[str, Any]],
) -> List[Tuple[int, List[Dict[str, Any]]]]:
    """Keep first-seen id order; several rows with the same id stay together."""
    grouped: Dict[int, List[Dict[str, Any]]] = {}
    order: List[int] = []
    for item in items:
        tid = int(item.get("id") or 0)
        if not tid:
            continue
        if tid not in grouped:
            grouped[tid] = []
            order.append(tid)
        grouped[tid].append(item)
    return [(tid, grouped[tid]) for tid in order]


def group_year(rows: List[Dict[str, Any]], fallback: int = 0) -> int:
    """Year stored on Sources rows; first non-empty value wins."""
    for row in rows:
        year = parse_sheet_int(row.get("year"), default=0) or 0
        if year:
            return year
    return int(fallback or 0)


def source_column_title(groups: List[Tuple[int, List[Dict[str, Any]]]]) -> str:
    """«Источник» when every tournament has one row, else «Источники»."""
    from counting import constants

    if any(len(rows) > 1 for _, rows in groups):
        return constants.SOURCES_MANY
    return constants.SOURCES_ONE


def source_phrase_html(item: Dict[str, Any]) -> str:
    """One source: link with caption, optional comment in parentheses."""
    link = str(item.get("link") or "").strip()
    name = str(item.get("link_name") or "").strip()
    comment = str(item.get("comment") or "").strip()
    if link:
        label = html.escape(name) if name else html.escape(link)
        core = f'<a href="{html.escape(link, quote=True)}">{label}</a>'
    else:
        core = html.escape(name)
    if comment:
        wrapped = f"({html.escape(comment)})"
        return f"{core} {wrapped}" if core else wrapped
    return core


def join_source_phrases(rows: List[Dict[str, Any]]) -> str:
    phrases = [source_phrase_html(row) for row in rows]
    return ", ".join(part for part in phrases if part)

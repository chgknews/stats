"""Manual Video sheet payload and tournament markdown."""
from __future__ import annotations

from typing import Any, Dict, Iterable, List, Optional

from counting import constants
from counting.sheet_utils import parse_sheet_id, parse_sheet_int


def empty_videos() -> List[Dict[str, Any]]:
    return []


def normalize_videos(data: Optional[Iterable[Any]]) -> List[Dict[str, Any]]:
    """Keep editor-entered Video rows; never invent them."""
    if not data:
        return empty_videos()
    items: List[Dict[str, Any]] = []
    for raw in data:
        if not isinstance(raw, dict):
            continue
        item = _normalize_video_item(raw)
        if item:
            items.append(item)
    return items


def _normalize_video_item(raw: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    tid = parse_sheet_id(raw.get("id"))
    if not tid:
        return None
    link = str(raw.get("link") or "").strip()
    name = str(raw.get("name") or "").strip()
    link_name = str(raw.get("link_name") or raw.get("link name") or "").strip()
    description = str(
        raw.get("description") or raw.get("decription") or ""
    ).strip()
    if not (link or name or link_name or description):
        return None
    year = parse_sheet_int(raw.get("year"), default=0) or 0
    return {
        "id": tid,
        "name": name,
        "year": year,
        "link": link,
        "link_name": link_name,
        "description": description,
    }


def videos_for_tournament(
    items: Iterable[Dict[str, Any]], tournament_id: int
) -> List[Dict[str, Any]]:
    """Rows for one tournament, in sheet order; skip rows without a URL."""
    tid = int(tournament_id or 0)
    if not tid:
        return []
    found: List[Dict[str, Any]] = []
    for item in items:
        if int(item.get("id") or 0) != tid:
            continue
        if str(item.get("link") or "").strip():
            found.append(item)
    return found


def video_markdown_phrase(item: Dict[str, Any]) -> str:
    """``[link_name](link)`` plus optional `` (description)``."""
    link = str(item.get("link") or "").strip()
    if not link:
        return ""
    label = str(item.get("link_name") or "").strip() or link
    core = f"[{label}]({link})"
    description = str(item.get("description") or "").strip()
    if description:
        return f"{core} ({description})"
    return core


def video_paragraph(items: List[Dict[str, Any]]) -> str:
    phrases = [video_markdown_phrase(item) for item in items]
    phrases = [part for part in phrases if part]
    if not phrases:
        return ""
    lead = (
        constants.VIDEO_ONE_LABEL if len(phrases) == 1 else constants.VIDEO_MANY_LABEL
    )
    return f"{lead}{', '.join(phrases)}."

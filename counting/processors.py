"""Utility functions for processing tournament data."""
from typing import Dict, Iterable, List, Optional, Set, Tuple

from counting import constants
from counting.models import Awardee
from counting.external_ids import merge_external_ids, normalize_external_ids


def medal_column_groups(games_with_medals: Iterable[str]) -> List[Tuple[str, Tuple[str, ...]]]:
    """Visible I/II/III blocks: (column name key, games whose medals are summed).

    A group is omitted when none of its games have medals. Two or more members
    with medals share one block: medals from **all** members are added together,
    and the title is the merge key (``kvrm`` → «КВРМ», ``brain`` → «БР», …).
    One member with medals keeps that game’s own name and is counted alone.
    """
    present: Set[str] = set(games_with_medals)
    columns: List[Tuple[str, Tuple[str, ...]]] = []
    for merged_name, members in constants.GAME_MEDAL_GROUPS:
        found = tuple(game for game in members if game in present)
        if not found:
            continue
        if len(found) > 1:
            columns.append((merged_name, members))
        else:
            columns.append((found[0], found))
    return columns


def count_champions(
    awardees: Dict[int, Awardee],
    id: int,
    place: int,
    game: str = "chgk",
    name: str = "",
    city: str = "",
    external_ids: Optional[Dict[str, str]] = None,
    non_russian_name: str = "",
) -> Dict[int, Awardee]:
    """Update awardee statistics based on tournament placement (internal id)."""
    awardee = awardees.get(
        id,
        Awardee(
            id=id,
            game=game,
            name=name,
            city=city,
            external_ids=normalize_external_ids(external_ids),
            non_russian_name=non_russian_name,
        ),
    )

    if not awardee.name and name:
        awardee.name = name
    if not awardee.city and city:
        awardee.city = city
    if not awardee.non_russian_name and non_russian_name:
        awardee.non_russian_name = non_russian_name
    awardee.external_ids = merge_external_ids(awardee.external_ids, external_ids)

    awardee.add_place(place, game)
    awardees[id] = awardee
    return awardees

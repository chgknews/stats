"""Tournament languages: normalization and Russian markdown phrasing.

Codes are ISO 639-1, matching the ``id``/``value`` fields of
https://api.rating.chgk.net/languages. That list covers only a part of the
countries tracked here, so languages the API does not know (Spanish, Turkish,
Hebrew and so on) are kept in the same table and entered by hand in Sheets.
"""
from typing import Dict, Iterable, List, NamedTuple, Optional

DEFAULT_LANGUAGE = "ru"


class Language(NamedTuple):
    """Russian forms needed to name a language in generated markdown."""
    name: str            # nominative, as shown in Sheets and the API
    prepositional: str   # used in «на <prepositional> языке»
    phrase: str = ""     # full override for languages that break that template
    aliases: tuple = ()  # other spellings accepted from Sheets


# Ordered roughly as in the API list, then the languages our countries need.
LANGUAGES: Dict[str, Language] = {
    "az": Language("Азербайджанский", "азербайджанском"),
    "be": Language("Белорусский", "беларусском", aliases=("Беларусский",)),
    "en": Language("Английский", "английском"),
    "ka": Language("Грузинский", "грузинском"),
    "hy": Language("Армянский", "армянском"),
    "kk": Language("Казахский", "казахском"),
    "ro": Language("Румынский", "румынском"),
    "ru": Language("Русский", "русском"),
    "sr": Language("Сербский", "сербском"),
    "uk": Language("Украинский", "украинском"),
    "uz": Language("Узбекский", "узбекском"),
    "cs": Language("Чешский", "чешском"),
    "de": Language("Немецкий", "немецком"),
    "fr": Language("Французский", "французском"),
    "he": Language("Иврит", "ивритском", phrase="на иврите"),
    "pl": Language("Польский", "польском"),
}

_BY_NAME: Dict[str, str] = {}
for _code, _language in LANGUAGES.items():
    _BY_NAME[_language.name.lower()] = _code
    for _alias in _language.aliases:
        _BY_NAME[_alias.lower()] = _code


def normalize_language(value: object) -> str:
    """Return an ISO code for a code or a Russian name; "" when unknown."""
    text = "" if value is None else str(value).strip()
    if not text:
        return ""
    lowered = text.lower()
    if lowered in LANGUAGES:
        return lowered
    return _BY_NAME.get(lowered, "")


def normalize_languages(values: Optional[Iterable[object]]) -> List[str]:
    """Normalize a sequence of languages, dropping unknowns and duplicates."""
    if not values or isinstance(values, (str, bytes)):
        values = [values] if values else []
    codes: List[str] = []
    for value in values:
        code = normalize_language(value)
        if not code:
            text = str(value).strip()
            if text:
                print(f"Warning: unknown language {text!r}, skipped")
            continue
        if code not in codes:
            codes.append(code)
    return codes


def language_name(code: str) -> str:
    """Nominative Russian name, used when writing the sheet."""
    language = LANGUAGES.get(code)
    return language.name if language else code


def has_non_russian(codes: Iterable[str]) -> bool:
    return any(code != DEFAULT_LANGUAGE for code in codes)


def language_phrase(codes: Iterable[str]) -> str:
    """Build «на русском и испанском языках» / «на иврите» for markdown.

    Returns "" for an empty list or Russian alone, since a Russian-language
    tournament needs no remark.
    """
    codes = [code for code in codes if code in LANGUAGES]
    if not codes or not has_non_russian(codes):
        return ""

    adjectives = [LANGUAGES[c].prepositional for c in codes if not LANGUAGES[c].phrase]
    overrides = [LANGUAGES[c].phrase for c in codes if LANGUAGES[c].phrase]

    parts: List[str] = []
    if adjectives:
        noun = "языке" if len(adjectives) == 1 else "языках"
        parts.append(f"на {_join_russian(adjectives)} {noun}")
    parts.extend(overrides)
    return _join_russian(parts)


def _join_russian(parts: List[str]) -> str:
    if len(parts) == 1:
        return parts[0]
    return ", ".join(parts[:-1]) + " и " + parts[-1]

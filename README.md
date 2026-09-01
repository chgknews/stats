# stats
Проект по сбору статистики интеллектуальных игр, в первую очередь результатов чемпионатов разных стран.

📖 **Подробная документация:** [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — схема таблицы, все CLI-флаги, Hugo, CI, миграции и разовые операции.

## Быстрый старт

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Ключ сервисного аккаунта Google (для работы с таблицей)
cp /path/to/service-account.json credentials.json
# Разрешите доступ к таблице для email сервисного аккаунта (Editor)
```

Slug страны — латиница, как имя вкладки в [Google Sheets](https://docs.google.com/spreadsheets/d/1HKNi0YXYkvhcV76DsW25hzvvbJ190cLWTWcbYuO4yC4/edit) (`poland`, `armenia`, `testing2`). Кириллическое название берётся из `counting/country_registry.py`.

## Типичные сценарии

### 1. Пересчитать статистику после правок в таблице

Редактор меняет строки во вкладке страны (Podium / Rosters / Tournaments), затем:

```bash
# Безопасно: только локальные файлы, таблица не перезаписывается
python scripts/count_champions.py -ug poland --read-only-sheets

# Полный цикл: пересчёт + нормализация и перезапись вкладки v2
python scripts/count_champions.py -ug poland
```

**`-ug` / `--update_from_google_sheets`** — slug страны.

Результат: `content/info/countries/{country}.md` (для `russia_01_19`, `russia_igra_tv`, `russia_kvrm` — `content/info/countries/russia/{country}.md`), `data/countries.json` (весь справочник вкладок).

### 2. Добавить завершившийся чемпионат

```bash
python scripts/count_champions.py -cn poland -at 11708
```

**`-cn`** — slug, **`-at`** — id турнира на [rating.chgk.info](https://rating.chgk.info). Другая игра: `-g brain`.

### 3. Добавить будущий чемпионат и потом заполнить его

```bash
# Пустая строка (дата и город)
python scripts/count_champions.py -cn poland -et "25 февраля 2026 года" -p "Варшаве"

# Ссылки
python scripts/count_champions.py -cn poland -u announce -ui "https://..."
python scripts/count_champions.py -cn poland -u tg -ui "https://t.me/..."

# После турнира — подтянуть результаты с rating.chgk.info
python scripts/count_champions.py -cn poland -u ts -ui 11708
```

**`-u`** — поле (`ts`, `place`, `announce`, `tg`, `fb`, `vk`, `site`, `recap`, `letopis`), **`-ui`** — значение.

### 4. Локальный предпросмотр в Hugo

```bash
python scripts/count_champions.py -ug poland --read-only-sheets

git submodule update --init --recursive   # один раз
hugo server --baseURL http://localhost:1313/
# http://localhost:1313/countries/poland/
```

### 5. Первая загрузка страны с rating.chgk.info

Файл `.txt` со списком id турниров (от новых к старым), например [tests/testing2.txt](tests/testing2.txt):

```bash
python scripts/count_champions.py -f tests/testing2.txt -cn testing2 --read-only-sheets   # проверка без записи в Sheets
python scripts/count_champions.py -f tests/armenia.txt -cn armenia                          # создаёт/перезаписывает вкладку
```

**`-f`** — файл с id, **`-cn`** — slug, **`-n`** — если история неполная (номер последнего учитываемого чемпионата).

Новая страна: добавьте slug в `country_registry.py`, затем загрузите данные. Подробнее — [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md#common-workflows).

### 6. Пересборка markdown из JSON (без сети)

Если изменился код генератора (`stats_generator.py`, `constants.py`) и нужно заново собрать страницу из уже сохранённого снимка — без Google Sheets и без API:

```bash
python scripts/count_champions.py --from-json testing2 -cn testing2
```

## CI

GitHub Actions: ручные workflow для пересборки из таблицы и добавления страны. Настройка секретов — [.github/CI_SETUP.md](.github/CI_SETUP.md).

Разовые операции (миграция схемы таблицы, смена формата дат, cross-country stats) — только в [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

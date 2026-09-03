#!/usr/bin/env python3
"""
Генерирует файл .md из Google Docs, используя официальный API.

Таблица в документе должна иметь три колонки:
  - Дата
  - Событие
  - Подробности
Все inline‑форматирования (жирный, ссылки, переносы) сохраняются.
"""

import os
import sys
import re
from pathlib import Path
import json

from googleapiclient.discovery import build
from google.oauth2 import service_account

REPO_ROOT = Path(__file__).resolve().parent.parent

# ----------------------------------------------------------------------
# Конфигурация
# ----------------------------------------------------------------------
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
SERVICE_ACCOUNT_FILE = str(REPO_ROOT / 'credentials.json')
DOCUMENT_ID = '1yY7-VlyTSo_EhecwBUIdTx77akdrYpsCOW_0tod0JQI'   # ID из ссылки
YEAR = 2026
OUTPUT_FILE = str(REPO_ROOT / 'content' / 'info' / 'chronicle' / f'{YEAR}.md')

# ----------------------------------------------------------------------
# Конвертация элементов Docs в HTML (сохраняем форматирование)
# ----------------------------------------------------------------------
def get_text_with_formatting(element, content):
    """Рекурсивно обходит структурные элементы и возвращает HTML‑строку с тегами <b>, <a>."""
    parts = []
    if 'paragraph' in element:
        para = element['paragraph']
        for elem in para.get('elements', []):
            text_run = elem.get('textRun')
            if not text_run:
                continue
            text = text_run.get('content', '')
            style = text_run.get('textStyle', {})
            # Обработка ссылок
            link = style.get('link')
            if link and link.get('url'):
                # Ссылка применяется ко всему тексту в этом run
                # Удаляем возможный лишний пробел в конце
                text = text.strip()
                if text:
                    parts.append(f'<a href="{link["url"]}">{text}</a>')
            else:
                # Жирный шрифт
                if style.get('bold'):
                    parts.append(f'<b>{text}</b>')
                else:
                    parts.append(text)
        # Добавляем перенос строки после абзаца (если не последний)
        # Но для ячеек таблицы мы будем собирать всё в одну строку с <br> для переносов
    elif 'table' in element:
        # Рекурсивно обходим таблицу (но мы её обрабатываем отдельно)
        pass
    return ''.join(parts)

def extract_table_data(doc_content):
    """Извлекает таблицу из документа и возвращает список строк (дата, событие, подробности)."""
    content = doc_content.get('body', {}).get('content', [])
    table_rows = []

    # Ищем первую таблицу (или ту, которая содержит нужные заголовки)
    target_table = None
    for elem in content:
        if 'table' in elem:
            table = elem['table']
            # Проверим заголовки первой строки
            rows = table.get('tableRows', [])
            if not rows:
                continue
            header_row = rows[0]
            header_cells = header_row.get('tableCells', [])
            # Собираем текст из каждой ячейки заголовка
            header_texts = []
            for cell in header_cells:
                cell_text = get_text_from_cell(cell, content)
                header_texts.append(cell_text.strip().lower())
            # Проверяем наличие ключевых слов
            keywords = ['дата', 'date', 'событие', 'event', 'подробности', 'details']
            if any(k in ' '.join(header_texts) for k in keywords):
                target_table = table
                break

    if not target_table:
        # Если не нашли по ключевым словам, берём первую таблицу
        for elem in content:
            if 'table' in elem:
                target_table = elem['table']
                break

    if not target_table:
        raise ValueError("В документе не найдено ни одной таблицы.")

    # Обрабатываем строки (пропускаем заголовок)
    rows = target_table.get('tableRows', [])
    if len(rows) < 2:
        raise ValueError("Таблица не содержит строк с данными.")

    for row in rows[1:]:
        cells = row.get('tableCells', [])
        if len(cells) < 3:
            # Если ячеек меньше, дополняем пустыми
            cells += [None] * (3 - len(cells))
        # Извлекаем HTML‑содержимое каждой ячейки
        date_html = get_html_from_cell(cells[0], content) if cells[0] else ''
        event_html = get_html_from_cell(cells[1], content) if cells[1] else ''
        details_html = get_html_from_cell(cells[2], content) if cells[2] else ''

        # Очищаем от лишних пробелов
        date_html = date_html.strip()
        event_html = event_html.strip()
        details_html = details_html.strip()

        if not date_html:
            continue   # пропускаем строки без даты

        table_rows.append((date_html, event_html, details_html))

    return table_rows

def get_text_from_cell(cell, content):
    """Возвращает простой текст из ячейки (для заголовка)."""
    texts = []
    for elem in cell.get('content', []):
        if 'paragraph' in elem:
            for run in elem['paragraph'].get('elements', []):
                if 'textRun' in run:
                    texts.append(run['textRun'].get('content', ''))
    return ''.join(texts).strip()

def get_html_from_cell(cell, content):
    """Возвращает HTML‑строку с сохранением жирного, ссылок и переносов."""
    html_parts = []
    for elem in cell.get('content', []):
        if 'paragraph' in elem:
            para = elem['paragraph']
            para_html = []
            for run_elem in para.get('elements', []):
                text_run = run_elem.get('textRun')
                if not text_run:
                    continue
                text = text_run.get('content', '')
                # Обрабатываем форматирование
                style = text_run.get('textStyle', {})
                # Ссылка
                link = style.get('link')
                if link and link.get('url'):
                    text = text.strip()
                    if text:
                        para_html.append(f'<a href="{link["url"]}">{text}</a>')
                else:
                    if style.get('bold'):
                        para_html.append(f'<b>{text}</b>')
                    elif style.get('italic'):
                        para_html.append(f'<i>{text}</i>')
                    else:
                        para_html.append(text)
            # Соединяем содержимое абзаца и добавляем <br> если есть несколько абзацев
            if para_html:
                # Убираем лишние пробелы в конце
                combined = ''.join(para_html).strip()
                if combined:
                    html_parts.append(combined)
    # Разделяем абзацы тегом <br> (так как в ячейке может быть несколько абзацев)
    return '<br><br>'.join(html_parts)

# ----------------------------------------------------------------------
# Генерация HTML‑таблицы (аналогично предыдущему шаблону)
# ----------------------------------------------------------------------
HTML_TEMPLATE = '''<div class="table-container" id="chronicle-expand">
  <div class="chronicle-toolbar">
    <button type="button" class="bulk-btn" data-expand-all>Показать всё</button>
    <button type="button" class="bulk-btn" data-collapse-all>Скрыть всё</button>
  </div>
  <table aria-label="Expandable details table">
    <colgroup>
      <col class="chronicle-col-date">
      <col class="chronicle-col-event">
    </colgroup>
    <thead>
       <tr>
          <th scope="col">Дата</th>
          <th scope="col">Событие</th>
       </tr>
    </thead>
    <tbody>
      {table_rows}
    </tbody>
  </table>
  <p class="chronicle-hint">Чтобы узнать о турнире больше, нажмите на стрелку справа у нужной строки. Кнопки «Показать всё» и «Скрыть всё» открывают или закрывают все блоки сразу.</p>
</div>

{{< chronicle-expand >}}'''

# ----------------------------------------------------------------------
# 3. Helper functions
# ----------------------------------------------------------------------

def extract_table_rows(html_content):
    """Parse the Google Doc HTML and return a list of (date, event, details) tuples.
       Each value is a string of HTML (inline markup preserved)."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the first table (or search for a table that has headers matching Date/Event/Details)
    tables = soup.find_all('table')
    if not tables:
        raise ValueError("No table found in the document.")

    # Try to identify the correct table by looking for header keywords
    target_table = None
    for table in tables:
        first_row = table.find('tr')
        if first_row:
            cells = first_row.find_all(['td', 'th'])
            cell_texts = [cell.get_text(strip=True).lower() for cell in cells]
            # Look for 'date', 'event', 'details' (or Russian equivalents)
            keywords = ['дата', 'date', 'событие', 'event', 'подробности', 'details']
            if any(key in ' '.join(cell_texts) for key in keywords):
                target_table = table
                break

    if not target_table:
        # If no table matches, use the first one
        target_table = tables[0]

    rows = target_table.find_all('tr')
    if len(rows) < 2:
        raise ValueError("Table has no data rows.")

    # Assume first row is header – skip it
    data_rows = rows[1:]

    extracted = []
    for row in data_rows:
        cells = row.find_all(['td', 'th'])
        if len(cells) < 3:
            # If fewer cells, pad with empty strings
            cells += [None] * (3 - len(cells))
        # Extract inner HTML of each cell, preserving inline tags
        date_cell = cells[0] if cells[0] else None
        event_cell = cells[1] if len(cells) > 1 else None
        details_cell = cells[2] if len(cells) > 2 else None

        date_html = date_cell.decode_contents() if date_cell else ''
        event_html = event_cell.decode_contents() if event_cell else ''
        details_html = details_cell.decode_contents() if details_cell else ''

        # Clean up: if the content is just whitespace, treat as empty
        date_html = date_html.strip()
        event_html = event_html.strip()
        details_html = details_html.strip()

        # If date is empty, skip the row
        if not date_html:
            continue

        extracted.append((date_html, event_html, details_html))

    return extracted

def generate_table_rows(rows):
    """Генерирует HTML для <tbody>."""
    row_parts = []
    for idx, (date_html, event_html, details_html) in enumerate(rows, start=1):
        details_id = f"details{idx}"
        summary_id = f"summary{idx}"
        arrow_id = f"arrow{idx}"
        row = f"""<tr>
          <td class="date-cell">{date_html}</td>
          <td>
            <div class="text-wrapper">
              <div class="summary-line">
                <span class="summary-text" id="{summary_id}">{event_html}</span>
                <button type="button" class="toggle-btn" data-target="{details_id}" aria-expanded="false" aria-controls="{details_id}" aria-label="Показать">
                  <span class="arrow-icon" id="{arrow_id}">▶</span>
                </button>
              </div>
              <div class="extra-details" id="{details_id}">
                {details_html}
              </div>
            </div>
          </td>
        </tr>"""
        row_parts.append(row)
    return '\n'.join(row_parts)

def write_markdown(year, output_path, table_rows_html):
    frontmatter = f"""---
title: {year}
weight: 1
bookToC: false
---

# {year}

"""
    full_html = HTML_TEMPLATE.replace('{table_rows}', table_rows_html)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter + full_html + "\n")

# ----------------------------------------------------------------------
# Основная функция
# ----------------------------------------------------------------------
def main():
    # Авторизация
    creds = None
    if os.path.exists(SERVICE_ACCOUNT_FILE):
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    else:
        sys.exit(f"Файл {SERVICE_ACCOUNT_FILE} не найден.")

    service = build('docs', 'v1', credentials=creds)

    # Получение документа
    try:
        doc = service.documents().get(documentId=DOCUMENT_ID).execute()
    except Exception as e:
        sys.exit(f"Ошибка при получении документа: {e}")

    # Извлечение данных из таблицы
    try:
        rows = extract_table_data(doc)
    except Exception as e:
        sys.exit(f"Ошибка при разборе таблицы: {e}")

    if not rows:
        sys.exit("Таблица не содержит данных.")

    print(f"Найдено {len(rows)} строк.")

    # Генерация HTML‑строк
    table_rows_html = generate_table_rows(rows)

    # Запись в файл
    write_markdown(YEAR, OUTPUT_FILE, table_rows_html)
    print(f"Файл {OUTPUT_FILE} успешно создан.")

if __name__ == '__main__':
    main()
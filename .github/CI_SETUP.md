# CI / Google Sheets setup

## GitHub secret: `GOOGLE_SHEETS_CREDENTIALS`

1. Create a Google Cloud service account with **Google Sheets API** and **Google Drive API** enabled.
2. Download the JSON key file.
3. In GitHub: **Settings → Secrets and variables → Actions → New repository secret**
4. Name: `GOOGLE_SHEETS_CREDENTIALS`
5. Value: paste the **entire JSON** file contents.

## Share the spreadsheet

Share the stats spreadsheet with the service account email (Editor access):

`your-service-account@project.iam.gserviceaccount.com`

Spreadsheet ID is configured in [`constants.py`](../constants.py) as `GOOGLE_SHEETS_SPREADSHEET_ID`.

## Workflows

Both workflows are **manual** (`workflow_dispatch`). They write `credentials.json` from the secret, run Python, then commit and push generated files.

| Workflow | Purpose |
|----------|---------|
| [`rebuild-from-sheets-manual.yaml`](workflows/rebuild-from-sheets-manual.yaml) | Rebuild one or more countries from Google Sheets (`-ug`). Default: `--read-only-sheets`. Optional writeback to Sheets. |
| [`add-country-from-file-manual.yaml`](workflows/add-country-from-file-manual.yaml) | Bulk load from a tournament ID file (`-f`) for a new country. Default: writes to Sheets. |

### Rebuild from Sheets

Inputs:

- **countries** — comma-separated slugs, e.g. `armenia,montenegro`
- **writeback** — if `true`, omits `--read-only-sheets` and rewrites the worksheet tab(s)
- **commit_message** — optional git commit message

Commits: `content/info/countries/`, `content/tournaments/countries/`, `data/`, `.github/sheets_state.json` (if changed).

### Add country from file

Inputs:

- **slug** — country slug / worksheet name, e.g. `armenia`
- **ids_file** — path in repo, e.g. `tests/armenia.txt`
- **game** — default `chgk`
- **number** — optional `-n` (last championship number)
- **writeback** — default `true`; set `false` for local-files-only test run
- **commit_message** — optional

## Local testing (mirrors CI)

```bash
pip install -r requirements.txt
cp /path/to/key.json credentials.json

# Same as CI rebuild (read-only)
python scripts/count_champions.py -ug testing2 --read-only-sheets

# Same as add-country workflow, without Sheets write
python scripts/count_champions.py -f tests/testing2.txt -cn testing2 --read-only-sheets
```

Use the `testing` or `testing2` worksheet tab — not production country tabs — when experimenting with writeback.

## Optional: Apps Script webhook

See [`scripts/google_apps_script.gs`](../scripts/google_apps_script.gs). Install in the spreadsheet editor:

**Extensions → Apps Script**, paste the script, set `GITHUB_TOKEN` and `GITHUB_REPO` in Script properties, create an `onEdit` trigger (debounced).

This can trigger a custom `repository_dispatch` workflow if you add one; the current repo uses manual dispatch only.

## Optional: change detection helper

`sheets_watch.py` compares worksheet content hashes against `.github/sheets_state.json` and prints `CHANGED:poland,testing` or `UNCHANGED`. It is **not** wired into the current GitHub Actions workflows; useful for local scripts or a future cron job.
# Wide World Importers sample dataset

The Lakehouse Lab uses the **Wide World Importers (WWI)** sample dataset. The full dataset ships as a **1.87 GB zip** (`wwi-sample-dataset.zip`), which is too large to include in a git repo.

The tutorial itself downloads it from the public Microsoft URL below, either:

- via the browser (step "Data ingestion into the lakehouse - Method#2 - Data Pipeline"), or
- via a Data Factory pipeline `Copy data` activity pointed at the same URL.

## Fetch it locally

**PowerShell**

```powershell
./fetch-wwi-data.ps1
```

**Bash**

```bash
./fetch-wwi-data.sh
```

Either script downloads to `wwi-sample-dataset.zip` in this folder. Both are gitignored (see `.gitignore` at repo root).

## Source URL

<https://assetsprod.microsoft.com/en-us/wwi-sample-dataset.zip>

## What else is in this folder

- `dimension_customer.csv` (65 KB) — sample dimension file used in Module 2 "OneLake File Explorer upload" step. Small enough to commit.
- The zip is fetched on demand; not committed.

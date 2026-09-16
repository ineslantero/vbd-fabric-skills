# vbd-lab-foundation references

Ground-truth lab tutorials from the SharePoint IP release Foundation Discovery Labs, converted from `.docx` to markdown with all reference links preserved.

**Source**: [`Data and AI/Fabric/1 - Upskilling/1 - Foundation/Upskilling on MS Fabric Foundation/Assets/02 - Discovery Labs`](https://microsoft.sharepoint.com/teams/ASDIPRelease/IP%20Release/Data%20and%20AI/Fabric/1%20-%20Upskilling/1%20-%20Foundation)

## Folders

| Folder | SharePoint source | Original file |
|---|---|---|
| `lakehouse/` | `01 - Lakehouse Lab` | `Lakehouse Tutorial.docx` |
| `warehouse/` | `02 - Data Warehouse Lab` | `Fabric Data Warehouse Tutorial.docx` |
| `rti/` | `03 - Real-Time Intelligence Lab` | `Real-time Intelligence Tutorial.docx` |
| `datascience/` | `04 - Data Science Lab` | `Data Science Tutorial.docx` |

Each folder contains a **single** `<lab>-tutorial.md` — the SharePoint Word tutorial converted to markdown and freshness-verified. Every Microsoft Learn URL cited is inline in the markdown (no separate index file). Freshness re-verifies each URL at lab-generation time.

## How `/vbd-lab-foundation` uses these

- **Authoritative structure.** Objectives, step order, checkpoints, code snippets, and Learn citations come from here.
- **Not rendered verbatim.** The skill rewrites each step against the customer's data + industry angle from `workshop.yaml`.
- **Freshness gate.** Before publishing, every URL in `sources.yaml` is re-verified against current Microsoft Learn; any 404 / redirect / deprecation is flagged.

## Refreshing the references

When the SharePoint IP release publishes a new tutorial revision:

1. Download the updated `.docx`.
2. Re-convert to markdown (`scripts/clean_tutorials.py`).
3. Replace `<lab>-tutorial.md`.
4. Re-run the freshness audit (see `.vbd/freshness-audit-<date>.md`).
5. Commit with a note pointing at the new SharePoint revision timestamp.

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

Each folder contains:

- `<lab>-tutorial.md` — the Word tutorial converted to markdown. Preserves headings, step numbering, code blocks, and every link to Microsoft Learn or sample data.
- `sources.yaml` — machine-readable list of every URL cited in the tutorial (Learn docs, GitHub samples, Fabric portal paths), used by `components/freshness` to re-verify each citation at generation time.

## How `/vbd-lab-foundation` uses these

- **Authoritative structure.** Objectives, step order, checkpoints, code snippets, and Learn citations come from here.
- **Not rendered verbatim.** The skill rewrites each step against the customer's data + industry angle from `workshop.yaml`.
- **Freshness gate.** Before publishing, every URL in `sources.yaml` is re-verified against current Microsoft Learn; any 404 / redirect / deprecation is flagged.

## Refreshing the references

When the SharePoint IP release publishes a new tutorial revision:

1. Download the updated `.docx`.
2. Re-convert to markdown (pandoc or the Scout `docx` skill).
3. Replace `<lab>-tutorial.md`.
4. Regenerate `sources.yaml` (list every URL in the new markdown).
5. Commit with a note pointing at the new SharePoint revision timestamp.

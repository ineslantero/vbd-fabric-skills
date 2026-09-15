# vbd-data references

Ground-truth CSVs from the SharePoint IP release Foundation Discovery Labs.

**Source**: [`Data and AI/Fabric/1 - Upskilling/1 - Foundation/Upskilling on MS Fabric Foundation/Assets/02 - Discovery Labs`](https://microsoft.sharepoint.com/teams/ASDIPRelease/IP%20Release/Data%20and%20AI/Fabric/1%20-%20Upskilling/1%20-%20Foundation)

## Folders

| Folder | SharePoint source | Original dataset |
|---|---|---|
| `lakehouse/` | `01 - Lakehouse Lab/Data` | Wide World Importers (retail) — customers, products, orders, order_lines |
| `warehouse/` | `02 - Data Warehouse Lab/Data` | WWI aggregates + dim tables for T-SQL loads |
| `rti/` | `03 - Real-Time Intelligence Lab/Data` | Streaming events sample (IoT/telemetry-shaped) |
| `datascience/` | `04 - Data Science Lab/Data` | NY Taxi trips (regression target: fare / tip) |

## How `/vbd-data` uses these

- **Read for shape only.** File count, column count, fact/dim split, row count magnitude.
- **Never copy verbatim.** Always regenerate against the customer's industry from `workshop.yaml`.
- **Map 1:1.** One output CSV per reference CSV, same role (fact / dim / lookup).

## Refreshing the references

If SharePoint updates the source datasets, re-download and replace the contents of each subfolder. Do **not** hand-edit — this is a mirror, not a fork.

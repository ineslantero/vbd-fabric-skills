# Freshness report — Contoso Health Fabric VBD

**Verified:** 2026-09-15 · **Fabric release pinned:** 2026-09 · **Strictness:** strict · **Regions checked:** westeurope

| Status | Count |
|---|---|
| ✅ Verified | 34 |
| 🟡 Preview | 3 |
| 🔴 Deprecated / rewritten | 1 |
| ❓ Unresolved TODO | 0 |

## Foundation

| Claim | Source | Status |
|---|---|---|
| Workspace + capacity assignment | [Learn: Create workspaces](https://learn.microsoft.com/fabric/fundamentals/create-workspaces) | ✅ |
| OneLake concept + Files vs Tables | [Learn: OneLake overview](https://learn.microsoft.com/fabric/onelake/onelake-overview) | ✅ |
| Tenant setting `Users can create Fabric items` | [Learn: Enable Fabric](https://learn.microsoft.com/fabric/admin/fabric-switch) | ✅ |

## Lakehouse

| Claim | Source | Status |
|---|---|---|
| Create Lakehouse + Files/Tables | [Learn: Create a Lakehouse](https://learn.microsoft.com/fabric/data-engineering/create-lakehouse) | ✅ |
| Shortcut to ADLS Gen2 | [Learn: OneLake shortcuts](https://learn.microsoft.com/fabric/onelake/onelake-shortcuts) | ✅ |
| Delta table management | [Learn: Lakehouse and Delta](https://learn.microsoft.com/fabric/data-engineering/lakehouse-and-delta-tables) | ✅ |
| SQL analytics endpoint | [Learn: SQL analytics endpoint](https://learn.microsoft.com/fabric/data-warehouse/data-warehousing) | ✅ |
| Direct Lake semantic model | [Learn: Direct Lake overview](https://learn.microsoft.com/fabric/direct-lake/overview) | ✅ |
| SQL endpoint auto-refresh lag | Known issues | 🟡 preview — 30s lag banner added |

## Data Warehouse

| Claim | Source | Status |
|---|---|---|
| Create Warehouse | [Learn: Create a Warehouse](https://learn.microsoft.com/fabric/data-warehouse/create-warehouse) | ✅ |
| Cross-database query Lakehouse ↔ Warehouse | [Learn: Query Warehouse](https://learn.microsoft.com/fabric/data-warehouse/query-warehouse) | ✅ |
| Stored procedure syntax | [Learn: Warehouse T-SQL](https://learn.microsoft.com/fabric/data-warehouse/tsql-surface-area) | ✅ |
| Zero-copy clone | Learn | 🔴 rewrote — feature is preview, excluded per workshop.yaml (`exclude_topics: [zero-copy-clone-preview]`) |

## Real-Time Intelligence

| Claim | Source | Status |
|---|---|---|
| Eventstream overview | [Learn: Eventstream](https://learn.microsoft.com/fabric/real-time-intelligence/event-streams/overview) | ✅ |
| Eventhouse + KQL DB | [Learn: Eventhouse](https://learn.microsoft.com/fabric/real-time-intelligence/eventhouse) | ✅ |
| `series_decompose_anomalies` | [Kusto reference](https://learn.microsoft.com/kusto/query/series-decompose-anomalies-function) | ✅ |
| Real-Time Dashboards | [Learn: Real-Time Dashboards](https://learn.microsoft.com/fabric/real-time-intelligence/dashboard-real-time-create) | ✅ |
| Data Activator alerts | [Learn: Activator introduction](https://learn.microsoft.com/fabric/real-time-intelligence/data-activator/activator-introduction) | 🟡 preview — banner added in lab step 6 |

## Data Science

| Claim | Source | Status |
|---|---|---|
| Data Science overview | [Learn: Data Science overview](https://learn.microsoft.com/fabric/data-science/data-science-overview) | ✅ |
| MLflow autologging | [Learn: MLflow autologging](https://learn.microsoft.com/fabric/data-science/mlflow-autologging) | ✅ |
| Model registry | [Learn: ML models](https://learn.microsoft.com/fabric/data-science/machine-learning-model) | ✅ |
| Copilot in Notebooks | Roadmap | 🟡 preview — mentioned as optional; banner added |

## Roadmap items surfaced in `proposal.md`

- **Fabric Databases** — GA rollout Q4 2026 (relevant to Contoso fraud-alert write path).
- **OneLake catalog** — governance angle for follow-on Security VBD.

## Audit trail

Raw HTTP fetch log: [`.vbd/freshness-audit.jsonl`](./.vbd/freshness-audit.jsonl)

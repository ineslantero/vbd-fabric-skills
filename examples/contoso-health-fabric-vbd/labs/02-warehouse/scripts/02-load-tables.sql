-- 02-load-tables.sql — pull from the Lakehouse gold via cross-database query.

INSERT INTO analytics.dim_provider (provider_id, provider_name, speciality, state)
SELECT provider_id, provider_name, speciality, state
FROM lh_claims_bronze.dbo.silver_providers;

INSERT INTO analytics.fact_provider_month_summary
SELECT provider_id, month, total_paid, claim_count, avg_claim
FROM lh_claims_bronze.dbo.gold_claims_by_provider_month;

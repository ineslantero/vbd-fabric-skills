-- 03-create-aggregate-proc.sql — refreshes the Warehouse-owned aggregate from the Lakehouse gold.

CREATE OR ALTER PROCEDURE dbo.usp_refresh_provider_summary
AS
BEGIN
    TRUNCATE TABLE analytics.fact_provider_month_summary;

    INSERT INTO analytics.fact_provider_month_summary
    SELECT provider_id, month, total_paid, claim_count, avg_claim
    FROM lh_claims_bronze.dbo.gold_claims_by_provider_month;
END;
GO

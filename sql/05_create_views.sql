USE india_aqi_db;

-- Drop views if they already exist
DROP VIEW IF EXISTS vw_state_summary;
DROP VIEW IF EXISTS vw_pollutant_trends;

-- 1. Create a view for state-level aggregations
CREATE VIEW vw_state_summary AS
SELECT 
    state,
    ROUND(AVG(aqi_value), 2) AS avg_aqi,
    MAX(aqi_value) AS max_aqi,
    MIN(aqi_value) AS min_aqi,
    COUNT(*) AS total_records
FROM aqi_cleaned_data
GROUP BY state;

-- 2. Create a view for pollutant analysis
CREATE VIEW vw_pollutant_trends AS
SELECT 
    prominent_pollutants,
    air_quality_status,
    ROUND(AVG(aqi_value), 2) AS avg_aqi,
    COUNT(*) as occurrence_count
FROM aqi_cleaned_data
GROUP BY prominent_pollutants, air_quality_status;



SELECT COUNT(*) AS total_rows FROM aqi_cleaned_data;


-- 1. View state-level summary data
SELECT * FROM vw_state_summary;

-- 2. View pollutant trends data
SELECT * FROM vw_pollutant_trends;
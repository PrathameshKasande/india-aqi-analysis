USE india_aqi_db;
TRUNCATE TABLE aqi_cleaned_data;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/cleaned_aqi.csv'
INTO TABLE aqi_cleaned_data
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(date, state, area, number_of_monitoring_stations, prominent_pollutants, aqi_value, air_quality_status, unit);


SELECT COUNT(*) AS total_rows FROM aqi_cleaned_data;


USE india_aqi_db;

-- 1. Check total row count (should be 235,785)
SELECT COUNT(*) AS total_rows FROM aqi_cleaned_data;

-- 2. Check for any NULL values in critical columns
SELECT 
    SUM(date IS NULL) AS missing_dates,
    SUM(state IS NULL) AS missing_states,
    SUM(aqi_value IS NULL) AS missing_aqi
FROM aqi_cleaned_data;

-- 3. Verify date range of the dataset
SELECT 
    MIN(date) AS earliest_date, 
    MAX(date) AS latest_date 
FROM aqi_cleaned_data;

-- 4. Check distinct air quality categories
SELECT DISTINCT air_quality_status, COUNT(*) as count
FROM aqi_cleaned_data
GROUP BY air_quality_status
ORDER BY count DESC;



USE india_aqi_db;

-- 1. Top 10 most polluted areas based on average AQI value
SELECT area, state, ROUND(AVG(aqi_value), 2) AS avg_aqi
FROM aqi_cleaned_data
GROUP BY area, state
ORDER BY avg_aqi DESC
LIMIT 10;

-- 2. State-wise average AQI ranking
SELECT state, ROUND(AVG(aqi_value), 2) AS avg_state_aqi
FROM aqi_cleaned_data
GROUP BY state
ORDER BY avg_state_aqi DESC;

-- 3. Most frequent prominent pollutants across the country
SELECT prominent_pollutants, COUNT(*) as frequency
FROM aqi_cleaned_data
GROUP BY prominent_pollutants
ORDER BY frequency DESC;

SELECT COUNT(*) AS total_rows FROM aqi_cleaned_data;

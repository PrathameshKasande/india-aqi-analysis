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
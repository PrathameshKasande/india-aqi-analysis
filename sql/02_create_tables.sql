USE india_aqi_db;

-- Drop table if it already exists to ensure a clean setup
DROP TABLE IF EXISTS aqi_cleaned_data;

-- Create the main AQI data table
CREATE TABLE aqi_cleaned_data (
    date DATE,
    state VARCHAR(100),
    area VARCHAR(150),
    number_of_monitoring_stations INT,
    prominent_pollutants VARCHAR(100),
    aqi_value FLOAT,
    air_quality_status VARCHAR(50),
    unit TEXT
);
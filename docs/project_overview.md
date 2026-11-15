# 🌍 Project Overview: India Air Quality Index (AQI) Analysis

## 🎯 Objective
To analyze historical air quality trends, pollutant distributions, and environmental monitoring metrics across India using exploratory data analysis, relational database management, and business intelligence dashboards.

## 📁 Dataset Profile
* **Source File:** `aqi.csv`
* **Total Records:** 235,785 rows
* **Geographic Coverage:** Pan-India states, union territories, and local monitoring areas.
* **Key Features:** 
  * `date` — Timestamp of environmental recording
  * `state` — Indian state or union territory
  * `area` — Specific city or monitoring zone
  * `number_of_monitoring_stations` — Active sensor infrastructure count
  * `prominent_pollutants` — Dominant atmospheric pollutants (e.g., PM2.5, PM10, NO₂, CO)
  * `aqi_value` — Numerical Air Quality Index score
  * `air_quality_status` — Health classification category (Satisfactory, Moderate, Poor, Very Poor, Severe)

---

## 🏗️ End-to-End Pipeline & Architecture

This project follows an enterprise-grade data analytics and engineering lifecycle:

```text
[ 1. Raw Data Ingestion ] ──► [ 2. Python Preprocessing ] ──► [ 3. MySQL Database ] ──► [ 4. Power BI Dashboard ]
       (Excel / CSV)             (Pandas & NumPy)               (Relational Backend)          (4-Page Executive View)
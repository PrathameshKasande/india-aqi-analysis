# 🔍 Data Quality & Hygiene Report

## 📋 Overview
* **Dataset Size:** 235,785 rows, 9 columns.
* **Missing Value Check:** 0 missing values detected in critical analytical columns (`date`, `state`, `area`, `aqi_value`, `air_quality_status`). The `note` column contains 235,785 null values and was excluded from active analysis.

---

## 📐 Range & Outlier Validation
* **AQI Value Range:** Verified between **3** (Minimum) and **500** (Maximum), aligning with the standard Indian Central Pollution Control Board (CPCB) index scale.
* **Mean AQI:** 111.13 (Standard Deviation: ~71.45).

---

## 🛠️ Data Hygiene & Validation Pipeline
1. **Schema & Null Handling:** Confirmed absolute integrity across core analytical dimensions; excluded redundant null fields (`note`) to maintain data model efficiency.
2. **Standardization:** Normalized state, area, and pollutant text strings via Python (Pandas) to guarantee error-free relational joins in MySQL and spatial aggregation in Power BI.
3. **Automated Testing:** Validated pipeline transformations using unit tests (`pytest`) prior to production database loading.
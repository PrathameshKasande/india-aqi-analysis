# 🇮🇳 India Air Quality Index (AQI) Analysis & Data Pipeline

An end-to-end data engineering and exploratory data analysis (EDA) project built in Python. This project ingests, cleans, validates, and analyzes air quality datasets across various Indian states and monitoring stations to uncover critical environmental insights and pollution trends.

---

## 🚀 Project Overview

Air pollution is a critical environmental and public health challenge. This project automates the data processing workflow for raw Indian AQI records to transform messy, unstructured data into clean, analysis-ready datasets. It features robust automated testing, exploratory data visualizations, and structured pipeline execution.

---

## 📂 Project Structure

```text
india-aqi-analysis/
│
├── data/
│   ├── raw/
│   │   └── aqi.csv                 # Raw historical AQI dataset
│   └── processed/
│       └── cleaned_aqi.csv         # Cleaned and validated output dataset
│
├── python/
│   ├── tests/
│   │   └── test_data_cleaning.py   # Pytest unit tests for pipeline verification
│   ├── main.py                     # End-to-end execution script
│   └── requirements.txt            # Project dependencies
│
├── notebooks/
│   └── india_aqi_eda.ipynb         # Exploratory Data Analysis & visual plots
│
├── config.yaml                     # Centralized project configuration & paths
└── README.md                       # Project documentation
```

---

## 🛠️ Tech Stack & Libraries

- **Language:** Python 3.11 / 3.13
- **Data Manipulation & Ingestion:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Testing Framework:** Pytest
- **Configuration:** PyYAML

---

## ⚙️ Key Pipeline Features

1. **Automated Data Cleaning (`main.py`):**
   - Drops redundant or fully null columns (e.g., `note`).
   - Parses date strings into standardized datetime formats (`dayfirst=True`).
   - Cleans categorical string columns by stripping leading/trailing whitespaces.
   - Imputes missing numerical values using robust median statistics.
   - Automatically detects and removes duplicate records.

2. **Automated Unit Testing (`tests/test_data_cleaning.py`):**
   - Ensures data integrity through automated test suites covering null value handling and duplicate removal.
   - Verified via `pytest`.

3. **Exploratory Data Analysis (`notebooks/india_aqi_eda.ipynb`):**
   - Distribution analysis of air quality categories across monitoring stations.
   - Identification of the top 10 most polluted states by average AQI value.
   - Frequency analysis of prominent pollutants (e.g., $PM_{2.5}$, $PM_{10}$, $NO_2$).

---

## 🚀 How to Run the Project

### 1. Clone & Setup Environment
Open your terminal in the project directory and install the required dependencies:
```bash
cd india-aqi-analysis
pip install -r python/requirements.txt
```

### 2. Run Unit Tests
Verify data cleaning logic and code health with `pytest`:
```bash
python -m pytest python/tests/ -v
```

### 3. Execute the Main Data Pipeline
Run the processing script to ingest raw data, clean it, and export the processed CSV:
```bash
python python/main.py
```

### 4. Explore via Jupyter Notebook
Launch your notebook viewer to inspect the EDA visualizations:
```bash
jupyter notebook notebooks/india_aqi_eda.ipynb
```

---

## 📊 Key Insights & Findings
- **Pollution Concentration:** Major urban centers and specific states consistently display higher average AQI values, predominantly driven by particulate matter ($PM_{2.5}$ and $PM_{10}$).
- **Data Quality Improvement:** Standardizing and deduplicating raw records improved data consistency, ensuring reliable downstream statistical summaries and modeling readiness.

---

## 👤 Author
**Prathmesh**  
*Data Science & Analytics Project*
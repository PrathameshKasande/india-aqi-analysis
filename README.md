# 🇮🇳 India Air Quality Analytics & Monitoring System

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Preprocessing-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![MySQL](https://img.shields.io/badge/MySQL-Database_Backend-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Power BI](https://img.shields.io/badge/Power_BI-Executive_Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)

</div>

---

## 📌 Executive Summary
Urban air pollution is a critical environmental and public health challenge across India. Raw environmental monitoring logs are often fragmented, noisy, and difficult for policymakers or analysts to digest. This project implements a **complete end-to-end data analytics and business intelligence pipeline**—transforming raw monitoring logs into a clean relational database and presenting them via an enterprise-grade, 4-page interactive **Power BI Dashboard** built around a professional Dark Navy theme (`#0B192C`).

---

## 🎯 Problem Statement & Objectives

### **The Problem**
* **Data Fragmentation:** Environmental data collected across hundreds of monitoring stations and states is often messy, unstructured, and siloed in raw CSV/Excel files.
* **Sensor Gaps & Inconsistencies:** Missing values, unstandardized regional text strings, and irregular pollutant logs make direct aggregation unreliable.
* **Lack of Unified Visual Insight:** Stakeholders lacked a cohesive, multi-dimensional platform to evaluate pollutant compositions (`PM2.5`, `PM10`, `NO₂`, `CO`), infrastructure distribution, and health status classifications simultaneously.

### **What This Project Solved**
1. **Automated Data Hygiene:** Built a robust data preprocessing workflow using Python to clean, impute missing sensor entries, and standardize geographic schemas.
2. **Relational Data Modeling:** Designed a structured relational database backend in MySQL to optimize query execution and storage efficiency.
3. **Executive Visual Intelligence:** Developed an interactive 4-page Power BI dashboard featuring dynamic slicers, KPI metric strips, infrastructure coverage analysis, and health classification breakdowns.

---

## 🏗️ End-to-End Architecture & Workflow

```text
[ 1. Raw Excel / CSV Logs ] 
            │
            ▼ (Exploratory Analysis & Structural Checks)
[ 2. Python (Pandas & NumPy) ] ──(Data Cleaning & Imputation)──► [ Cleaned Dataset ]
            │
            ▼ (Relational Insertion & Schema Design)
[ 3. MySQL Database Backend ] ──(Optimized Queries & Aggregations)──► [ SQL Server ]
            │
            ▼ (Data Modeling & DAX Measures)
[ 4. Power BI Executive Dashboard (4 Pages) ]

'''


📂 Project Directory Structure:

india-aqi-analysis/
├── powerbi/
│   ├── AQI Dashboard.pbix              # Traditional binary file
│   ├── AQI Dashboard.pbip              # Power BI Project format (Git trackable)
│   ├── AQI Dashboard.Report/           # Report layout and visual configurations
│   ├── AQI Dashboard.SemanticModel/    # Data model, relationships, and tables
│   ├── dax_measures.dax                # Custom DAX calculation scripts
│   └── screenshots/                    # Dashboard page previews for documentation
├── python/
│   ├── data/processed/                 # Cleaned CSV datasets
│   ├── notebooks/                      # Exploratory Data Analysis (EDA) notebooks
│   └── src/                            # Data cleaning and pipeline scripts
├── sql/                                # Database creation, tables, and analysis queries
├── data/                               # Raw and processed data assets
├── docs/                               # Project overviews and workflow specifications
└── reports/                            # Generated data quality reports and insights

📂 Detailed Pipeline Breakdown by Stage
Stage 1: Ingestion & Exploratory Analysis (Excel)Inspected raw files to understand table schemas, field attributes (aqi_value, prominent_pollutant, state, area, number_of_monitoring_stations), and anomaly patterns before automated pipeline migration.Stage 2: Preprocessing & Cleaning (Python)Utilized Pandas and NumPy to handle missing environmental readings.Standardized text formats across state and city names to guarantee error-free relational joins downstream.Engineered derived categorical fields for air quality health statuses (Satisfactory, Moderate, Poor, Very Poor, Severe).Stage 3: Database Management & Storage (MySQL)Imported cleaned datasets into a structured relational database using MySQL Workbench.Executed aggregation queries to validate monitoring station totals by state and calculate baseline national AQI averages prior to BI consumption.Stage 4: Business Intelligence & Visualization (Power BI)Designed a strict Dark Navy Theme (#0B192C background, high-contrast white text) for executive presentation standards.Implemented the 4-Page Dashboard Architecture:Page 1: National Overview — High-level executive summary cards and macro AQI performance indicators.Page 2: Regional Map — Geographical concentration hot-spots tracking pollution spread across Indian states.Page 3: Pollutant Composition — Granular tracking featuring Avg. PM2.5, PM10, $\text{NO}_2$, and CO cards, state contribution share bar charts, time-series trends, and a state interaction slicer.Page 4: Monitoring & Station Analytics — Infrastructure assessment displaying total stations (441K), monitored cities (291), coverage bars, status classification donut charts, multi-series status distributions across top states, and an expandable hierarchical matrix table (State $\rightarrow$ Area).🛠️ Tech Stack & ToolchainProgramming Language: Python 3 (Pandas, NumPy)Database & Querying: MySQL, SQL WorkbenchBusiness Intelligence: Power BI Desktop, DAX, Data ModelingVersion Control: Git, GitHub (PrathameshKasande)🚀 How to Run the ProjectClone the Repository:Bashgit clone [https://github.com/PrathameshKasande/india-aqi-analysis.git](https://github.com/PrathameshKasande/india-aqi-analysis.git)
Database Setup: Run the provided SQL scripts in the sql/ folder using MySQL Workbench to initialize the database schema and populate tables.Power BI Dashboard: Open the .pbix or .pbip project file located in the powerbi/ folder using Power BI Desktop.Explore: Use page navigation tabs and interactive slicers across all 4 executive pages to explore regional insights.👤 AuthorPrathamesh KasandeComputer Science & Engineering Graduate | Data Analyst & AI Enthusiast
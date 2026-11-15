# ⚙️ Project Workflow & Pipeline Architecture

This document outlines the systematic, multi-phase technical workflow implemented for the **India Air Quality Index (AQI) Analysis** project, tracking data from raw ingestion to executive dashboard deployment.

---

## 🚀 Phase 1: Excel Exploration & Initial Dashboard
* **Data Profiling & Inspection:** Initial exploratory data analysis and quality checks performed using Excel (`AQI_Analysis_Dashboard.xlsx`) on the primary dataset comprising **235,785 records**.
* **Summary Statistics:** Calculation of baseline metrics, including a National Average AQI of **111.13** and a Max AQI spike of **500**.
* **Categorization:** Initial identification and mapping of air quality status classifications and dominant atmospheric pollutants (`PM10`, `PM2.5`, `NO₂`, `CO`).

---

## 🐍 Phase 2: Python Data Pipeline (`python/`)
* **Scripting & Automation:** Developed automated data cleaning scripts (`data_cleaning.py`, `data_quality_check.py`) using Python 3, Pandas, and NumPy.
* **Configuration & Testing:** Implemented configuration management via `config.yaml` and robust unit testing frameworks using `pytest` (`test_data_cleaning.py`) to ensure data hygiene.
* **Export:** Processed and structured cleaned data outputs (`cleaned_aqi.csv`) stored in `data/processed/` for downstream database ingestion.

---

## 🗄️ Phase 3: SQL Database Engineering (`sql/`)
* **Relational Schema Design:** Created structured SQL DDL scripts (`01_create_database.sql`, `02_create_tables.sql`) using MySQL Workbench.
* **Analytical Queries & Views:** Executed custom SQL scripts (`03_data_quality_checks.sql`, `04_analysis_queries.sql`, `05_create_views.sql`) to aggregate pollution metrics, validate monitoring station counts, and optimize query performance.

---

## 📊 Phase 4: Power BI Visualization (`powerbi/`)
* **Business Intelligence Dashboard:** Developed an enterprise-grade, 4-page interactive reporting suite built around a professional **Dark Navy Theme** (`#0B192C`).
* **Core Dashboard Architecture:**
  * **Page 1: National Overview** — High-level summary cards and macro AQI performance indicators.
  * **Page 2: Regional Map** — Geographical distribution maps tracking regional pollution hot-spots.
  * **Page 3: Pollutant Composition** — Granular tracking featuring Avg. PM2.5/PM10/NO₂/CO cards, state contribution share bar charts, time-series trends, and interactive state slicers.
  * **Page 4: Monitoring & Station Analytics** — Infrastructure assessment (`441K` total stations, `291` monitored cities), status classification donut charts, multi-series status distributions across top states, and an expandable hierarchical matrix table (`State` $\rightarrow$ `Area`).

---

## 📦 Phase 5: Documentation & GitHub Deployment
* **Comprehensive Documentation:** Compiled project overview specifications (`docs/project_overview.md`), technical workflow guidelines (`docs/project_workflow.md`), and automated reports (`reports/`).
* **Version Control & Publishing:** Organized the repository file structure (`powerbi/`, `python/`, `sql/`, `docs/`, `data/`) and published the complete production-ready project to GitHub (`PrathameshKasande`).
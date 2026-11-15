#Pipeline Orchestrator

import os
import pandas as pd
from src.data_cleaning import clean_aqi_data
from src.data_quality_check import run_quality_checks
from src.analysis import perform_analysis

def load_config():
    return {
        'paths': {
            'raw_data': '../data/raw/aqi.csv',
            'processed_data': '../data/processed/cleaned_aqi.csv',
            'reports_dir': '../reports'
        }
    }

def main():
    print("=" * 50)
    print(" Starting India AQI Data Analysis Pipeline ")
    print("=" * 50)
    
    config = load_config()
    
    raw_path_root = os.path.join(os.path.dirname(__file__), "../data/raw/aqi.csv")
    raw_path_alt = os.path.join(os.path.dirname(__file__), "../aqi.csv")
    
    if not os.path.exists(raw_path_root) and os.path.exists(raw_path_alt):
        os.makedirs(os.path.dirname(raw_path_root), exist_ok=True)
        import shutil
        shutil.copy(raw_path_alt, raw_path_root)
        
    raw_path = os.path.join(os.path.dirname(__file__), config['paths']['raw_data'])
    print(f"[1/4] Loading raw data from: {raw_path}")
    if not os.path.exists(raw_path):
        raise FileNotFoundError(f"Raw data file not found at {raw_path}.")
    
    df = pd.read_csv(raw_path)
    
    print("[2/4] Executing data cleaning module...")
    df_cleaned = clean_aqi_data(df)
    
    print("[3/4] Running data quality validation checks...")
    run_quality_checks(df_cleaned)
    
    print("[4/4] Performing statistical and trend analysis...")
    perform_analysis(df_cleaned)
    
    processed_path = os.path.join(os.path.dirname(__file__), config['paths']['processed_data'])
    os.makedirs(os.path.dirname(processed_path), exist_ok=True)
    df_cleaned.to_csv(processed_path, index=False)
    
    print("=" * 50)
    print(f" Pipeline Finished Successfully! Cleaned data saved to {processed_path}")
    print("=" * 50)

if __name__ == "__main__":
    main()
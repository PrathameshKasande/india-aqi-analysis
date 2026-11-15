import pandas as pd

def run_quality_checks(df: pd.DataFrame) -> bool:
    """
    Validates missing values and AQI value boundaries (0-500).
    """
    print("--- Running Data Quality Validation Checks ---")
    
    critical_cols = ['date', 'state', 'area', 'aqi_value', 'air_quality_status']
    for col in critical_cols:
        null_count = df[col].isnull().sum()
        print(f"[Check] Null values in '{col}': {null_count}")
        assert null_count == 0, f"Critical column {col} contains null values!"
        
    min_aqi = df['aqi_value'].min()
    max_aqi = df['aqi_value'].max()
    print(f"[Check] AQI Range: Min = {min_aqi}, Max = {max_aqi}")
    assert min_aqi >= 0 and max_aqi <= 500, "AQI values out of standard CPCB bounds (0-500)!"
    
    print("All data quality validation checks passed successfully! ✅")
    return True
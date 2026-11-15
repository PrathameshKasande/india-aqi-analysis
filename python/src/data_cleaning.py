import pandas as pd
import numpy as np
import os

def clean_aqi_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the raw AQI dataset by parsing dates, standardizing columns, 
    handling missing values, and removing duplicates.
    """
    df_clean = df.copy()
    
    if 'note' in df_clean.columns:
        df_clean = df_clean.drop(columns=['note'])
        
    if 'date' in df_clean.columns:
        df_clean['date'] = pd.to_datetime(df_clean['date'], dayfirst=True, errors='coerce')
        
    str_cols = ['state', 'area', 'prominent_pollutants', 'air_quality_status', 'unit']
    for col in str_cols:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].astype(str).str.strip()
            
    if 'aqi_value' in df_clean.columns:
        df_clean['aqi_value'] = pd.to_numeric(df_clean['aqi_value'], errors='coerce')
        df_clean['aqi_value'] = df_clean['aqi_value'].fillna(df_clean['aqi_value'].median())
        
    if 'number_of_monitoring_stations' in df_clean.columns:
        df_clean['number_of_monitoring_stations'] = pd.to_numeric(df_clean['number_of_monitoring_stations'], errors='coerce').fillna(1).astype(int)
        
    initial_len = len(df_clean)
    df_clean = df_clean.drop_duplicates()
    print(f"Data Cleaning: Dropped {initial_len - len(df_clean)} duplicate rows.")
    
    return df_clean
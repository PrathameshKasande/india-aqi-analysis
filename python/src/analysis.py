import pandas as pd

def perform_analysis(df: pd.DataFrame):
    """
    Generates summary statistics and state-wise pollution rankings.
    """
    print("--- Performing AQI Trend & Statistical Analysis ---")
    
    mean_aqi = df['aqi_value'].mean()
    median_aqi = df['aqi_value'].median()
    max_aqi = df['aqi_value'].max()
    min_aqi = df['aqi_value'].min()
    
    print(f"Total Records Analyzed: {len(df)}")
    print(f"National Average AQI: {mean_aqi:.2f}")
    print(f"Median AQI: {median_aqi}")
    print(f"Max AQI: {max_aqi} | Min AQI: {min_aqi}")
    
    state_avg = df.groupby('state')['aqi_value'].mean().sort_values(ascending=False).head(5)
    print("\nTop 5 States by Average AQI:")
    print(state_avg)
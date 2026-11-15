#unit test 

import pandas as pd
import pytest
from src.data_cleaning import clean_aqi_data

def test_clean_aqi_data_removes_duplicates(sample_aqi_dataframe):
    cleaned_df = clean_aqi_data(sample_aqi_dataframe)
    assert len(cleaned_df) == 3

def test_clean_aqi_data_handles_nulls(sample_aqi_dataframe):
    cleaned_df = clean_aqi_data(sample_aqi_dataframe)
    assert cleaned_df['aqi_value'].isnull().sum() == 0
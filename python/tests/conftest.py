#Test Fixtures

import pytest
import pandas as pd

@pytest.fixture
def sample_aqi_dataframe():
    data = {
        'City': ['Delhi', 'Delhi', 'Mumbai', 'Bangalore'],
        'date': ['01-01-2023', '01-01-2023', '01-01-2023', '01-01-2023'],
        'state': ['Delhi', 'Delhi', 'Maharashtra', 'Karnataka'],
        'area': ['ITO', 'ITO', 'Colaba', 'Indiranagar'],
        'number_of_monitoring_stations': [2, 2, 1, 1],
        'prominent_pollutants': ['PM2.5', 'PM2.5', 'PM10', 'NO2'],
        'aqi_value': [350.0, 350.0, 180.0, None],
        'air_quality_status': ['Very Poor', 'Very Poor', 'Moderate', 'Satisfactory'],
        'unit': ['AQI', 'AQI', 'AQI', 'AQI'],
        'note': [None, None, None, None]
    }
    return pd.DataFrame(data)
import pandas as pd
import mysql.connector

# 1. Load your cleaned CSV
df = pd.read_csv('../data/processed/cleaned_aqi.csv')

# 2. Connect to your local MySQL database (replace 'your_password' with your MySQL password)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password", 
    database="india_aqi_db"
)
cursor = conn.cursor()

# 3. Loop through dataframe and insert rows
for index, row in df.iterrows():
    sql = """
        INSERT INTO aqi_cleaned_data 
        (date, state, area, number_of_monitoring_stations, prominent_pollutants, aqi_value, air_quality_status, unit) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        str(row['date']),
        str(row['state']),
        str(row['area']),
        int(row['number_of_monitoring_stations']),
        str(row['prominent_pollutants']),
        float(row['aqi_value']),
        str(row['air_quality_status']),
        str(row['unit'])
    )
    cursor.execute(sql, values)

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()

print(f"Successfully loaded {len(df)} rows into MySQL via Python!")
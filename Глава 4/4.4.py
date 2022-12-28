import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('new_ekb_weather.csv')
df = df.drop('Unnamed: 0', axis=1)
df['date'] = pd.to_datetime(df['date'])
print(df)


group_month_temp = df.groupby('month')['temp'].agg([min, max, np.median])

print(group_month_temp)


group_month_pressure = df.groupby('month')['pressure'].agg([min, max, np.median])

print(group_month_pressure)


group_month_humidity = df.groupby('month')['humidity'].agg([min, max, np.median])

print(group_month_humidity)
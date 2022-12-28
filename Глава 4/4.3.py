import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('new_ekb_weather.csv')
df = df.drop('Unnamed: 0', axis=1)
df['date'] = pd.to_datetime(df['date'])
print(df)


pearson_temp_pressure = df['temp'].corr(df['pressure']) 
pearson_temp_humidity = df['temp'].corr(df['humidity']) 
pearson_pressure_humidity = df['pressure'].corr(df['humidity']) 

print('Коэффициент Пирсона\n'
	'Температура/давление: {pearson_temp_pressure}\n'
	'Температура/влажность: {pearson_temp_humidity}\n'
	'Давление/влажность: {pearson_pressure_humidity}\n'.format(pearson_temp_pressure = pearson_temp_pressure,
	pearson_temp_humidity = pearson_temp_humidity, pearson_pressure_humidity = pearson_pressure_humidity ))
print('Корреляция данных покоэффициенту Пирсона для всех данных \n', df.corr(numeric_only = True))


pd.plotting.scatter_matrix(df, alpha = 0.5, color='r')
plt.show()
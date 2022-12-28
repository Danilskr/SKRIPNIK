import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('new_ekb_weather.csv')
df = df.drop('Unnamed: 0', axis=1)
df['date'] = pd.to_datetime(df['date'])
print(df)

month_temp_var = (df.groupby('month')['temp'].apply(lambda i: round(np.var(i), 2)))
month_temp_std = (df.groupby('month')['temp'].apply(lambda i: round(np.std(i), 2)))

dict_month_temp_var = month_temp_var.to_dict()
dict_month_temp_std = month_temp_std.to_dict()

print('Дисперсия значений температуры по месяцам: {var} \n\n'	'Стандартное отклонение значений температуры по месяцам:{std}'.format(var = dict_month_temp_var, std = dict_month_temp_std))


month_temp_var = (df.groupby('month')['pressure'].apply(lambda i: round(np.var(i), 2)))
month_temp_std = (df.groupby('month')['pressure'].apply(lambda i: round(np.std(i), 2)))

dict_month_pressure_var = month_temp_var.to_dict()
dict_month_pressure_std = month_temp_std.to_dict()

print('Дисперсия значений давления по месяцам: {var} \n\n' 	'Стандартное отклонение значений давления по месяцам:{std}'.format(var = dict_month_pressure_var, std = dict_month_pressure_std))

month_humidity_var = (df.groupby('month')['humidity'].apply(lambda i: round(np.var(i), 2)))
month_humidity_std = (df.groupby('month')['humidity'].apply(lambda i: round(np.std(i), 2)))

dict_month_humidity_var = month_humidity_var.to_dict()
dict_month_humidity_std = month_humidity_std.to_dict()

print('Дисперсия значений влажности по месяцам: {var} \n\n' 	'Стандартное отклонение значений влажности по месяцам:{std}'.format(var = dict_month_humidity_var, std = dict_month_humidity_std))

df_describe = df.describe()

print(df_describe, end='\n'*3)
print('Межквартильное расстояние:\n', df_describe.loc['75%']-df_describe.loc['25%'])

print(df)

#plt.rcParams["figure.figsize"] = [10.50, 10.50]
plt.rcParams["figure.autolayout"] = True
plt.boxplot(df.temp)
plt.title('temp')
plt.show()

df['pressure'].plot(kind='box')
plt.boxplot(df.pressure)
plt.title('pressure')
plt.show()

plt.boxplot(df.humidity)
plt.title('humidity')
plt.show()
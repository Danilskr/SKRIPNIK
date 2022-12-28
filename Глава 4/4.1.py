import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
df = pd.read_csv('ekb_weather.csv')

print(df.head(10))
print(df.describe())

df['date'] = pd.to_datetime(df['date'])

print(df.info())

df = pd.read_csv('ekb_weather.csv')
months = {1:'Январь', 2:'Февраль', 3:'Март', 4:'Апрель', 5:'Май', 6:'Июнь', 7:'Июль', 8:'Август', 9:'Сентябрь', 10:'Октябрь', 11:'Ноябрь', 12:'Декабрь'}

df['date'] = pd.to_datetime(df['date'])
df['month'] = pd.DatetimeIndex(df['date']).month

print(df)

df = pd.read_csv('new_ekb_weather.csv')
df = df.drop('Unnamed: 0', axis=1)
df['date'] = pd.to_datetime(df['date'])
print(df)

mean_month_group = df.groupby('month').mean(numeric_only = True)
print(mean_month_group)


if mean_month_group.loc['Январь','temp'] < mean_month_group.loc['Декабрь','temp']:
    print("Январь", '\n')
else:
    print("Декабрь", '\n')
    
if mean_month_group.loc["Апрель",'pressure'] > mean_month_group.loc["Ноябрь",'pressure']:
    print("Апрель", '\n')
else:
    print("Ноябрь", '\n')
    
    
if mean_month_group.loc["Июнь",'humidity'] > mean_month_group.loc["Август",'humidity']:
    print("Июнь", '\n')
else:
    print("Август", '\n')



df = pd.read_csv('new_ekb_weather.csv')
df = df.drop('Unnamed: 0', axis=1)
df['date'] = pd.to_datetime(df['date'])
print(df)

month_temp_group = df.groupby('month')['temp'].agg([np.mean,np.median, lambda i: stats.mode(i, axis=None,keepdims=False)[0]])
month_temp_group = month_temp_group.reset_index(level='month')
month_temp_group.rename(columns = {'month' :  'Month', 'mean' : 'Mean', 'median' : 'Median', '<lambda_0>' : 'Mode'},inplace = True)

print(month_temp_group)


fig, (ax1,ax2, ax3) = plt.subplots(nrows = 3, ncols = 1, figsize = (15,15))

ax1.bar(month_temp_group['Month'], month_temp_group['Mean'], color = 'y')
ax2.bar(month_temp_group['Month'], month_temp_group['Median'])
ax3.bar(month_temp_group['Month'], month_temp_group['Mode'], color = 'g')

plt.show()


month_pressure_group = df.groupby('month')['pressure'].agg([np.mean,np.median, lambda i: stats.mode(i, axis=None,keepdims=False)[0]])
month_pressure_group = month_pressure_group.reset_index(level='month')
month_pressure_group.rename(columns = {'month' :  'Month', 'mean' : 'Mean', 'median' : 'Median', '<lambda_0>' : 'Mode'},inplace = True)

print(month_pressure_group)


fig, (ax1,ax2, ax3) = plt.subplots(nrows = 3, ncols = 1, figsize = (15,15))

ax1.bar(month_pressure_group['Month'], month_pressure_group['Mean'], color = 'r')
ax2.bar(month_pressure_group['Month'], month_pressure_group['Median'])
ax3.bar(month_pressure_group['Month'], month_pressure_group['Mode'], color = 'b')

plt.show()


month_humidity_group = df.groupby('month')['pressure'].agg([np.mean,np.median, lambda i: stats.mode(i, axis=None,keepdims=False)[0]])
month_humidity_group = month_humidity_group.reset_index(level='month')
month_humidity_group.rename(columns = {'month' :  'Month', 'mean' : 'Mean', 'median' : 'Median', '<lambda_0>' : 'Mode'},inplace = True)

print(month_humidity_group)


fig, (ax1,ax2, ax3) = plt.subplots(nrows = 3, ncols = 1, figsize = (15,15))

ax1.bar(month_humidity_group['Month'], month_humidity_group['Mean'], color = 'g')
ax2.bar(month_humidity_group['Month'], month_humidity_group['Median'], color = 'b')
ax3.bar(month_humidity_group['Month'], month_humidity_group['Mode'], color = 'y')

plt.show()
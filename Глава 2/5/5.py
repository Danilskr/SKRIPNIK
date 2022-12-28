import pandas as pd
import numpy as np

df = pd.read_csv('precious_metal.csv', sep = ';')
df.set_axis(['gold', 'silver', 'platinum', 'palladium','date'], axis = 'columns', inplace = True)
print("задание 5.1")
df.head()
print(df)

print(df.info())

print("задание 5.2")
df['date'] = pd.to_datetime(df.date, format = '%d.%m.%Y %H:%M')

print(df.info())


import matplotlib.pyplot as plt
import pandas as pd

print("задание 5.3")
months = {1:'Январь', 2:'Февраль', 3:'Март', 4:'Апрель', 5:'Май', 6:'Июнь', 7:'Июль', 8:'Август', 9:'Сентябрь', 10:'Октябрь', 11:'Ноябрь', 12:'Декабрь'}

df['date'] = pd.to_datetime(df['date'])
df['month'] = pd.DatetimeIndex(df['date']).month
print(df)
print("задание 5.4")
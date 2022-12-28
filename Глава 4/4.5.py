from scipy import stats as st
import pandas as pd

df = pd.read_csv('ekb_weather.csv')
df['date'] = pd.to_datetime(df['date'])

print(df)


assumed_value_temp = 5
alpha = 0.05

result = st.ttest_1samp(df['temp'], assumed_value_temp)

print('p-значение:', round(result.pvalue*100,5),'%')

if (result.pvalue <alpha):
    print('Нулевая гипотеза отвергнута.')
else:
    print('Нулевая гипотеза принята.')


assumed_value_pressure = 761
alpha = 0.05

result = st.ttest_1samp(df['pressure'],assumed_value_pressure,nan_policy= 'omit')

print('p-значение:', round(result.pvalue*100,2),'%')

if (result.pvalue < alpha):
    print('Нулевая гипотеза отвергнута.')
else:
    print('Нулевая гипотеза принята.')

assumed_value_humidity = 66
alpha = 0.05

result = st.ttest_1samp(df['humidity'],assumed_value_humidity,nan_policy= 'omit')

print('p-значение:', round(result.pvalue*100,2),'%')

if (result.pvalue < alpha):
    print('Нулевая гипотеза отвергнута.')
else:
    print('Нулевая гипотеза принята.')
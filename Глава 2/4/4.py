import pandas as pd

df = pd.read_csv('precious_metal.csv', sep=';')

print("задание 4.1")
print(df.info())

df.set_axis(['gold', 'silver', 'platinum', 'palladium','date'], axis = 'columns', copy = True)
print("задание 4.2")
print(df)
print("задание 4.3")
print('blank gold:', df['gold'].isnull().sum())
print('blank silver:', df['silver'].isnull().sum())
print('blank platinum:', df['platinum'].isnull().sum())
print('blank palladium:', df['palladium'].isnull().sum())
print('blank date:', df['date'].isnull().sum())
print('\n'*3)

df_new = df.fillna(0)
#Где пустые ваши пустые колонки
print(df_new)
print('blank gold:', df_new['gold'].isnull().sum())
print('blank silver:', df_new['silver'].isnull().sum())
print('blank platinum:', df_new['platinum'].isnull().sum())
print('blank palladium:', df_new['palladium'].isnull().sum())
print('blank date:', df_new['date'].isnull().sum())


print("задание 4.4")
df['gold'] = df['gold'].apply(lambda x: float(str(x).replace(',','.')))
df['silver'] = df['silver'].apply(lambda x: float(str(x).replace(',','.')))
df['platinum'] = df['platinum'].apply(lambda x: float(str(x).replace(',','.')))
df['palladium'] = df['palladium'].apply(lambda x: float(str(x).replace(',','.')))

print(df)

print("задание 4.5")
df = pd.read_csv('https://elteha.ru/data_science/precious_metal.csv', sep = ';')
df.set_axis(['gold', 'silver', 'platinum', 'palladium','date'], axis = 'columns', inplace  = True)
df.dropna(subset = ['gold', 'silver', 'platinum', 'palladium'], inplace  = True) #Отсекаем ячейки в которых были пропущ занч.
df.drop(["date"], axis = 1, inplace=True) #Отсекаем дату 

df['gold'] = df['gold'].apply(lambda x: float(str(x).replace(',','.')))
df['silver'] = df['silver'].apply(lambda x: float(str(x).replace(',','.')))
df['platinum'] = df['platinum'].apply(lambda x: float(str(x).replace(',','.')))
df['palladium'] = df['palladium'].apply(lambda x: float(str(x).replace(',','.')))
# Больше колонок богу колонок
value_usd = float(73.41)
df["gold_usd"] = round(df['gold'] / value_usd, 2)
df["silver_usd"] = round(df['silver'] / value_usd, 2)
df["platinum_usd"] = round(df['platinum'] / value_usd, 2)
df["palladium_usd"] = round(df['palladium'] / value_usd, 2)
df.to_csv("precious_metal_new.xls")

print(df)
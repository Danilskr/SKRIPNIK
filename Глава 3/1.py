import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
#1
print ("Задание 1.1")
x_data = np.linspace(0, 20, 100)
y_data = np.sin(x_data)
f = plt.figure(figsize=(10,5))
a = plt.axes()
plt.plot(x_data, y_data, color='r', linewidth='1.0')
plt.grid('g--',linewidth='0.8')
plt.xlabel('х')
plt.ylabel('y')
plt.title('Структура')
plt.show()

#2
x_data = np.linspace(0, 20, 100)
y_data = np.sin(x_data)
plt.plot(x_data, y_data, color='b', linewidth='1.0')
plt.grid('g--',linewidth='0.8')
plt.xlabel('х')
plt.ylabel('y')
plt.title('Объект')
plt.show()


print ("Задание 1.2")
x_data = np.linspace(0, 10, 100)
y_data = np.sin(x_data)
fig = plt.figure(figsize=(10, 5))
ax = plt.axes()
plt.plot(x_data, y_data, linewidth='3.0', marker='o')
plt.grid('r--',linewidth='0.9')
plt.xlabel('х')
plt.ylabel('y')
plt.show()



print ("Задание 1.3")


x_data = [random.randint(0,100) for x in range(100)]

fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(nrows=2, ncols=3, figsize=(15,10))

ax1.hist(x_data, bins = 10, color = 'b')
ax2.hist(x_data, bins = 30, color = 'y')
ax3.hist(x_data, bins = 50, color = 'r')

ax4.hist(x_data, bins = 20, color = 'b')
ax5.hist(x_data, bins = 40, color = 'y')
ax6.hist(x_data, bins = 40, color = 'r')

plt.show()

print ("Задание 1.4")
heights = [188, 172, 187, 161, 183, 172, 185, 163, 173,
           183, 174, 174, 175, 178, 183, 195, 178, 173,
           174, 183, 174, 181, 162, 180, 170, 175, 182,
           180, 183, 178, 182, 188, 175, 179, 184, 193,
           182, 183, 175, 185, 182, 183, 156, 185, 199]

gender = ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'female',
           'male', 'female', 'female', 'male', 'female', 'male', 'male', 'female', 'female',
           'female', 'male', 'female', 'male', 'female', 'male', 'female', 'female', 'female',
           'female', 'male', 'female', 'female', 'male', 'female', 'male', 'male', 'male',
           'male', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'male']

weights = [86, 71, 89, 64, 83, 71, 86, 68, 73, 84, 73,
           72, 75, 78, 85, 93, 78, 70, 74, 80, 83, 82,
           68, 80, 73, 78, 82, 81, 83, 79, 82, 86, 76,
           77, 80, 103, 82, 83, 77, 89, 80, 85, 82, 85, 110]

ages = [58, 61, 54, 54, 58, 57, 63, 54, 37, 51, 34,
        26, 50, 48, 45, 52, 56, 46, 54, 28, 52, 47,
        55, 55, 54, 42, 51, 56, 55, 51, 54, 32, 21,
        62, 43, 55, 56, 61, 53, 22, 64, 45, 54, 47, 38]

print ("1. Диограммы")
data_dict = {'heights':(heights), 'weights': (weights), 'ages': (ages), 'gender': (gender)}
df = pd.DataFrame(data_dict)
plt.scatter( df['heights'],df['weights'],color='y', marker='o')
plt.xlabel('heights')
plt.ylabel('weights')
plt.title('График heights/weight')
plt.show()
df.plot(kind= 'scatter', x = 'heights', y = 'ages',color='r', title= 
'График heights/ages')
plt.show()
df.plot(kind= 'scatter', x = 'weights', y = 'ages',color='b', title= 
'График weights/ages')
plt.show()
print ("2. Гистограммы")
df['heights'].plot(
    kind = 'hist',
    title = 'heights',
    bins = 5)

plt.show()
df['weights'].plot(
    kind = 'hist',
    title = 'weights',
    bins = 5,
    color = 'r')

plt.show()
df['ages'].plot(
    kind = 'hist',
    title = 'ages',
    bins = 5,
    color = 'g')

plt.show()
print ("3. Линейные диограммы")
gender_cnt = df['gender'].value_counts()

plt.style.use('ggplot')
gender_cnt.plot(kind = 'bar')
plt.show()

df_describe = df.describe()

print(df_describe, end='\n'*3)
print('Межквартильное расстояние:\n', df_describe.loc['75%']-df_describe.loc['25%'])

import numpy as np

plt.style.use ('classic')

plt.boxplot(heights)
plt.title('heights')
plt.show()

plt.boxplot(weights)
plt.title('weights')
plt.show()

plt.boxplot(ages)
plt.title('ages')
plt.show()

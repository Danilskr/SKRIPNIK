import pandas as pd


heights = [188, 172, 187, 161, 183, 172, 185, 163, 173, 183, 174, 174, 175,
178, 183, 195, 178, 173, 174, 183, 174, 181, 162, 180, 170, 175, 182, 180, 183,
178, 182, 188, 175, 179, 184, 193, 182, 183, 175, 185, 182, 183, 150, 185, 199]

weights = [86, 71, 89, 64, 83, 72, 86, 68, 73, 84, 73, 72, 75, 78, 85, 93, 78,
70, 74, 80, 83, 82, 68, 80, 73, 78, 82, 81, 83, 79, 82, 86, 76, 77, 80, 103,
82, 83, 77, 89, 80, 85, 82, 85, 110]

ages = [58, 61, 54, 54, 58, 57, 63, 54, 37, 51, 34, 26, 50, 48, 45, 52, 56,
40, 54, 28, 52, 47, 55, 55, 54, 42, 51, 50, 55, 51, 54, 32, 21, 62, 43, 55,
50, 61, 53, 22, 64, 45, 54, 47, 38]


print("задание 3.1")
data_dict = {'heights':(heights), 'weights': (weights) , 'ages': (ages)}
df = pd.DataFrame(data_dict)
new_one_df = df.head(40)
print(new_one_df)


print("задание 3.2")
data_dict = {'heights':(heights), 'weights': (weights) , 'ages': (ages)}
df = pd.DataFrame(data_dict)
new_df = df.head(40)
funс = new_df[new_df["heights"] > 180]
print(funс)
print("Count rows", len(funс.index))

print("задание 3.3")
data_dict = {'heights':(heights), 'weights': (weights) , 'ages': (ages)}
df = pd.DataFrame(data_dict)
new_df = df.head(40)
funс = new_df[new_df.weights < 80]

print("Count rows", len(funс.index))
print(funс)
print("задание 3.4")
data_dict = {'heights':(heights), 'weights': (weights) , 'ages': (ages)}
df = pd.DataFrame(data_dict)
new_df = df.head(40)
funс = new_df [((new_df.ages < 50) & (new_df.ages > 30)) ]

print("Count rows", len(funс.index))
print(funс)

print("задание 3.5")
data_dict = {'heights':(heights), 'weights': (weights) , 'ages': (ages)}
df = pd.DataFrame(data_dict)
new_df = df.head(40)
funс = new_df [((new_df.heights > 170) & (new_df.weights > 80)) ]

print("Count rows", len(funс.index))
print(funс)
print(funс.describe())
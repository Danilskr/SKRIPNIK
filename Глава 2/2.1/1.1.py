import numpy as np

a=np.array([[2.3, 5.1, 4.7],
            [3.5, 6.7, 1.5],
            [8.4, 3.1, 9.2]])

b=np.array([[4.3, 8.1, 0.1],
            [3.7, 6.2, 1.5],
            [2.4, 5.7, 4.7]])
string,column=a.shape
string_1,column_1=b.shape
cos_a=np.cos(a)
sin_b=np.sin(b)

print("Массив а содержит", string, "строк и", column, "столбцов.")
print("Массив b содержит", string_1, "строк и", column_1, "столбцов.", end="\n"*2)

print(a+b, end="\n"*2)
print(a-b, end="\n"*2)
print(a*b, end="\n"*2)
print(a/b, end="\n"*2)

print(pow(a,2),end="\n"*2)


print(b/2,end="\n"*2)


print("cos a:", cos_a,end="\n"*2)
print("sin b:", sin_b,end="\n"*2)
print(cos_a+sin_b)
import numpy as np

a=np.array([[2.3, 5.1, 4.7],
            [3.5, 6.7, 1.5],
            [8.4, 3.1, 9.2]])

b=np.array([[4.3, 8.1, 0.1],
            [3.7, 6.2, 1.5],
            [2.4, 5.7, 4.7]])
            
aq = np.array([1.2, 2.4, 3.0, 3.5, 6.7, 1.5, 8.4, 3.1, 9.2])

print("1")
print(a.shape,end="\n"*2)

print("2")
arr_1=a.reshape((9, 1))
print(arr_1,end="\n"*2)

print("3")
arr_2=a.reshape((3, 3))
print(arr_2,end="\n"*2)

print("4")
print(arr_2.max(axis=0),end="\n"*2)
print(arr_2.max(axis=1),end="\n"*2)

print("5")
print(arr_2.max(axis=0),end="\n"*2)
print(arr_2.max(axis=1),end="\n"*2)

print("6")
print(arr_2.sum(axis=0),end="\n"*2)
print(arr_2.sum(axis=1),end="\n"*2)




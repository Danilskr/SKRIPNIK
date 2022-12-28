import numpy as np
a = np.array([[4, 2], [9, 1]])
b = np.array([[5, 3], [2, 5]])

print("задание 1")
na_1 = np.vstack((a, b))
print(na_1)

print("задание 2")
a_2 = na_1[:,0][0:3]
print(a_2)

print("задание 3")
print(a_2.sum())
print(a_2.min())
print(a_2.max())

print("задание 4")
na_2 = np.hstack((a, b))
print(na_2)

print("задание 5")
print(na_2[0,:][0:3])

print("задание 6")
print(sum(na_2[0,:][0:3]))
print(max(na_2[0,:][0:3]))
print(min(na_2[0,:][0:3]))




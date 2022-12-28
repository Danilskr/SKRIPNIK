import numpy as np
from numpy import linalg as lg

a = np.array([[2, 8],
              [1, -6]])

b = np.array([[3, 2, 7],
             [4, 1, 8],
             [6, 3, 7]])

c = np.array([[4, 3, 2, 7],
             [6, 1, 1, -2],
             [7, 5, 8, 1],
             [9, 5, -3, -5]])

print("задание 1")
print(a.transpose(),end="\n"*2)
print(b.transpose(),end="\n"*2)
print(c.transpose(),end="\n"*2)

print("задание 2")
print(lg.inv(a),end="\n"*2)
print(lg.inv(b),end="\n"*2)
print(lg.inv(c),end="\n"*2)

print("задание 3")
axis0 = np.split(b, 3, axis=0)
print(lg.norm(axis0),end="\n"*2)
import numpy as np
from numpy import linalg as lg

a = np.array([[5, 4],[2, -6]])
b = np.array([14, -2])
ex =lg.solve(a,b)
print(ex)
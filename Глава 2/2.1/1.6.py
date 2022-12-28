import numpy as np
import random

a = np.array([random.randint(0, 100) for i in range(0, 100, 1)])
print(a)

count = 0
for i in a:
     if i>50:
        count+=1
print (count)

cn = 0
cn = sum(map(lambda item: item > 50, a))
print(cn)
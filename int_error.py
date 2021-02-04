import numpy as np

n = np.int16(0)
while n >= 0:
    previousVal = n
    n = n + np.int16(1)
print(previousVal)

n = np.int32(0)
while n >= 0:
    n = n + np.int32(10000)
while n < 0:
    n = n - np.int32(1)
print(n)

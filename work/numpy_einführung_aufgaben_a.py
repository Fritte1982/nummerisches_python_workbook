import numpy as np

v = np.arange(7)
print(type(v))
# v = v[1:: 2]
v = v[::-1]
print(v)
m = np.arange(12).reshape(4, 3)
print(m)
m = m[1: -1, 1: -1]
print(m)
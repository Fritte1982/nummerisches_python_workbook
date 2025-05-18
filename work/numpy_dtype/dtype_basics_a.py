import numpy as np

Pixel = np.dtype(np.uint8)
print(Pixel)

lst = [ [115, 230.9, 229.2, 234],
[117, 229, 232.1, 235],
[116, 140, 141, 142] ]

A = np.array(lst, dtype=Pixel)
print(A)

Density = np.dtype([("density", np.int32)])
x = np.array([(393,), (337,), (256,)], dtype=Density)




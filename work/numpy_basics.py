import numpy as np , time
from icecream import ic
from matplotlib import pyplot as plt

cvalues = [20.1, 20.8, 21.9, 22.5, 22.7,
21.8, 21.3, 20.9, 20.1]

C = np.array(cvalues)
ic(C, type(C))
ic(C*9/5+32)

# plt.plot(C)
# plt.show()

from sys import getsizeof as size
lst = [24, 12, 57]
size_of_list_object = size(lst) # only green box
size_of_elements = len(lst) * size(lst[0]) # 24, 12, 57
total_list_size = size_of_list_object + size_of_elements
print("Größe ohne Größe der Elemente: ", size_of_list_object)
print("Größe aller Elemente: ", size_of_elements)
print("Gesamtgröße der Liste: ", total_list_size)


size_of_vec = 10000
def pure_python_version():
    t1 = time.perf_counter()
    X = range(size_of_vec)
    Y = range(size_of_vec)
    Z = [X[i] + Y[i] for i in range(len(X))]
    return time.perf_counter() - t1

def numpy_version():
    t1 = time.perf_counter()
    X = np.arange(size_of_vec)
    Y = np.arange(size_of_vec)
    Z = X + Y
    return time.perf_counter() - t1

t1 =pure_python_version()
t2 = numpy_version()
ic(t1, t2)
print("NumPy is in this example " + str(t1/t2) + " faster!")

import numpy as np

b = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
            [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])

ic(b)

ic(b[0:2,1,:])

b = np.arange(4 * 5 * 6).reshape(4, 5, 6)
ic(b)
import numpy as np
ic(b[2][b[2] > 2])
# ic ( np.array([b[i].diagonal() for i in range(b.shape[0])]))

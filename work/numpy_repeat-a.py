import numpy as np
import matplotlib.pyplot as plt
from icecream import ic

cvalues = [20.1, 20.8, 21.9, 22.5, 22.7,
           21.8, 21.3, 20.9, 20.1]
C = np.array(cvalues)

fvalues = [x * 9 / 5 + 32 for x in cvalues]  # umrechnung in Fahrenheit

# plt.plot(C)
# plt.show()


""" arange([start,] stop[, step], [, dtype=None])"""
a = np.arange(1, 7)
ic(a)
# im Vergleich dazu nun range:
x = range(1, 7)
ic(x)  # x ist ein Iterator
ic(list(x))

x = np.arange(0.5, 6.1, 0.8, int)
ic(x)

"""linspace(start, stop, num=50, endpoint=True, retstep=False)"""
# 50 Werte (Default) zwischen 1 und 10:
print(np.linspace(1, 10))
# 7 Werte zwischen 1 und 10:
print(np.linspace(1, 10, 7))
# jetzt ohne Endpunkt:
print(np.linspace(1, 10, 7, endpoint=False))
"""Falls der Parameter ’retstep’ gesetzt ist, wird die Funktion auch den Wert des Abstands zwischen zwei benachbarten 
Werten des Ausgabearrays zurückliefern. Die Funktion liefert also ein Tupel (’samp￾les’, ’step’) zurück:
"""
samples_, spacing = np.linspace(1, 10, retstep=True)
print(spacing)
samples, spacing = np.linspace(1, 10, 5, endpoint=True, retstep=True)
print(samples, spacing)
samples, spacing = np.linspace(1, 10, 5, endpoint=False, retstep=True)
print(samples, spacing)

# Daten
B = np.array([
    [[111, 112], [121, 122]],
    [[211, 212], [221, 222]],
    [[311, 312], [321, 322]]
])
print(B[0][1][0])
print(B[0, 1, 0])  # besser

A = np.array([
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55]
])
print(A[:3, 2:])
print(A[3:, :])
print(A[:, 4:])

X = np.arange(28).reshape(4, 7)
print(X)
print(X[::2, ::3])
print(X[::, ::3])

A = np.array([
    [[45, 12, 4], [45, 13, 5], [46, 12, 6]],
    [[46, 14, 4], [45, 14, 5], [46, 11, 5]],
    [[47, 13, 2], [48, 15, 5], [52, 15, 1]]
])

print(A[1:3, 0:2])  # equivalent to A[1:3, 0:2, :]
print(A[1:3, 0:2].shape)

A = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
B1 = A[::2]
B2 = A[1::2]
print(np.may_share_memory(B1, B2))

X = np.array([
    [[3, 1, 2],
     [4, 2, 2]],
    [[-1, 0, 1],
     [1, -1, -2]],
    [[3, 2, 2],
     [4, 4, 3]],
    [[2, 2, 1],
     [3, 1, 3]]
])
print(X.shape)
print("Dimension 0 with size ", X.shape[0])
for i in range(X.shape[0]):
    print(X[i, :, :])

print("\nDimension 1 with size ", X.shape[1])
for i in range(X.shape[1]):
    print(X[:,i,:])

print("\nDimension 2 with size ", X.shape[2])
for i in range(X.shape[2]):
    print(X[:, :, 1])

x = np.array([2, 5, 18, 14, 4])
E = np.ones_like(x)
print(E)
Z = np.zeros_like(x)
print(Z)

v = np.arange(7)
ungerade_ind = v[1::2]
print(v)
print(ungerade_ind)
v = v[::-1]
print(v)
print()
m = np.arange(12).reshape(4,3 )
print(m)
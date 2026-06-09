import numpy as np
import lu_decomp as lu

A = np.array([[1., 1.,  3.],
               [1.,  2.,  2.],
               [2.,  1.,  5.]])
b = np.array([2., 1., 1.])
n = len(b)
P = np.linspace(0, n-1, n, dtype=int)

lu.lu_decomp(A, P, pivot=True)
print("Decomposed Matrix:")
print(A)
lu.forwards_sub(A, P, b)
print("After forwards subs:")
print(A)
print(b)
lu.backwards_sub(A, P, b)
print("Solved:")
print(A)
print(b)
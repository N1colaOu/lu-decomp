from numpy import array, linspace
import lu_decomp as lu

A = array([[1., 1.,  3.],
               [1.,  2.,  2.],
               [2.,  1.,  5.]])
b = array([2., 1., 1.])
n = len(A)
P = linspace(0, n-1, n, dtype=int)
lu.part_lu_decomp(A, n, P, pivot=False)
print(P)
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
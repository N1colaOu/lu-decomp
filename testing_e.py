from numpy import array, linspace
import lu_decomp as lu

A = array([[0., 1.,  3.],#problem because 0 is a leading element
               [1.,  2.,  2.],
               [2.,  1.,  5.]])
b = array([2., 1., 1.])
n = len(b)
P = linspace(0, n-1, n, dtype=int)

lu.lu_decomp(A, P, pivot=False)
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
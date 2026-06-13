from numpy import array, linspace
import lu_decomp as lu

A = array([[1., 1.,  3.],
               [1.,  2.,  2.],
               [2.,  1.,  5.]])
b = array([2., 1., 1.])
n = len(A)

(A, P) = lu.lu_decomp(A, pivot=True)
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
from numpy import array, linspace
import lu_decomp as lu

A = array([[0., 1.,  3.],#problem because 0 is a leading element
               [1.,  2.,  2.],
               [2.,  1.,  5.]])
b = array([2., 1., 1.])
n = len(b)

(A, P) = lu.lu_decomp(A, pivot=False)
print("Decomposed Matrix:")
print(A)
x = lu.forwards_sub(A, P, b)
lu.backwards_sub(A, x)
print("Solved:")
print(x)
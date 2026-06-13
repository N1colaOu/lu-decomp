import lu_decomp as l_u
from scipy.linalg import lu_factor, lu_solve
from numpy.random import rand
from numpy import linspace, copy
import error as err
import time as time

n = 100
A1 = rand(n, n)
A2 = copy(A1)
A3 = copy(A1)
b1 = rand(n)
b2 = copy(b1)
b3 = copy(b1)

time_scipy = time.time()
lu, piv = lu_factor(A1)
x_scipy = lu_solve((lu, piv), b1)
time_scipy -= time.time()
time_scipy *= -1

time_mine = time.time()
(A2, P2) = l_u.lu_decomp(A2)
l_u.forwards_sub(A2, P2, b2)
l_u.backwards_sub(A2, P2, b2)
time_mine -= time.time()
time_mine *= -1

time_part = time.time()
P3 = linspace(0, n-1, n, dtype=int)
l_u.part_lu_decomp(A3, n, P3, pivot=True)
l_u.forwards_sub(A3, P3, b3)
l_u.backwards_sub(A3, P3, b3)
time_part -= time.time()
time_part *= -1

x_exact = [1]*n

err_mine = err.get_error(A1, x_exact)
err_scipy = err.get_error(A2, x_exact)
err_part = err.get_error(A3, x_exact)

print(f'Error mine: {err_mine}')
print(f'Error partitioned: {err_part}')
print(f'Error scipy: {err_scipy}')

print(f'Time mine: {time_mine}')
print(f'Time partitioned: {time_part}')
print(f'Time scipy: {time_scipy}')

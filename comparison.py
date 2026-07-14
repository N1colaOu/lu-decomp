import lu_decomp as l_u
from scipy.linalg import lu_factor, lu_solve
from numpy.random import rand
from numpy import linspace, copy, abs
import error as err
import time as time

n = 200
A1 = rand(n, n)
A2 = copy(A1) #three different matrices, because my methods edit them
A3 = copy(A1)
b1 = rand(n)

time_scipy = time.time()
lu, piv = lu_factor(A1)
x_scipy = lu_solve((lu, piv), b1)
time_scipy -= time.time()
time_scipy *= -1

time_mine = time.time()
(A2, P2) = l_u.lu_decomp(A2, pivot=True)
x_2 = l_u.forwards_sub(A2, P2, b1)
l_u.backwards_sub(A2, x_2)
time_mine -= time.time()
time_mine *= -1

time_part = time.time()
P3 = linspace(0, n-1, n, dtype=int)
l_u.part_lu_decomp(A3, n, P3, pivot=True)
x_3 = l_u.forwards_sub(A3, P3, b1)
l_u.backwards_sub(A3, x_3)
time_part -= time.time()
time_part *= -1


print(f'Time mine: {time_mine}')
print(f'Time partitioned: {time_part}')
print(f'Time scipy: {time_scipy}')

print(f'Diff between scipy and mine / scipy and partitioned: {err.get_norm_2(x_scipy-x_2)} , {err.get_norm_2(x_scipy-x_3)}') #difference in answers

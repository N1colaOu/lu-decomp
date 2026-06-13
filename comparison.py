import lu_decomp as l_u
from scipy.linalg import lu_factor, lu_solve
from numpy.random import rand
import error as err
import time as time
from multiprocessing import Pool

n = 30
A = rand(n, n)
b = rand(n)

time_mine = time.time()
x_mine = l_u.solve(A, b)
time_mine -= time.time()
time_mine *= -1

time_scipy = time.time()
lu, piv = lu_factor(A)
x_scipy = lu_solve((lu, piv), b)
time_scipy -= time.time()
time_scipy *= -1

x_noise = [1]*n

err_mine = err.get_error(A, x_noise)
err_scipy = err.get_error(lu, x_noise)

print(f'Difference in errors: {err_mine-err_scipy}')
print(f'Time mine: {time_mine}')
print(f'Time scipy: {time_scipy}')

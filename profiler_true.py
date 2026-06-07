import lu_decomp
import numpy as np


n = 100
A = np.random.uniform(-1, 1, (n, n)).astype(np.float64)
P = np.linspace(0, n-1, n, dtype=int)
lu_decomp.lu_decomp(A, P, True)
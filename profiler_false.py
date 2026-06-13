import lu_decomp
import numpy as np


n = 100
A = np.random.uniform(-1, 1, (n, n)).astype(np.float64)
(A, P) = lu_decomp.lu_decomp(A, False)
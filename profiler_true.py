import lu_decomp
import numpy as np


n = 300
A = np.random.rand(n, n)
(A, P) = lu_decomp.lu_decomp(A, True)
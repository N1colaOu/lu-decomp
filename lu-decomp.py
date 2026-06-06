import numpy as np

def lu_decomp(A, P, pivot = False):    

    n = len(A)
    for i in range(n):
        for j in range(i+1, n):
            A[j, i] /= A[i, i] # we setup the L part
            for k in range(i+1, n):
                A[j, k] -= A[j,i]*A[i, k]  # we setup the U part

def switch_rows():
    pass
def pivot():
    pass



_A = np.array([[1, 1, 3], [1, 2, 2], [2, 1, 5]])
lu_decomp(_A, 1, pivot=False)
print(_A)

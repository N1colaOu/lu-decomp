import numpy as np

def lu_decomp(A, P, pivot = False):    

    n = len(A)
    for i in range(n):
        if pivot:
            pivot_(P, A, i)
        for j in range(i+1, n):
            #here we pivot
            A[j, i] /= A[i, i] # we setup the L part
            for k in range(i+1, n):
                A[j, k] -= A[j,i]*A[i, k]  # we setup the U part

def switch_rows(A, i, j):
    temp = np.copy(A[i,:])
    A[i,:] = A[j,:]
    A[j,:] = temp
def pivot_(P, A, i):
    n = len(A)
    max_idx = i
    for k in range(i+1, n):
        if np.abs(A[max_idx, i]) <= np.abs(A[k, i]):
            max_idx = k
    if max_idx != i:
        switch_rows(A, i, max_idx)
        P[i] = max_idx
        P[max_idx] = i



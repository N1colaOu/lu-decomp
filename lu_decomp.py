from numpy import linspace, abs, copy

def lu_decomp(A, pivot = False):    
    n = len(A)
    P = linspace(0, n-1, n, dtype=int)
    for i in range(n):
        if pivot:
            #here we pivot
            find_and_pivot(A, P, i)
        for j in range(i+1, n):
            A[j, i] /= A[i, i] # we setup the L part
            for k in range(i+1, n):
                A[j, k] -= A[j,i]*A[i, k]  # we setup the U part
    return A, P

def switch_rows(A, i, j):
    temp = copy(A[i,:])
    A[i,:] = A[j,:]
    A[j,:] = temp
    
def find_and_pivot(A, P, i):
    n = len(A)
    max_idx = i
    for k in range(i+1, n):
        if abs(A[max_idx, i]) <= abs(A[k, i]):
            max_idx = k
    if max_idx != i:
        switch_rows(A, i, max_idx)
        temp = P[i]
        P[i] = P[max_idx]
        P[max_idx] = temp

def forwards_sub(L, P, b):
    n = len(b)

    for i in range(n):
        perm = P[i]
        if perm != i:
            temp = b[i]#switch b if we have to
            b[i] = b[perm]
            b[perm] = temp

            temp = P[i]#switch P to not switc twice later
            P[i] = P[perm]
            P[perm] = temp

    for i in range(n):
        for j in range(i+1, n):
            b[j] -= L[j, i]*b[i]
            L[j, i] = 0.00


def backwards_sub(R, P, b):
    n = len(b)

    for i in range(n):
        perm = P[i]
        if perm != i:
            temp = b[i]#switch b if we have to
            b[i] = b[perm]
            b[perm] = temp

            temp = P[i]#switch P to not switc twice later
            P[i] = P[perm]
            P[perm] = temp

    for i in range(n-1, -1, -1):
        b[i] /= R[i, i]
        R[i, i] = 1.00
        for j in range(i-1, -1, -1):
            b[j] -= R[j, i]*b[i]
            R[j, i] = 0.00

def part_lu_decomp(A, n, P, k=0, pivot=False):
    if k < n-1:
        if pivot:
            find_and_pivot(A, P, k)
        for i in range(k+1, n):
            A[i, k] /= A[k, k]
            for j in range(k+1, n):
                A[i, j] -= A[i, k]*A[k, j]
        part_lu_decomp(A, n, P, k+1, pivot)
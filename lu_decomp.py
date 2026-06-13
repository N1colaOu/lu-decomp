from numpy import linspace, abs, copy
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
    temp = copy(A[i,:])
    A[i,:] = A[j,:]
    A[j,:] = temp
def pivot_(P, A, i):
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

def solve(A, b):
    n = len(A)
    P = linspace(0, n-1, n, dtype=int)
    lu_decomp(A, P, pivot=True)
    forwards_sub(A, P, b)
    backwards_sub(A, P, b)
    return b

def part_lu_decomp(A, n, k = 0):
    if k < n-1:
        c = A[k, k]
        for i in range(k+1, n):
            A[i, k] /= c
        for i in range(k+1, n):
            for j in range(k+1, n):
                A[i, j] -= A[i, k]*A[k, j]
        part_lu_decomp(A, n, k+1)

import numpy as np
import lu_decomp as lu


def get_error(A, x_exact, pivot):
    b = np.matmul(A, x_exact) #we get b
    n = len(A)

    (A, P) = lu.lu_decomp(A, pivot=pivot)
    x = lu.forwards_sub(A, P, b)
    lu.backwards_sub(A, x)
    err = get_norm_2(x-x_exact)/get_norm_2(x_exact)
    return err

def get_norm_2(v):
    sum = 0.00 
    for i in v:
        sum += i**2
    return np.sqrt(sum)


import numpy as np
import lu_decomp as lu


def get_error(A, x_noise):
    b = np.matmul(A, x_noise)
    n = len(A)

    (A, P) = lu.lu_decomp(A, pivot=False)
    lu.forwards_sub(A, P, b)
    lu.backwards_sub(A, P, b)
    err = get_norm_2(b-x_noise)/get_norm_2(x_noise)
    return err

def get_norm_2(v):
    sum = 0.00 
    for i in v:
        sum += i**2
    return np.sqrt(sum)


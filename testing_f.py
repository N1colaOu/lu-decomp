from numpy import linspace, power, abs, zeros
import lu_decomp as lu
import error as err
import matplotlib.pyplot as plt
n_arr = linspace(2, 20, 19, dtype=int)
err_1 = []
err_hilbert = []
for n in n_arr:
    x_noise = [1]*n
    A1 = zeros([n, n])
    for i in range(n):
        for j in range(n):
            A1[i, n-j-1] = power(1/3, abs(i-j)) + power(1/2, j+i) + 10e-10

    Ah = zeros([n, n])
    for i in range(n):
        for j in range(n):
            Ah[i, j] = 1/(i+j+1)
    
    err_1.append(err.get_error(A1, x_noise))
    err_hilbert.append(err.get_error(Ah, x_noise))

plt.figure(1)
plt.semilogy(n_arr, err_1, label="Matrix 1")
plt.title("Error of Matrix 1: Log plot")
plt.grid()
plt.savefig('./build/error_1.png')

plt.figure(2)
plt.semilogy(n_arr, err_hilbert, label="Hilbert Matrix")
plt.title("Error of Hilbert Matrix: Log plot")
plt.grid()
plt.savefig('./build/error_hilbert.png')

plt.figure(3)
plt.semilogy(n_arr, err_1, label="Matrix 1")
plt.semilogy(n_arr, err_hilbert, label="Hilbert Matrix")
plt.title("Comparison of the Errors: Log Plot")
plt.legend()
plt.grid()
plt.savefig('./build/error_comp.png')
    
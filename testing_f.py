from numpy import linspace, power, abs, zeros
import lu_decomp as lu
import error as err
import matplotlib.pyplot as plt

n_arr = linspace(2, 20, 19, dtype=int)
err_1_with = []
err_1_without = []
err_hilbert_with = []
err_hilbert_without = []
for n in n_arr:
    x_noise = [1]*n
    A1 = zeros([n, n])
    for i in range(1, n+1):
        for j in range(1, n+1):
            A1[i-1, n-j] = power(1/3, abs(i-j)) + power(1/2, j+i) + 10e-10

    Ah = zeros([n, n])
    for i in range(1, n+1):
        for j in range(1, n+1):
            Ah[i-1, j-1] = 1/(i+j+1)
    
    err_1_with.append(err.get_error(A1, x_noise, True))
    err_1_without.append(err.get_error(A1, x_noise, False))
    err_hilbert_with.append(err.get_error(Ah, x_noise, True))
    err_hilbert_without.append(err.get_error(Ah, x_noise, False))


plt.figure(1)
plt.semilogy(n_arr, err_1_with, label="Matrix 1 With")
plt.semilogy(n_arr, err_1_without, label="Matrix 1 Without")
plt.title("Error of Matrix 1: Log plot")
plt.grid()
plt.legend()
plt.savefig('./build/error_1.png')

plt.figure(2)
plt.semilogy(n_arr, err_hilbert_with, label="Hilbert Matrix With")
plt.semilogy(n_arr, err_hilbert_without, label="Hilbert Matrix Without")
plt.title("Error of Hilbert Matrix: Log plot")
plt.grid()
plt.legend()
plt.savefig('./build/error_hilbert.png')

plt.figure(3)
plt.semilogy(n_arr, err_1_with, label="Matrix 1 With")
plt.semilogy(n_arr, err_1_without, label="Matrix 1 Without")
plt.semilogy(n_arr, err_hilbert_with, label="Hilbert Matrix With")
plt.semilogy(n_arr, err_hilbert_without, label="Hilbert Matrix Without")
plt.title("Comparison of the Errors: Log Plot")
plt.legend()
plt.grid()
plt.savefig('./build/error_comp.png')
    
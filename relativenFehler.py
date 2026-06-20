import numpy as np
import matplotlib.pyplot as plt

# 1) Hilfsfunktionen zum Generieren der Matrizen 
def generate_matrix_i(n):
    A = np.zeros((n, n))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Achtung: Index-Verschiebung für Python (startet bei 0)
            # A_{i, n-j+1} entspricht in Python A[i-1, n-j]
            A[i-1, n-j] = 3**(-abs(i-j)) + 2**(-j-i) + 10**(-10)
    return A

def generate_hilbert(n):
    A = np.zeros((n, n))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            A[i-1, j-1] = 1.0 / (i + j - 1)
    return A

# 2) Vorbereitung der Listen für den Plot
sizes = range(2, 21)
err_m1_no_piv, err_m1_piv = [], []
err_m2_no_piv, err_m2_piv = [], []

# 3) Die Hauptschleife über alle Matrixgrößen 
for n in sizes:
    x_ex = np.ones(n)

    # Matrix i) testen
    A1 = generate_matrix_i(n)
    b1 = np.dot(A1, x_ex)
    
    # Ohne Pivot
    A_temp = A1.copy()
    P_temp = np.arange(n)
    A_lu, P_res = lu_decomposition(A_temp, P_temp, pivot=False)
    x_calc = solve_lu(A_lu, P_res, b1)
    err = np.linalg.norm(x_calc - x_ex) / np.linalg.norm(x_ex)
    err_m1_no_piv.append(err)
    
    # Mit Pivot
    A_temp = A1.copy()
    P_temp = np.arange(n)
    A_lu, P_res = lu_decomposition(A_temp, P_temp, pivot=True)
    x_calc = solve_lu(A_lu, P_res, b1)
    err = np.linalg.norm(x_calc - x_ex) / np.linalg.norm(x_ex)
    err_m1_piv.append(err)

    # Matrix ii) (Hilbert) testen
    A2 = generate_hilbert(n)
    b2 = np.dot(A2, x_ex)
    
    # Ohne Pivot
    A_temp = A2.copy()
    P_temp = np.arange(n)
    A_lu, P_res = lu_decomposition(A_temp, P_temp, pivot=False)
    x_calc = solve_lu(A_lu, P_res, b2)
    err = np.linalg.norm(x_calc - x_ex) / np.linalg.norm(x_ex)
    err_m2_no_piv.append(err)
    
    # Mit Pivot
    A_temp = A2.copy()
    P_temp = np.arange(n)
    A_lu, P_res = lu_decomposition(A_temp, P_temp, pivot=True)
    x_calc = solve_lu(A_lu, P_res, b2)
    err = np.linalg.norm(x_calc - x_ex) / np.linalg.norm(x_ex)
    err_m2_piv.append(err)

# 4) Plotten der Ergebnisse 
plt.figure(figsize=(10, 6))
plt.plot(sizes, err_m1_no_piv, label='Matrix i) - Ohne Pivot', marker='o')
plt.plot(sizes, err_m1_piv, label='Matrix i) - Mit Pivot', marker='x')
plt.plot(sizes, err_m2_no_piv, label='Hilbert - Ohne Pivot', marker='s')
plt.plot(sizes, err_m2_piv, label='Hilbert - Mit Pivot', marker='^')

plt.yscale('log')
plt.xlabel('Matrixgröße n')
plt.ylabel('Relativer Fehler')
plt.title('Relativer Fehler der LR-Zerlegung')
plt.legend()
plt.grid(True)
plt.show()


# Matrix i) (Strukturelles Problem): Ohne Pivotisierung ist der Fehler bei dieser Matrix gigantisch.
# Das liegt daran, dass durch die Konstruktion (n-j+1) die betragsmäßig größten Elemente auf der Nebendiagonale 
# (rechts oben nach links unten) liegen. 
# Auf der Hauptdiagonale liegen extrem kleine Zahlen (10^{-10}). 
# Ohne Pivotisierung teilt der Algorithmus durch diese winzigen Zahlen, was zu einem numerischen Kollaps führt. 
# Mit Pivotisierung verschwindet das Problem völlig.  
# Matrix ii) (Die Hilbert-Matrix): Hier wächst der Fehler exponentiell an (die Kurve schießt nach oben), 
# sowohl mit als auch ohne Pivotisierung. 
# Die ausschlaggebende Eigenschaft hierfür ist die Konditionszahl (Condition Number) der Matrix. 
# Die Hilbert-Matrix ist extrem "schlecht konditioniert" (ill-conditioned). Das bedeutet, dass schon winzige Rundungsfehler in der Fließkomma-Arithmetik des Computers zu massiven Änderungen in der Lösung führen. 
#Da kann auch die beste Pivotisierung nichts mehr retten, da das Problem in der Matrix selbst liegt, nicht im Algorithmus.

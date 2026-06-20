import numpy as np

# Vorbereitung der gegebenen Daten
A = np.array([[1.0, 1.0, 3.0],
              [1.0, 2.0, 2.0],
              [2.0, 1.0, 5.0]])

b = np.array([2.0, 1.0, 1.0])

# TEST 1: Ohne Pivotisierung
print(" Test: Ohne Pivotisierung ")
A_test1 = A.copy()
P_test1 = np.arange(len(A))  # Erstellt den Vektor [0, 1, 2]

A_res1, P_res1 = lu_decomposition(A_test1, P_test1, pivot=False)
x1 = solve_lu(A_res1, P_res1, b)

print("Kombinierte LU-Matrix:\n", A_res1)
print("Lösung x:\n", x1)

# TEST 2: Mit Pivotisierung
print("\n Test: Mit Pivotisierung ")
A_test2 = A.copy()
P_test2 = np.arange(len(A))  # Erstellt den Vektor [0, 1, 2]

A_res2, P_res2 = lu_decomposition(A_test2, P_test2, pivot=True)
x2 = solve_lu(A_res2, P_res2, b)

print("Kombinierte LU-Matrix:\n", A_res2)
print("Permutationsvektor P:\n", P_res2)
print("Lösung x:\n", x2)


# e) Die Beispielmatrix: A = (0 & 1 \\ 1 & 0)
# Warum schlägt die Zerlegung ohne Pivotisierung hier fehl?
# Sie ist invertierbar: Die Determinante der Matrix ist -1 (also ungleich 0).
# Der Absturz: Ohne Pivotisierung versucht unser Code im allerersten Schritt, den Faktor für die untere Zeile zu berechnen (L_{21} = \frac{A_{21}}{A_{11}}).
# Division durch Null: Da A_{11} = 0 ist, rechnet der Computer \frac{1}{0}. Das führt sofort zu einem Programmabsturz.Mit Pivotisierung würde der Algorithmus einfach die beiden Zeilen tauschen und problemlos weiterrechnen.

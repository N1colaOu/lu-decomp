import numpy as np

def solve_lu(A, P, b): # die Funktion nimmt in-place überschriebene Matrix A und den Permutationsvektor P und die rechte Seite b 
    n = len(A) # Größe des Gleichungssystems
    y = np.zeros(n)
    x = np.zeros(n)
    # zwei mit Nullen gefüllten Vektoren 
    # y = x~ = Zwischenlösung speichern
    # x = finale Lösung speichern

    # 1) Permutation der rechten Seite
    b_perm = b[P] 
    
    # 2) Vorwärtssubstitution (L * y = b_perm) 
    for i in range(n):
        y[i] = b_perm[i] - np.dot(A[i, :i], y[:i])
        
    # 3) Rückwärtssubstitution (U * x = y) 
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
        
    return x

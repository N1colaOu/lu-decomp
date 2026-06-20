import numpy as np

def lu_decomposition(A, P, pivot=True):    #Pivotisierung standardmäßig eingeschaltet
    n = len(A) #Größe der Matrix bestimmen 
    
    for i in range(n): # äußere Hauptschleife - geht jede Spalte/Zeile auf der Diagonalen der Matrix
        # 1) pivotisierung
        if pivot:
            p = i + np.argmax(np.abs(A[i:n, i])) # wir suchen in der aktuellen Spalte i abwärts nach dem Element mit dem größten Betrag (np.abs) und (np.argmax) gibt uns die Position dieses Maximums (ich verstehe nicht warum wir i dazuaddieren?)
            
            if i != p: # wenn das gefundene größte Element nicht ohnehin schon auf der aktuellen Diagonalposition ist, müssen wir tauschen  
                A[[i, p]] = A[[p, i]]  # Zeile i und Zeile p komplett miteienander vertauschen 
                P[i], P[p] = P[p], P[i]  # gleichzeitig vertauschen wir die Einträge in dem Permutationsvektor P
                
        #  2) LR-zerlegung (In-Place)
        for j in range(i + 1, n):  # alle Zeilen unterhalb des aktuellen Diagonalelements durchgehen 
            A[j, i] = A[j, i] / A[i, i]  # wir speichern das Ergebnis im unteren Teil der Matrix A 
            
            for k in range(i + 1, n): # restliche "Restmatrix" rechts unten anpassen 
                A[j, k] = A[j, k] - A[j, i] * A[i, k] # restlichen Einträge überschreiben 
                
    return A, P # modifizierte Matrix und vertauschten Vektor zurückgeben

# Teuerster Teil: Der rechenintensivste Abschnitt ist die Aktualisierung der Restmatrix (
# die Berechnung der vorläufigen U-Matrix-Einträge U_{jk}=A_{jk}-L_{ji}A_{ik}).
# Da dies in der dreifach verschachtelten innersten Schleife passiert, skaliert der Aufwand mit n^3
# und benötigt die meiste Rechenzeit.

# Speicherzugriffe (Cache-Effizienz): Um Verzögerungen beim Datenabruf aus dem RAM zu vermeiden, 
# muss die innerste Schleife die Elemente exakt in der Reihenfolge abarbeiten, in der sie im Speicher liegen. 
# Python/NumPy legt Matrizen zeilenweise im Speicher ab (Row-Major), weshalb die innerste Schleife über 
# die Spalten einer Zeile laufen muss. In Julia liegen Matrizen spaltenweise (Column-Major) vor, 
# weshalb die innerste Schleife dort über die Zeilen einer Spalte laufen sollte.

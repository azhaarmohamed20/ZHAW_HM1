import timeit

import numpy as np
import matplotlib.pyplot as plt

def fact_rec(n):
    # y = fact_rec(n) berechnet die Fakultät von n als fact_rec(n) = n * fact_rec(n -1) mit fact_rec(0) = 1
    # Fehler, falls n < 0 oder nicht ganzzahlig
    if n < 0 or np.trunc(n) != n:
        raise Exception('The factorial is defined only for positive integers')
    if n <=1:
        return 1
    else:
        return n*fact_rec(n-1)

def fact_for(n):
    result = n;
    for i in reversed(range(1, n)):
        result = result * i 
    return result

t1=timeit.repeat("fact_rec(500)", "from __main__ import fact_rec", number=100)
t2=timeit.repeat("fact_for(500)", "from __main__ import fact_for", number=100)

print("Faktorial Rekursiv: ", np.mean(t1))
print("Faktorial Schleife: ", np.mean(t2))
print("Faktor ", np.mean(t1) / np.mean(t2)) 

"""
Welche der beiden Funktionen ist schneller und um was für einen Faktor? Weshalb?

Die fact_for Methode ist um den Faktor 2 schneller als die rekursive Implementation. Der Grund dafür ist, dass bei der rekursiven Funktion für jeden Schritt nochmals die Funktion aufgerufen und ausgeführt wird. Diese vielen Funktionsaufrufen verursachen ein zusätzlichen Zeitaufwand. Bei der Schleifen Implementation wird direkt nacheinander multipliziert, dadurch entsteht weniger Aufwand.

Gibt es in Python eine obere Grenze für die Fakultät von n
    1. als ganze Zahl (vom Typ 'integer')? Versuchen Sie hierzu, das Resultat für n ∈ [190, 200] als integer auszugeben.
        Die Fakultät von 190 bis 200 können ohne Probleme ausgegeben werden.
        Siehe ausgabe unten.

    2. als reelle Zahl (vom Typ 'float')? Versuchen Sie hierzu, das Resultat für n ∈ [170, 171] als float auszugeben.
        Wenn ich versuche die Fakultät als Float auszugeben kriege ich ab Fakultät 171 die Folgende Ausgabe: "OverflowError: int too large to convert to float"
    
"""

# 1 Integer
for i in range(190, 201):
    print(i, fact_for(i))


# 2
# for i in range(170, 172):
#     print(i, float(fact_for(i)))
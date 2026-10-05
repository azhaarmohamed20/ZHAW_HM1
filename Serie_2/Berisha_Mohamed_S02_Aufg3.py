import math
import numpy as np
import matplotlib.pyplot as plt


def umfang_annaeherung(n, s):
    return 2 * n * seitenlaenge(s);

def seitenlaenge(s):
    return math.sqrt(2 - 2 * (math.sqrt(1 - s ** 2 / 4 )))

# Aufgabe 3a
n = 6
s = 1.0;
x_werte = []
y_werte = []

for _ in range(100):
    x_werte.append(2 * n)
    y_werte.append(umfang_annaeherung(n, s))

    s = seitenlaenge(s)
    n = 2 * n

plt.figure(1)
plt.plot(x_werte, y_werte, "o-", label="Umfang-Approximation")
plt.axhline(2 * math.pi, color="red", label="Umfang 2π")
plt.xlabel("Anzahl der Ecken")
plt.ylabel("Umfang Approximation")
plt.xscale("log")
plt.xlim(-10, 10 ** 15)
plt.ylim(-0.5, 13)
plt.legend()
plt.grid()

"""
Was passiert für grosse n und weshalb?

Zuerst nähert sich der Umfang an 2pi an. Bei sehr grossen n wird die Seitenlänge aber so klein, dass Rundungsfehler die Berechnung stark beeinflussen. Dadurch weicht der Umfang ab und steigt kurz auf etwa 12. Sobald (1 - s**2/4) auf 1 gerundet wird, ergibt die Formel (sqrt(2 - 2) = 0). Deshalb fällt der Umfang auf 0 und bleibt dort.
"""

# Aufgabe 3b
def umfang_annaeherung_neueVariante(n, s):
    return 2 * n * seitenlaenge_neueVariante(s);

def seitenlaenge_neueVariante(s):
    return math.sqrt(s ** 2 / (2 * (1 + math.sqrt(1 - s ** 2/ 4))))

print(umfang_annaeherung_neueVariante(6, 1.0))

# Aufgabe 3a
n = 6
s = 1.0;
x_werte_neueVariante = []
y_werte_neueVariant = []

for _ in range(100):
    x_werte_neueVariante.append(2 * n)
    y_werte_neueVariant.append(umfang_annaeherung_neueVariante(n, s))

    s = seitenlaenge_neueVariante(s)
    n = 2 * n

plt.figure(2)
plt.plot(x_werte_neueVariante,y_werte_neueVariant, "o-", label="Umfang-Approximation")
plt.axhline(2 * math.pi, color="red", label="Umfang 2π")
plt.xlabel("Anzahl der Ecken")
plt.ylabel("Umfang Approximation")
plt.xscale("log")
plt.legend()
plt.grid()
plt.show()


"""
Was lässt sich bei der neuen Variante beobachten?

Bei der neuen Variante bleibt der berechnete Umfang auch bei sehr grossen n nahe bei 2pi. Die Berechnung ist stabiler, weil nicht mehr zwei fast gleich grosse Zahlen voneinander abgezogen werden. Dadurch tritt das Problem mit den Rundungsfehlern aus Aufgabe 3a nicht mehr auf.
"""
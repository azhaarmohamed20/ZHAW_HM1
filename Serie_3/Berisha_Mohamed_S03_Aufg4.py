
import numpy as np
import matplotlib.pyplot as plt


def h(x):
    """Berechnet h(x) mit der ursprünglichen Formel."""
    return np.sqrt(100 * x**2 - 200 * x + 99)


def h_stabil(x):
    """Berechnet h(x) mit der umgeformten Formel."""
    return np.sqrt((10 * x - 9) * (10 * x - 11))


def kondition(x):
    """Berechnet die relative Konditionszahl von h(x)."""
    radicand = (10 * x - 9) * (10 * x - 11)
    return np.abs(100 * x * (x - 1) / radicand)


# Aufgabe 4a
# Bei x = 1.1 ergibt das Polynom:
# 100 * 1.1**2 - 200 * 1.1 + 99 = 121 - 220 + 99 = 0
#
# In der Nähe von 1.1 werden also relativ grosse Zahlen
# voneinander abgezogen, obwohl das Ergebnis sehr klein ist.
# Dabei können durch Rundungsfehler wichtige Stellen verloren gehen.
# Das nennt man Auslöschung.
#
# Zum Vergleich berechnen wir h(x) mit beiden Formeln.

x_near = np.array([
    1.1,
    1.1 + 1e-14,
    1.1 + 1e-12,
    1.1 + 1e-10
])

print("Aufgabe 4a: Vergleich der Berechnungsmethoden\n")

for x in x_near:
    print(f"x = {x:.15f}")
    print(f"  h(x):        {h(x):.15e}")
    print(f"  h_stabil(x): {h_stabil(x):.15e}")
    print()


# Aufgabe 4b
# Die relative Konditionszahl berechnen wir mit:
# kappa(x) = |x * h'(x) / h(x)|
#
# Mit der Ableitung von h(x) ergibt sich:
# kappa(x) = |100*x*(x-1) / ((10*x-9)*(10*x-11))|
#
# Wir verwenden die faktorisierte Form, damit bei der
# Berechnung nicht wieder die gleiche Auslöschung auftritt.
#
# Bei x = 1.1 ist die Kondition nicht definiert,
# deshalb starten wir einen Schritt danach.

delta_x = 1e-7

x_values = 1.1 + np.arange(1, 2_000_001) * delta_x
condition_values = kondition(x_values)

plt.figure(figsize=(10, 6))

plt.semilogy(
    x_values,
    condition_values,
    label=r"$\kappa_h(x)$"
)

plt.xlabel("x")
plt.ylabel(r"Relative Kondition $\kappa_h(x)$")
plt.title("Aufgabe 4b: Kondition von h(x)")

plt.grid(True, which="both")
plt.legend()
plt.tight_layout()

print("Aufgabe 4b:")
print(
    "Kondition bei x = 1.1 + 1e-7:",
    kondition(1.1 + delta_x)
)

plt.show()


# Aufgabe 4c
# Durch die Faktorisierung
#
# h(x) = sqrt((10*x - 9)*(10*x - 11))
#
# können wir die Auslöschung aus der ursprünglichen
# Berechnung grösstenteils vermeiden.
#
# Das Problem mit der Kondition bleibt aber bestehen.
# Wenn x gegen 1.1 geht, geht h(x) gegen 0 und die
# relative Konditionszahl wird immer grösser.
#
# Die Umformung hilft also bei der Berechnung,
# ändert aber nichts daran, dass die Funktion
# in der Nähe von x = 1.1 schlecht konditioniert ist.

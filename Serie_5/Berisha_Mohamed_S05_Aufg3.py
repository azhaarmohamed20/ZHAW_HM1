import numpy as np


# Sekanten Verfahren
def Berisha_Mohamed_S05_Aufg3(f, x0, x1, tol):
    for i in range(100):
        f0 = f(x0)
        f1 = f(x1)

        if f1 == f0:
            raise ValueError("Division durch Null nicht erlaubt")

        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)

        if abs(x2 - x1) < tol:
            return x2

        x0 = x1
        x1 = x2
    raise ValueError("Keine Konvergenz nach 100 Iterationen.")


"""
 Schwierigkeit beim Newton-Verfahren:
 Das Newton-Verfahren benötigt die Ableitung f'(x). Diese kann bei einer beliebigen Funktion f nicht ohne Weiteres automatisch berechnet werden. Deshalb müsste man die Ableitung zusätzlich übergeben oder numerisch approximieren.
"""


# Funktion von Aufgabe 1
def f1(x):
    return np.exp(x**2) + x ** (-3) - 10


# Funktion von Aufgabe 2
def f2(h):
    return (np.pi * h**2 / 3) * (15 - h) - 471


tol = 1e-3

y1 = Berisha_Mohamed_S05_Aufg3(f1, -1.0, -1.2, tol)
y2 = Berisha_Mohamed_S05_Aufg3(f1, 0.5, 0.6, tol)
y3 = Berisha_Mohamed_S05_Aufg3(f1, 1.7, 2.0, tol)
y4 = Berisha_Mohamed_S05_Aufg3(f2, 8.0, 9.0, tol)

print("Aufgabe 1:")
print("Nullstelle 1:", y1)
print("Nullstelle 2:", y2)
print("Nullstelle 3:", y3)

print("")
print("Aufgabe 2:")
print("Maximale Wasserhöhe:", y4, "m")

"""
 Kurze Notiz zu den von Hand berechneten und den python berechneten Ergebnissen:
 Die python berechneten Nullstellen stimmen näherungsweise mit den Ergebnissen
 aus Aufgabe 1 und 2 überein. Kleine Abweichungen entstehen, da in
 Aufgabe 1 nur vier Iterationen durchgeführt wurden.
"""

import numpy as np
import matplotlib.pyplot as plt

# Aufgabe 2a)

def f1(x):
    return x**7 - 14 * x**6 + 84 * x**5 - 280 * x**4 + 560 * x**3 - 672 * x**2 + 448 * x - 128


def f2(x):
    return (x - 2)**7

# print(f1(1))
# print(f2(1))

# f1 und f2 sind analytisch gleich, da f2(x) ausmultipiziert f1(x) entspricht.
# Die volle Rechnung dazu ist ersichtlich in der Datei Berisha_Mohamed_S02_Aufg2_Beweis.jpg

plt.figure(figsize=(10, 6))
points_exercise_a = np.linspace(1.99, 2.01, 501)
plt.plot(points_exercise_a, f1(points_exercise_a), label='f1(x)', color='blue')
plt.plot(points_exercise_a, f2(points_exercise_a), label='f2(x)', color='orange')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Comparison of f1(x) and f2(x)')
plt.xlabel('x')
plt.xlim(1.99, 2.01)
plt.yscale("symlog", linthresh=1e-15)
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()


# Der Grund dafür, warum die Funktionen analytisch identisch aber graphisch unterschiedlich sind, besteht darin
# dass in f2(x) zuerst die Different (x-2) berechnet wird und dann potenziert wird, während in f1(x) die Potenzierung zuerst durchgeführt wird.
# Dies führt dazu, dass bei f1(x) die Werte sehr klein werden, bevor sie subtrahiert werden, was zu einem Verlust an Genauigkeit führt.

# Aufgabe 2b)

def g(x):
    return x/(np.sin(1+x) - np.sin(1))

""" plt.figure(figsize=(10, 6))
points_exercise_b = np.arange(-10**-14, 10**-14, 10**-17)
plt.plot(points_exercise_b, g(points_exercise_b), label='g(x)', color='green')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Comparison of g(x)')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.xlim(-10**-14, 10**-14)
plt.yscale("symlog", linthresh=1e-15)
plt.legend()
plt.grid()
plt.show() """

# Die numerische Berechnung des Grenzwertes von g(x) für x gegen 0 ist problematisch, da die Funktion eine Form von 0/0 annimmt.
# Dies führt zu einer numerischen Instabilität und kann zu ungenauen Ergebnissen führen.

# Aufgabe 2c)

def umformung(x):
    return x/(2*np.cos(1+x/2) * np.sin(x/2))

plt.figure(figsize=(10, 6))
points_exercise_c = np.arange(-10**-14, 10**-14, 10**-17)
plt.plot(points_exercise_c, umformung(points_exercise_c), label='Umformung g(x)', color='purple')
plt.plot(points_exercise_c, g(points_exercise_c), label='g(x)', color='green', linestyle='dashed')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Comparison of Umformung g(x) and g(x)')
plt.xlabel('x')
plt.ylabel('Umformung g(x)')
plt.xlim(-10**-14, 10**-14)
plt.yscale("symlog", linthresh=1e-15)
plt.legend()
plt.grid()
plt.show()

# Die Umformung beseitigt die Auslöschung in sin(1+x) - sin(1) und ist deshalb für die Annäherung an x = 0 numerisch deutlich stabiler.
# Der Ausdruck ist bei x = 0 weiterhin nicht definiert. Sein Grenzwert ist aber korrekt und lautet nun: lim(x->0) g(x) = 1/cos(1) ≈ 1.8508
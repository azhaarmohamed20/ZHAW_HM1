import numpy as np
import matplotlib.pyplot as plt


def h(x):
	"""Berechnet h mit dem Polynom aus der Aufgabenstellung."""
	return np.sqrt(100 * x**2 - 200 * x + 99)


def h_stabil(x):
	"""Berechnet h in faktorisierter Form, um Auslöschung zu vermeiden."""
	return np.sqrt((10 * x - 9) * (10 * x - 11))


def kondition(x):
	"""Relative Konditionszahl von h bezüglich Änderungen von x."""
	radicand = 100 * x**2 - 200 * x + 99
	return np.abs(100 * x * (x - 1) / radicand)


# Aufgabe 4a: In der Nähe von x = 1.1 werden im Polynom fast gleich grosse
# Zahlen voneinander abgezogen. Dadurch gehen wichtige Stellen verloren.
x_near = np.array([1.1, 1.1 + 1e-14, 1.1 + 1e-12, 1.1 + 1e-10])
print("x:", x_near)
print("h(x), polynomial:", h(x_near))
print("h(x), factorized:", h_stabil(x_near))

# Aufgabe 4b: Halb-logarithmischer Plot mit der verlangten Auflösung.
delta_x = 1e-7
x_values = np.arange(1.1, 1.3 + delta_x, delta_x)
condition_values = kondition(x_values)

plt.figure(figsize=(10, 6))
plt.semilogy(x_values[1:], condition_values[1:], label=r"$\kappa_h(x)$")
plt.xlabel("x")
plt.ylabel(r"relative Kondition $\kappa_h(x)$")
plt.title("Kondition von h(x)")
plt.grid(True, which="both")
plt.legend()

print("Kondition bei x = 1.1 + 1e-7:", kondition(1.1 + delta_x))

plt.show()


"""
Aufgabe 4c:

Die Auslöschung kann durch die algebraische Umformung

	h(x) = sqrt((10*x - 9)*(10*x - 11))

während der Auswertung vermieden werden. Dabei werden keine fast gleichen,
grossen Zahlen voneinander abgezogen. Die schlechte Kondition an der Stelle
x = 1.1 kann dadurch aber nicht beseitigt werden: h(x) geht dort gegen 0 und

	kappa_h(x) = |100*x*(x - 1) / (100*x**2 - 200*x + 99)| -> unendlich.

Die Funktion bleibt an dieser Stelle also von sich aus schlecht konditioniert.
"""

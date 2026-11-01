import numpy as np
from Berisha_Mohamed_S06_Aufg2 import Berisha_Mohamed_S06_Aufg2

A1 = [[4, -1, -5],
      [-12, 4, 17],
      [32, -10, -41]]
b1 = [6, -12, 48]

A2 = [[2, 7, 3],
      [-4, -10, 0],
      [12, 34, 9]]
b2 = [5, -22, 42]

A3 = [[-2, 5, 4],
      [-14, 38, 22],
      [6, -9, -27]]
b3 = [16, 82, -120]

A4 = [[-1, 2, 3, 2, 5, 4, 3, -1],
      [3, 4, 2, 1, 0, 2, 3, 8],
      [2, 7, 5, -1, 2, 1, 3, 5],
      [3, 1, 2, 6, -3, 7, 2, -2],
      [5, 2, 0, 8, 7, 6, 1, 3],
      [-1, 3, 2, 3, 5, 3, 1, 4],
      [8, 7, 3, 6, 4, 9, 7, 9],
      [-3, 14, -2, 1, 0, -2, 10, 5]]
b4 = [-11, 103, 53, -20, 95, 78, 131, -26]


systeme = [(A1, b1), (A2, b2), (A3, b3), (A4, b4)]

for i, (A, b) in enumerate(systeme, start=1):
    A_triangle, detA, x = Berisha_Mohamed_S06_Aufg2(A, b)
    x_numpy = np.linalg.solve(np.array(A, dtype=float),
                              np.array(b, dtype=float))

    print(f"\nGleichungssystem {i}:")
    print("Gauss:", x)
    print("NumPy:", x_numpy)
    print("Determinante:", detA)
    print("Stimmen überein:", np.allclose(x, x_numpy))


# Vergleich:
# Die Ergebnisse stimmen bei allen vier Gleichungssystemen
# mit NumPy überein. Teilweise gibt es kleine Abweichungen
# bei den Nachkommastellen, die durch Rundungsfehler entstehen.
# Deshalb wird mit np.allclose() verglichen.

import numpy as np
import matplotlib.pyplot as plt
from Serie_6.Berisha_Mohamed_S06_Aufg2 import Berisha_Mohamed_S06_Aufg2

def berechne_polynom(jahre, tage):
    startjahr = jahre[0]
    t = jahre - startjahr

    A = np.vander(t, len(jahre), increasing=True)

    _, _, koeffizienten = Berisha_Mohamed_S06_Aufg2(A.astype(float), tage.astype(float))

    return koeffizienten[::-1], startjahr


def schaetze_tage(koeffizienten, jahre, startjahr):
    t = np.asarray(jahre) - startjahr
    return np.polyval(koeffizienten, t)


jahre = np.array([1997, 1999, 2006, 2010])
tage = np.array([150, 104, 172, 152])


# Aufgabe 3a
koeffizienten, startjahr = berechne_polynom(jahre, tage)

print("Aufgabe 3a:")
print("Polynomkoeffizienten:", koeffizienten)


# Aufgabe 3b
jahre_gesucht = np.array([2003, 2004])

schaetzwerte = schaetze_tage(koeffizienten, jahre_gesucht, startjahr)

print("\nAufgabe 3b:")
for jahr, wert in zip(jahre_gesucht, schaetzwerte):
    print(f"{jahr}: {wert:.2f} Tage")


# Aufgabe 3c
t = jahre - startjahr

koeffizienten_polyfit = np.polyfit(t, tage, 3)

schaetzwerte_polyfit = schaetze_tage( koeffizienten_polyfit, jahre_gesucht, startjahr)

print("\nAufgabe 3c:")
print("Koeffizienten polyfit:", koeffizienten_polyfit)
print("Schätzwerte polyfit:", schaetzwerte_polyfit)

print("Koeffizienten stimmen überein:",np.allclose(koeffizienten, koeffizienten_polyfit))


t_plot = np.arange(0, jahre[-1] - startjahr + 0.1, 0.1)
jahre_plot = t_plot + startjahr

y_interpolation = np.polyval(koeffizienten, t_plot)
y_polyfit = np.polyval(koeffizienten_polyfit, t_plot)

plt.figure(figsize=(10, 6))

plt.plot(jahre_plot, y_interpolation, label="Interpolation (Gauss)")

plt.plot(jahre_plot, y_polyfit, "--", label="Interpolation (polyfit)")

plt.scatter(jahre, tage, color="red", label="Messwerte")
plt.scatter(jahre_gesucht, schaetzwerte, color="blue", label="Schätzwerte")

plt.xlabel("Jahr")
plt.ylabel("Tage mit extremer UV-Belastung")
plt.title("Polynominterpolation – Hawaii")
plt.legend()
plt.grid(True)
plt.show()

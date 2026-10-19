import numpy as np
import matplotlib.pyplot as plt


def grippeausbreitung(alpha, schritte=50):
    k = 0.1
    werte = [k]

    for i in range(schritte):
        k = alpha * k * (1 - k)
        werte.append(k)

    return werte


# Aufgabe 2a)
# Wir schauen uns verschiedene Werte von alpha zwischen 0 und 4 an.
# Für alpha <= 1 geht k gegen 0.
# Für 1 < alpha < 3 geht k gegen einen positiven Fixpunkt.
# Für alpha = 3 geht k auch gegen diesen Fixpunkt, aber sehr langsam.
# Für alpha > 3 gibt es keinen einzelnen Grenzwert mehr.
# Es können dann zum Beispiel periodische Werte oder Chaos entstehen.

alphas = [0, 1, 2, 3, 4]

plt.figure()

for alpha in alphas:
    plt.plot(grippeausbreitung(alpha), label="alpha = " + str(alpha))

plt.xlabel("Zeitschritt")
plt.ylabel("k")
plt.title("Fixpunktiteration für verschiedene alpha")
plt.grid()
plt.legend()
plt.show()


# Aufgabe 2b)
# Ein Fixpunkt bedeutet, dass sich k nicht mehr verändert.
# Der Anteil der kranken Kinder bleibt also gleich gross.
# Es werden dann gleich viele Kinder gesund, wie sich neu anstecken.
#
# Der Fixpunkt k = 0 bedeutet, dass niemand krank ist.
# Der positive Fixpunkt bedeutet, dass ein gleichbleibender Anteil
# der Kinder krank ist.


# Aufgabe 2c)
# Für einen Fixpunkt gilt:
#
# k = alpha * k * (1 - k)
#
# Wenn man alles auf eine Seite bringt, erhält man:
#
# 0 = alpha * k - alpha * k**2 - k
# 0 = k * (alpha - 1 - alpha * k)
#
# Daraus folgen die beiden Fixpunkte:
#
# k1 = 0
# k2 = (alpha - 1) / alpha
#
# Der zweite Fixpunkt ist nur für alpha > 1 positiv.


def fixpunkte(alpha):
    if alpha == 0:
        return 0, None

    return 0, (alpha - 1) / alpha


print("Fixpunkte:")
for alpha in [0, 1, 2, 3, 4]:
    print("alpha =", alpha, ":", fixpunkte(alpha))

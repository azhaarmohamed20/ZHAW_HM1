import math

def eps(n):
    eps = n
    stellenzahl = 0

    while eps + 1.0 != 1.0:
        eps = eps / 2
        stellenzahl = stellenzahl + 1;

    return eps, stellenzahl

def qmin(n):
    qmin = n

    while 1.0 + qmin != qmin:
        qmin = qmin * 2

    return qmin


eps, stellenzahl = eps(1.0)
qmin = qmin(1.0)

print("Maschinengenauigkeit eps:", eps)
print("qmin:", qmin)
print("Stellenzahl:", stellenzahl)


"""
Wie hängen qmin und eps zusammen?
eps wird so lange halbiert, bis 1 + eps wieder 1 ergibt. Bei qmin wird der Wert stattdessen so lange verdoppelt, bis 1 + qmin wieder qmin ergibt.qmin und eps sind Kehrwerte voneinander. Es gilt also qmin = 1 / eps beziehungsweise qmin · eps = 1. eps ist sehr klein, während qmin entsprechend gross ist.
"""

print("qmin (1/eps): ", 1 / eps)
print("qmin * eps  =", qmin * eps)
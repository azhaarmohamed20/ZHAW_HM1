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

"""
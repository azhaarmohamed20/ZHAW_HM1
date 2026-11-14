import numpy as np
import timeit

def Serie08_Aufg2(A):
    A = np.copy(A)                              #necessary to prevent changes to original matrix A
    A = A.astype('float64')                     #enforce data type float

    n = np.shape(A)[0]

    if n != np.shape(A)[1]:
        raise Exception('Matrix is not square')

    Q = np.eye(n)
    R = A

    for j in range(0, n-1):
        a = np.copy(R[j:, j]).reshape(n-j, 1)    #reshape to column vectors
        e = np.zeros(n-j).reshape(n-j, 1)
        e[0] = 1.
        length_a = np.linalg.norm(a)
        if a[0] >= 0:
            sig = length_a
        else:
            sig = -length_a
        v = a + sig * e
        u = v / np.linalg.norm(v)
        H = np.eye(n-j) - 2 * u @ u.T
        Qi = np.eye(n)
        Qi[j:,j:] = H
        R = Qi @ R
        Q = Q @ Qi

    return(Q,R)


# Aufgabe 2b
A = np.array([[1, -2, 3], [-5, 4, 1], [2, -1, 3]])
b = np.array([1, 9, 5])

Q, R = Serie08_Aufg2(A)
x = np.linalg.solve(R, Q.T @ b)

print('Lösung aus Aufgabe 1:', x)
print('Kontrolle A = QR:', np.allclose(A, Q @ R))

# Aufgabe 2c
t1 = timeit.repeat(lambda: Serie08_Aufg2(A), number=100)
t2 = timeit.repeat(lambda: np.linalg.qr(A), number=100)

avg_t1 = np.average(t1) / 100
avg_t2 = np.average(t2) / 100

print('\n3 x 3 Matrix:')
print('Eigene QR-Zerlegung:', avg_t1, 'Sekunden')
print('NumPy QR-Zerlegung:', avg_t2, 'Sekunden')

# Aufgabe 2d
Test = np.random.rand(100, 100)

t1 = timeit.repeat(lambda: Serie08_Aufg2(Test), number=100)
t2 = timeit.repeat(lambda: np.linalg.qr(Test), number=100)

avg_t1 = np.average(t1) / 100
avg_t2 = np.average(t2) / 100

print('\n100 x 100 Matrix:')
print('Eigene QR-Zerlegung:', avg_t1, 'Sekunden')
print('NumPy QR-Zerlegung:', avg_t2, 'Sekunden')


"""
Beim Laufzeitvergleich fällt auf, dass NumPy vor allem bei grösseren Matrizen deutlich schneller ist als unsere eigene Funktion. Das liegt daran, dass NumPy bereits optimierte Funktionen verwendet, während unsere Implementierung viele einzelne Matrixoperationen durchführen muss.
"""

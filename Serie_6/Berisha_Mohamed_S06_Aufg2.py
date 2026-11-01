def Berisha_Mohamed_S06_Aufg2(A, b):
    n = len(A)
    A = [row.copy() for row in A]
    b = b.copy()
    detA = 1

    for i in range(n):
        max_row = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_row][i]):
                max_row = j

        if i != max_row:
            A[i], A[max_row] = A[max_row], A[i]
            b[i], b[max_row] = b[max_row], b[i]
            detA *= -1

        if abs(A[i][i]) < 1e-12:
            raise ValueError("Keine eindeutige Lösung vorhanden")

        detA *= A[i][i]

        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]

            for k in range(i, n):
                A[j][k] -= factor * A[i][k]

            b[j] -= factor * b[i]

    A_triangle = A

    x = [0] * n

    for i in range(n - 1, -1, -1):
        summe = 0
        for j in range(i + 1, n):
            summe += A[i][j] * x[j]

        x[i] = (b[i] - summe) / A[i][i]

    return A_triangle, detA, x


if __name__ == "__main__":
    A = [[2, 1, -1], [3, 3, 9], [3, 4, 4]]
    b = [8, 0, -2]

    A_triangle, detA, x = Berisha_Mohamed_S06_Aufg2(A, b)

    print("Obere Dreiecksmatrix:")
    for row in A_triangle:
        print(row)

    print("Determinante:", detA)
    print("Lösung für x:", x)
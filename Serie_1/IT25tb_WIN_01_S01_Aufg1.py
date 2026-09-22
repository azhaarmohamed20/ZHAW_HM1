import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x ** 5 - 5 * x ** 4 - 30 * x ** 3 + 110 * x ** 2 + 29 * x - 105

def f_stamm(x):
    return x ** 6 / 6 - x ** 5 - 7.5 * x ** 4 + (110 / 3) * x ** 3 + (29 / 2) * x ** 2 - 105 * x

def f_a(x):
    return 5* x ** 4 - 20 * x ** 3 - 90 * x ** 2 + 220 * x + 29

def nullstellen(x):
    nullstellen = []
    for i in range(-10,10):
        if f(i) == 0:
            nullstellen.append(i)
    return nullstellen

x = np.arange(-10, 10, 1)
print("Nullstellen: ", nullstellen(x))

# Abbildung
plt.figure(1)
plt.plot(x,f(x), label='f(x)')
plt.plot(x,f_stamm(x), label='Stammfunktion F(x)')
plt.plot(x,f_a(x), label='Ableitung f\'(x)')
plt.xlim(-10,10)
plt.ylim(-500,500)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Abbildung 1')
plt.grid()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x ** 5 - 5 * x ** 4 - 30 * x ** 3 + 110 * x ** 2 + 29 * x - 105

def F(x):
    return x ** 5 - 5 * x ** 4 - 30 * x ** 3 + 110 * x ** 2 + 29 * x  - 105

def f_a(x):
    return 5* x ** 4 - 20 * x ** 3 - 90 * x ** 2 + 220 * x + 29 - 105

x = np.arange(-10, 10)
nullstellen = np.roots(f(x))
print(nullstellen)




# Abbildung
plt.figure(1)
plt.plot(x,f(x), label='f(x)')
plt.xlim()
plt.ylim()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Abbildung 1')
plt.grid()
plt.show()
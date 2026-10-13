
import numpy as np
import matplotlib.pyplot as plt

# x values between 0.01 and 100
x = np.logspace(-2, 2, 500)

# Functions
f = 5 / np.cbrt(2 * x**2)
g = 10**5 * (2 * np.e)**(-x / 100)
h = (10**4 / 2**10)**x

# (i) Power function
plt.figure()
plt.loglog(x, f)
plt.title("(i) f(x) - log-log")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()

# (ii) Exponential function
plt.figure()
plt.semilogy(x, g)
plt.title("(ii) g(x) - semilog-y")
plt.xlabel("x")
plt.ylabel("g(x)")
plt.grid(True)
plt.show()

# (iii) Exponential function
plt.figure()
plt.semilogy(x, h)
plt.title("(iii) h(x) - semilog-y")
plt.xlabel("x")
plt.ylabel("h(x)")
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

def print_function(a, str):
    a = check_vector(a)
    degree = a.size - 1
    terms = []
    for coefficient in a:
        if coefficient == 0:
            degree -= 1
            continue
        if degree == 0:
            term = f"{abs(coefficient):g}"
        elif degree == 1:
            term = f"{abs(coefficient):g}x"
        else:
            term = f"{abs(coefficient):g}x^{degree}"
        if coefficient < 0:
            terms.append("- " + term)
        else:
            terms.append("+ " + term)
        degree -= 1
    expression = " ".join(terms).lstrip("+ ")
    print(str, " = ", expression)


def f(a, x):
    a = check_vector(a)
    x = np.asarray(x, dtype=float)
    p = np.zeros_like(x, dtype=float)
    exp = a.size - 1
    for coefficient in a:
        p += coefficient * x**exp
        exp -= 1
    return p

def f_abl_vector(a):
    a = check_vector(a)
    degree = a.size - 1
    if degree == 0:
        return np.array([0])
    derivative = np.zeros(degree)
    for i in range(degree):
        derivative[i] = a[i] * (degree - i)
    return derivative

def f_abl(a, x):
    derivative = f_abl_vector(a)
    return f(derivative, x)

def f_stamm_vector(a):
    a = check_vector(a)
    degree = a.size - 1
    stamm = np.zeros(degree + 2)
    for i in range(degree + 1):
        stamm[i] = a[i] / (degree - i + 1)
    return stamm

def f_stamm(a, x):
    stamm = f_stamm_vector(a)
    return f(stamm, x)

def Berisha_Mohamed_S01_Aufg2(a, xmin, xmax):
    x = np.arange(xmin, xmax+1, 0.1)
    p = f(a, x)
    derivative = f_abl_vector(a)
    dp = f(derivative, x)
    stamm = f_stamm_vector(a)
    pint = f(stamm, x)
    print_function(a, "f(x)")
    print_function(derivative, "f'(x)")
    print_function(stamm, "F(x)")
    x_int = np.arange(xmin, xmax+1, dtype=int)
    p_int = f(a, x_int)
    print("f(x) =", p_int)
    print("f'(x) =", f(derivative, x_int))
    print("F(x) =", f(stamm, x_int))

    return x, p, dp, pint

def check_vector(a):
    a = np.asarray(a)
    if a.size == 0:
        raise ValueError("Vector is empty")
    if np.shape(a) == (a.size,1) or np.shape(a) == (a.size,):
        a = a.flatten()
    else:
        raise ValueError("Vector is not a valid vector")
    return a

plt.figure(1)
x, p, dp, pint = Berisha_Mohamed_S01_Aufg2([1, 1, 0], -5, 5)
plt.plot(x, p, label='f(x)')
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot(x, dp, label='f\'(x)')
plt.plot(x, pint, label='F(x)')
plt.legend()
plt.title('Abbildung 1')
plt.grid()
plt.show()
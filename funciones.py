import numpy as np

def f1(x):
    return x**2 - 2

def f1_derivada(x):
    return 2*x

def f2(x):
    return x**5 - 6.6 * x**4 + 5.12 * x**3 + 21.312 * x**2 - 38.016 * x + 17.28

def f2_derivada(x):
    return 5 * x**4 -26.4 * x**3 + 15.36 * x**2 + 42.624 * x - 38.016

def f3(x):
    return (x - 1.5) * np.exp(-4 * (x - 1.5) ** 2)

def f3_derivada(x):
    return (-8 * x + 12) * (x - 1.5) * np.exp(-4 * (x - 1.5) ** 2) + np.exp(-4 * (x - 1.5)**2)
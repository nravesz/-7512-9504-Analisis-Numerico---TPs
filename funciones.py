import numpy as np
import matplotlib.plotly as plt

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

def imprimirFuncion(funcion):
    nroResolucion = 250
    inicioIntervalo = 0
    finIntervalo = 2
    
    valores = np.zeros((nroResolucion,2))
    
    vector_x = np.linspace(inicioIntervalo, finIntervalo, nroResolucion)
    i = 0
    for x in vector_x:
        valores[i] = (x,funcion(x))
        i = i+1
    
    plt.figure()
    plt.plot(valores[:,0],valores[:,1], '-',lw=2,label='f(x)')    
    plt.title('f(x)')
    plt.legend(loc='best')
    plt.grid(True)
    ax = plt.gca()  # gca stands for 'get current axis'
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    plt.show()
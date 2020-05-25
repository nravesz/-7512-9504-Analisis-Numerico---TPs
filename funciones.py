import numpy as np
import matplotlib.pyplot as plt
from abc import ABCMeta, abstractmethod

class Funcion(metaclass=ABCMeta):
    
    @abstractmethod
    def evaluar_funcion(self, x):
        pass
    
    @abstractmethod
    def evaluar_derivada_primera(self, x):
        pass
    
    @abstractmethod
    def evaluar_derivada_segunda(self, x):
        pass

class F1(Funcion):
    
    def evaluar_funcion(self, x):
        return x**2 - 2
    
    def evaluar_derivada_primera(self, x):
        return 2*x
    
    def evaluar_derivada_segunda(self, x):
        return 2

class F2(Funcion):
    
    def evaluar_funcion(self, x):
        return x**5 - 6.6 * x**4 + 5.12 * x**3 + 21.312 * x**2 - 38.016 * x + 17.28
    
    def evaluar_derivada_primera(self, x):
        return 5 * x**4 -26.4 * x**3 + 15.36 * x**2 + 42.624 * x - 38.016
    
    def evaluar_derivada_segunda(self, x):
        return 20 * x**3 - 79.2 * x**2 +30.72 * x + 42.624

class F3(Funcion):
    
    def evaluar_funcion(self, x):
        return (x - 1.5) * np.exp(-4 * (x - 1.5) ** 2)
    
    def evaluar_derivada_primera(self, x):
        return (-8 * x + 12) * (x - 1.5) * np.exp(-4 * (x - 1.5) ** 2) + np.exp(-4 * (x - 1.5)**2)
    
    def evaluar_derivada_segunda(self, x):
        return (-24 * x + (x - 1.5) * (8 *x - 12)**2 + 36) * np.exp(-4 * (x - 1.5)**2)

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
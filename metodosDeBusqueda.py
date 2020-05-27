import numpy as np
import math

def calcular_cantidad_iteraciones_biseccion(tolerancia, a, b):
    n = np.log2(b - a) - np.log2(tolerancia)
    return math.ceil(n)

def biseccion(funcion, tolerancia, a, b):
    """
    Prerequisitos: la funcion debe admitir raiz
    Recibe:
    -funcion: funcion a la cual se le buscara la raiz.
    -tolerancia: el criterio de paro. Si la diferencia entre la raiz actual
    y la anterior es esa tolerancia, se finaliza la busqueda.
    -a: inicio del intervalo donde se buscara la raiz.
    -b: fin del intervalo donde se buscara la raiz.
    Devuelve:
    -El historial de todas las iteraciones hasta cumplir con la tolerancia.
    """
    historial = []
    n = calcular_cantidad_iteraciones_biseccion(tolerancia, a, b)
    for i in range(0, n, 1):
        raizAct = (a + b) / 2
        historial.append(raizAct)
        if funcion.evaluar_funcion(a) * funcion.evaluar_funcion(raizAct) < 0:
            b = raizAct
        else:
            a = raizAct
    return historial

def newton_raphson(funcion, tolerancia, semilla):
    """
    Recibe:
    -funcion: funcion a la cual se le buscara la raiz.
    -tolerancia: el criterio de paro. Si la diferencia entre la raiz actual
    y la anterior es esa tolerancia, se finaliza la busqueda.
    -semilla: donde se va a iniciar a iterar
    -derivada: derivada de la funcion a la cual se le quiere buscar la raiz
    Devuelve:
    -El historial de todas las iteraciones hasta cumplir con la tolerancia.
    """
    historial = []
    error = np.inf
    raizAnt = semilla
    while error > tolerancia:
        raizAct = raizAnt - (funcion.evaluar_funcion(raizAnt) / funcion.evaluar_derivada_primera(raizAnt))
        historial.append(raizAct)
        error = np.abs(raizAnt - raizAct)
        raizAnt = raizAct
    return historial

def secante(funcion, tolerancia, semilla1, semilla2):
    """
    Recibe:
    -funcion: funcion f(x) a la cual se le buscara la raiz.
    -tolerancia: el criterio de paro. Si la diferencia entre la raiz actual.
    y la anterior es esa tolerancia, se finaliza la busqueda.
    -semilla1: punto donde se va a iniciar a iterar.
    -semilla2: segundo punto donde se va a iniciar a iterar.
    Devuelve:
    -El historial de todas las iteraciones hasta cumplir con la tolerancia.
    """
    historial = []
    ptoAnterior = semilla1
    ptoAnterior2 = semilla2
    error = np.inf
    while error > tolerancia:
        p = ptoAnterior - ((funcion.evaluar_funcion(ptoAnterior)*(ptoAnterior-ptoAnterior2))\
                            /(funcion.evaluar_funcion(ptoAnterior)-funcion.evaluar_funcion(ptoAnterior2)))
        historial.append(p)
        error = np.abs(p-ptoAnterior)
        ptoAnterior2 = ptoAnterior
        ptoAnterior = p
    return historial

def newtonRaphsonMod(funcion, tolerancia, semilla):
    """
    Recibe:
    -funcion: funcion a la cual se le buscara la raiz.
    -tolerancia: el criterio de paro. Si la diferencia entre la raiz actual
    y la anterior es esa tolerancia, se finaliza la busqueda.
    -semilla: punto donde se va a iniciar a iterar.
    Devuelve:
    -El historial de todas las iteraciones hasta cumplir con la tolerancia.
    """
    historial = []
    error = np.inf
    raizAnt = semilla
    while error > tolerancia:
        raizAct = raizAnt - (funcion.evaluar_funcion(raizAnt) * funcion.evaluar_derivada_primera(raizAnt)\
                             /(((funcion.evaluar_derivada_primera(raizAnt))**2) - funcion.evaluar_funcion(raizAnt)\
                             * funcion.evaluar_derivada_segunda(raizAnt)))
        historial.append(raizAct)
        error = np.abs(raizAnt - raizAct)
        raizAnt = raizAct
    return historial

def estimarOrdenConvergencia(historialRaices):
    nIteraciones = len(historialRaices)
    alfa = []
    
    for n in range(2,nIteraciones-1):
        e_n_mas_1 = historialRaices[n+1]-historialRaices[n]
        e_n = historialRaices[n] - historialRaices[n-1]
        e_n_menos_1 = historialRaices[n-1]-historialRaices[n-2]
        
        alfa.append(np.log10(np.abs(e_n_mas_1/e_n))/ \
        np.log10(np.abs(e_n/e_n_menos_1)))
    
    return alfa
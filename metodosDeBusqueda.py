import numpy as np

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
    ini = a
    fin = b
    historial = []
    error = np.inf
    raizAnt = np.inf
    while error > tolerancia:
            raizAct = (ini + fin) / 2
            historial.append(raizAct)
            if funcion(ini) * funcion(raizAct) < 0:
                fin = raizAct
            else:
                ini = raizAct
            error = np.abs(raizAnt - raizAct)
            raizAnt = raizAct
    return historial

def newtonRaphson(funcion, tolerancia, semilla, derivada):
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
        raizAct = raizAnt - (funcion(raizAnt) / derivada(raizAnt))
        historial.append(raizAct)
        error = np.abs(raizAnt - raizAct)
        raizAnt = raizAct
    return historial


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

def puntoFijo(funcion, tolerancia, semilla, maxIteraciones):
    """
    Recibe:
    -funcion: funcion g(x) a la cual se le buscara la raiz.
    -tolerancia: el criterio de paro. Si la diferencia entre la raiz actual
    y la anterior es esa tolerancia, se finaliza la busqueda.
    -semilla: donde se va a iniciar a iterar
    -maxIteraciones: cantidad maxima de iteraciones que se va a ejecutar el algoritmo.    
    Devuelve:
    -El historial de todas las iteraciones hasta cumplir con la tolerancia.
    """
    historial = []
    ptoAnterior = semilla
    i = 0
    while i < maxIteraciones:
        p = funcion(ptoAnterior)
        historial[i] = (i, p)
        if np.abs(p-ptoAnterior) < tolerancia:
            return historial
        
        ptoAnterior = p
        i = i + 1
    
    print("No converge utilizando puntoFijo")
    return None

def secante(funcion, tolerancia, semilla1, semilla2):
    """
    Recibe:
    -funcion: funcion f(x) a la cual se le buscara la raiz.
    -tolerancia: el criterio de paro. Si la diferencia entre la raiz actual
    y la anterior es esa tolerancia, se finaliza la busqueda.
    -semilla1: donde se va a iniciar a iterar
    -semilla2: segundo punto donde se va a iniciar a iterar
    Devuelve:
    -El historial de todas las iteraciones hasta cumplir con la tolerancia.
    """
    historial = []
    ptoAnterior = semilla1
    ptoAnterior2 = semilla2
    error = np.inf
    while error > tolerancia:
        p = ptoAnterior + ((funcion(ptoAnterior)*(ptoAnterior-ptoAnterior2))\
                            /(funcion(ptoAnterior)-funcion(ptoAnterior2)))
        historial.append(p)
        error = np.abs(p-ptoAnterior)
        ptoAnterior2 = ptoAnterior
        ptoAnterior = p
    return historial

def newtonRaphsonMod(funcion, tolerancia, semilla, derivada1, derivada2):
    """
    Recibe:
    -funcion: funcion a la cual se le buscara la raiz.
    -tolerancia: el criterio de paro. Si la diferencia entre la raiz actual
    y la anterior es esa tolerancia, se finaliza la busqueda.
    -semilla: donde se va a iniciar a iterar
    -derivada1: derivada primera de la funcion a la cual se le quiere buscar la raiz.
    -derivada2: derivada segunda de la funcion a la cual se le quiere buscar la raiz.
    Devuelve:
    -El historial de todas las iteraciones hasta cumplir con la tolerancia.
    """
    historial = []
    error = np.inf
    raizAnt = semilla
    while error > tolerancia:
        raizAct = raizAnt - (funcion(raizAnt) * derivada1(raizAnt)\
                             /(((derivada1(raizAnt))**2)-funcion(raizAnt)*derivada2(raizAnt)))
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
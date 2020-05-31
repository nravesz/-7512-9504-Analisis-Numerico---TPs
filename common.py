import pandas as pd
import metodosDeBusqueda as metodo
import numpy as np
import matplotlib.pyplot as plt

def aplicar_metodos(funcion, tolerancia, rango, semilla):
	a, b = rango

	historial1 = metodo.biseccion(funcion, tolerancia, a, b)
	
	historial2 = metodo.newton_raphson(funcion, tolerancia, semilla)

	historial3 = metodo.secante(funcion, tolerancia, a, b)
	
	historial4 = metodo.newtonRaphsonMod(funcion, tolerancia, semilla)
	
	return historial1, historial2, historial3, historial4

def imprimir_funcion(funcion):
	nroResolucion = 250
	inicioIntervalo = 0
	finIntervalo = 2
	
	valores = np.zeros((nroResolucion,2))
	
	vector_x = np.linspace(inicioIntervalo, finIntervalo, nroResolucion)
	i = 0
	for x in vector_x:
		valores[i] = (x,funcion.evaluar_funcion(x))
		i = i+1
	
	plt.figure()
	plt.plot(valores[:,0],valores[:,1], '-',lw=2,label=funcion.imprimir_nombre(), color = 'red')    
	plt.title(funcion.imprimir_nombre())
#    plt.legend(loc='best')
	plt.grid(True)
	ax = plt.gca()  # gca stands for 'get current axis'
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.spines['bottom'].set_position(('data',0))
	ax.yaxis.set_ticks_position('left')
	ax.spines['left'].set_position(('data',0))
	plt.show()

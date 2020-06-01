import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from metodosDeBusqueda import biseccion, newton_raphson, newtonRaphsonMod, secante

def log(errores):
	return list(map(np.log10, errores))

def graficar_errores(funcion, tolerancia, semilla_nr, inicio_secante, fin_secante):
	'''Para F3 recomiendo semilla 1.4 para NR y intervalos 1.1-2.0 para secante'''
	historial, errores = biseccion(funcion, tolerancia, 0.0, 2.0)
	dfs=(crear_df_iteraciones(historial, log(errores), "biseccion"))
	historial, errores = newton_raphson(funcion, tolerancia, semilla_nr)
	dfs = dfs.append(crear_df_iteraciones(historial, log(errores), "NR"))
	historial, errores = newtonRaphsonMod(funcion, tolerancia, semilla_nr)
	dfs = dfs.append(crear_df_iteraciones(historial, log(errores), "NRM"))
	historial, errores = secante(funcion, tolerancia, inicio_secante, fin_secante)
	dfs = dfs.append(crear_df_iteraciones(historial, log(errores), "secante"))
	sns.lineplot(data = dfs, x="iteracion", y= "error", hue = "metodo")
	plt.title("Error segun cantidad de iteraciones para F3")
	plt.xlabel("Cantidad de iteraciones")
	plt.ylabel("Valor del error (logscale)")
	plt.show()

def crear_df_iteraciones(historial, errores, nombre):
	'''Nombre es el metodo usado '''
	df = pd.DataFrame({"raiz":historial, "error":errores, "metodo":[nombre for _ in range(len(historial))]})
	df.index.name = 'iteracion'
	df.index = df.index + 1
	return df.reset_index()

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

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import optimize
from metodosDeBusqueda import biseccion, newton_raphson, newtonRaphsonMod, secante

def conseguir_raices(funcion, tolerancia, semilla_nr, inicio_secante, fin_secante):
	raices = []
	raices.append(biseccion(funcion, tolerancia, 0.0, 2.0)[0][-1])
	raices.append(newton_raphson(funcion, tolerancia, semilla_nr)[0][-1])
	raices.append(newtonRaphsonMod(funcion, tolerancia, semilla_nr)[0][-1])
	raices.append(secante(funcion, tolerancia, inicio_secante, fin_secante)[0][-1])
	raices.append(optimize.brentq(funcion.expresion, 0.0, 2.0))
	return raices

def log(errores):
	return list(map(np.log10, errores))

def graficar_errores(funcion, tolerancia, semilla_nr, inicio_secante, fin_secante):
	'''Para F3 recomiendo semilla 1.4 para NR y intervalos 1.1-2.0 para secante'''
	historial, errores = biseccion(funcion, tolerancia, 0.0, 2.0)
	dfs=(crear_df_iteraciones(historial, errores, "biseccion"))
	historial, errores = newton_raphson(funcion, tolerancia, semilla_nr)
	dfs = dfs.append(crear_df_iteraciones(historial, errores, "NR"))
	historial, errores = newtonRaphsonMod(funcion, tolerancia, semilla_nr)
	dfs = dfs.append(crear_df_iteraciones(historial, errores, "NRM"))
	historial, errores = secante(funcion, tolerancia, inicio_secante, fin_secante)
	dfs = dfs.append(crear_df_iteraciones(historial, errores, "secante"))
	plt.figure()
	sns.lineplot(data = dfs, x="iteracion", y= "error", hue = "metodo")
	plt.title(f"Error segun cantidad de iteraciones para {funcion.denominacion}")
	plt.xlabel("Cantidad de iteraciones")
	plt.ylabel("Valor del error (logscale)")
	plt.yscale("log")
	plt.savefig(f"./figuras/{funcion.denominacion}_error{tolerancia}")

def crear_df_iteraciones(historial, errores, nombre):
	'''Nombre es el metodo usado '''
	df = pd.DataFrame({"raiz":historial, "error":errores, "metodo":[nombre for _ in range(len(historial))]})
	df.index.name = 'iteracion'
	df.index = df.index + 1
	return df.reset_index()

def graficar_funcion(funcion):
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
	plt.title(funcion.denominacion)
	plt.xlabel("x")
	plt.ylabel("y")
#    plt.legend(loc='best')
	plt.grid(True)
	ax = plt.gca()  # gca stands for 'get current axis'
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.spines['bottom'].set_position(('data',0))
	ax.yaxis.set_ticks_position('left')
	ax.spines['left'].set_position(('data',0))
	plt.savefig(f"./figuras/{funcion.denominacion}")

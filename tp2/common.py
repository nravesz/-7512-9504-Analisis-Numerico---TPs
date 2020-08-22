from funciones import f1, f2
from metodos import *
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go

def separar_en_listas(lista):
	"""Recibe una lista de tuplas (las tuplas contienen 4 elementos)
	   Devuelve 4 listas para cada posicion en la tupla."""
	y_lista = []
	u_lista = []
	e_lista = []
	t_lista = []
	for y, u, e, t in lista:
		y_lista.append(y)
		u_lista.append(u)
		e_lista.append(e)
		t_lista.append(t)
	return y_lista, u_lista, e_lista, t_lista


def crear_grafico_overlap(resultados_RK1, resultados_RK4):
	"""Recibe una lista de tuplas con los resultados de los metodos
	   RK1 (Euler) y RK4. Crea un grafico con una columna correspondiente
	   a los graficos de RK1 y otra columna para los graficos de RK4.
	   Los graficos que contiene cada columna son los de pos vs t,
	   vel vs t y energia vs t."""
   
	rk1_y, rk1_u, rk1_e, rk1_t = separar_en_listas(resultados_RK1)
	rk4_y, rk4_u, rk4_e, rk4_t = separar_en_listas(resultados_RK4)
	
	fig, ((ax1, ax2)) = plt.subplots(2, 1, sharey=True)
	fig.suptitle("Sin amortiguado overlap (h = 0.0001)")

	
	ax1.plot(rk1_t, rk1_y, 'tab:blue')
	ax1.set_ylabel('Pos[rad]')
	ax1.title.set_text('RK1 vs RK4')
	ax1.grid()
	
	ax1.plot(rk4_t, rk4_y, 'tab:orange')

	
	ax2.plot(rk1_t, rk1_u, 'tab:blue')
	ax2.set_ylabel('Vel[rad/s]')
	ax2.grid()
	
	ax2.plot(rk4_t, rk4_u, 'tab:orange')
	plt.savefig("./figs/Caso con amortiguado overlap.png")


def crear_tablas(resultados_RK1, resultados_RK4):
	rk1_y, rk1_u, rk1_e, rk1_t = separar_en_listas(resultados_RK1)
	rk4_y, rk4_u, rk4_e, rk4_t = separar_en_listas(resultados_RK4)

	d = {"tiempo":rk1_t[:5] + rk1_t[-5:], "posicion":rk1_y[:5] + rk1_y[-5:], "velocidad":rk1_u[:5] + rk1_u[-5:]}
	df_euler = pd.DataFrame(d)

	d = {"tiempo":rk4_t[:5] + rk4_t[-5:], "posicion":rk4_y[:5] + rk4_y[-5:], "velocidad":rk4_u[:5] + rk4_u[-5:]}
	df_rk4 = pd.DataFrame(d)
	return df_euler, df_rk4




def crear_grafico(resultados_RK1, resultados_RK4):
	"""Recibe una lista de tuplas con los resultados de los metodos
	   RK1 (Euler) y RK4. Crea un grafico con una columna correspondiente
	   a los graficos de RK1 y otra columna para los graficos de RK4.
	   Los graficos que contiene cada columna son los de pos vs t,
	   vel vs t y energia vs t."""
   
	rk1_y, rk1_u, rk1_e, rk1_t = separar_en_listas(resultados_RK1)
	rk4_y, rk4_u, rk4_e, rk4_t = separar_en_listas(resultados_RK4)
	
	fig, ((ax1, ax2), (ax3, ax4), (ax5,ax6)) = plt.subplots(3, 2, sharey=True)
	fig.suptitle("Sin amortiguado (h = 0.02)")

	
	# RK1: Pos vs t
	ax1.plot(rk1_t, rk1_y, 'tab:orange')
	ax1.set_ylabel('Pos[rad]')
	ax1.title.set_text('RK1')
	ax1.grid()
	
	# RK4: Pos vs t
	ax2.plot(rk4_t, rk4_y, 'tab:orange')
	ax2.title.set_text('RK4')
	ax2.grid()
	
	# RK1: Vel vs t
	ax3.plot(rk1_t, rk1_u, 'tab:green')
#	ax3.set_xlabel('Tiempo[s]')
	ax3.set_ylabel('Vel[rad/s]')
	ax3.grid()
	
	# RK4: Vel vs t
	ax4.plot(rk4_t, rk4_u, 'tab:green')
#	ax4.set_xlabel('Tiempo[s]')
	ax4.grid()
	
	# RK1: Energia vs t

	ax5.plot(rk1_t, rk1_e, 'tab:red')
	ax5.set_xlabel('Tiempo[s]')
	ax5.set_ylabel('Energia')
	ax5.grid()
	

	# RK4: Energia vs t
	ax6.plot(rk4_t, rk4_e, 'tab:red')
	ax6.set_xlabel('Tiempo[s]')
	ax6.grid()
	plt.savefig("./figs/Caso con amortiguado.png")
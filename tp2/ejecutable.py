import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import math

# ----------------------------- Definicion de parametros para la ejecucion del programa -------------------------------------
# Modifique el valor x dentro de math.radians(x) en y para cambiar el valor en grados de la posicion inicial.
y= np.float(math.radians(30))

# Modifique el valor x dentro de math.radians(x) en u para cambiar el valor en Hz de la velocidad inicial.
u= np.float(math.radians(100))

# Los siguientes son los parametros de:
#   La ecuacion: "-b/m * u - g/l * y ", ecuacion diferencial planteada en el trabajo practico.
#   La ecuacion: "m*g*l*(1-cos(y))+0.5*m*(l*u)**2", ecuacion que calcula la energia del pendulo segun su posicion y velocidad.

# Mantener el valor de b en 0 es utilizado para el caso de sistema no amortiguado.
# Modificar el valor de b con un numero mayor a 0 nos lleva a un sistema con amortiguamiento subcrı́tico
# b es el coeficiente de amortiguación dado por el razomiento del medio
b = 0.5
# m es la masa del pendulo.
m = 1
# g es la aceleracion de la gravedad
g = 9.81
# l es la longitud del pendulo.
l = 1

# paso es el h, cambiar para probar otros pasos
paso = 0.02 

# rango_maximo es el maximo valor de t que se llega a tomar
rango_maximo = 20


# ----------------------------- Definicion de la clase Funcion --------------------------------------------------------------
class Funcion():

    def __init__(self, denominacion, expresion, b, m, g, l):
        self.denominacion = denominacion
        self.expresion = expresion
        self.b = float(b)
        self.m = float(m)
        self.g = float(g)
        self.l = float(l)

    def imprimir_nombre(self):
        print(self.denominacion)

    def get_denominacion(self):
        return self.denominacion

    def imprimir_expresion(self):
        print(self.expresion)

    def get_expresion(self):
        return self.expresion

    def evaluar_expresion(self, valor_y, valor_u):
        return self.expresion(valor_y, valor_u)


# Definimos la funcion f1 la cual es la ecuacion diferencial presentada en el enunciado:
f1 = Funcion(
            "-b/m * u - g/l * y ",
            lambda y,u: -(b/m) * u - (g/l) * y ,
            b,
            m,
            g,
            l
            )

# Definicion de funcion f2 la cual es: "m*g*l*(1-cos(y))+0.5*m*(l*u)**2" la ecuacion de la energia
f2 = Funcion(
            "m*g*l*(1-cos(y))+0.5*m*(l*u)**2",
            lambda y,u: m*g*l*(1-np.cos(y))+0.5*m*(l*u)**2,
            b,
            m,
            g,
            l
            )

# ----------------------------- Definicion de los metodos Euler y Runge-Kutta4 ----------------------------------------------
def metodo_euler(funcion ,y ,u , paso):
    y = np.float(y)
    u = np.float(u)
    paso = np.float(paso)
    y1 = y + paso * u
    u1 = u + paso * funcion.evaluar_expresion(y, u)
    return y1, u1

def realizar_metodo(metodo, funcion, inicio_intervalo, fin_intervalo, y, u, paso):
    total_pasos = fin_intervalo/paso
    valores = []
    tiempo = 0.0
    e = f2.evaluar_expresion(y,u)
    valores.append((y,u,e,tiempo))

    for i in range(0, int(total_pasos)):
        y, u = metodo(funcion, y, u, paso)
        e = f2.evaluar_expresion(y,u)
        tiempo = tiempo + paso
        valores.append((y,u,e, tiempo))
    
    return valores

def runge_kutta4(funcion, y, u, paso):
    k1 = funcion.evaluar_expresion(y,u)
    m1 = u
    k2 = funcion.evaluar_expresion(y+ 0.5 * paso * m1, u + 0.5 * paso * k1)
    m2 = u + 0.5 * paso * k1
    k3 = funcion.evaluar_expresion(y+ 0.5 * paso * m2, u + 0.5 * paso * k2)
    m3 = u + 0.5 * paso * k2
    k4 = funcion.evaluar_expresion(y+ 0.5 * paso * m3, u + 0.5 * paso * k3)
    m4 = u + paso * k3
    y1 = y + (paso/6) * (m1 + 2*m2 + 2*m3 + m4)
    u1 = u + (paso/6) * (k1 + 2*k2 + 2*k3 + k4)
    return y1, u1

# ----------------------------- Definicion de funciones para crear graficos y tablas ----------------------------------------
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


def crear_grafico_overlap(resultados_RK1, resultados_RK4, nombre):
	"""Recibe una lista de tuplas con los resultados de los metodos
	   RK1 (Euler) y RK4. Crea un grafico con una columna correspondiente
	   a los graficos de RK1 y otra columna para los graficos de RK4.
	   Los graficos que contiene cada columna son los de pos vs t,
	   vel vs t y energia vs t."""
   
	rk1_y, rk1_u, rk1_e, rk1_t = separar_en_listas(resultados_RK1)
	rk4_y, rk4_u, rk4_e, rk4_t = separar_en_listas(resultados_RK4)
	
	fig, ((ax1, ax2)) = plt.subplots(2, 1, sharey=True)
	fig.suptitle(f"{nombre}")

	
	ax1.plot(rk1_t, rk1_y, 'tab:blue', label = 'RK1')
	ax1.set_ylabel('Pos[rad]')
	ax1.title.set_text('RK1 vs RK4')
	ax1.grid()
	
	ax1.plot(rk4_t, rk4_y, 'tab:orange', label = 'RK4')
	ax1.legend()

	
	ax2.plot(rk1_t, rk1_u, 'tab:blue')
	ax2.set_ylabel('Vel[rad/s]')
	ax2.grid()
	
	ax2.plot(rk4_t, rk4_u, 'tab:orange')
	plt.show()


def crear_tablas(resultados_RK1, resultados_RK4):
	rk1_y, rk1_u, rk1_e, rk1_t = separar_en_listas(resultados_RK1)
	rk4_y, rk4_u, rk4_e, rk4_t = separar_en_listas(resultados_RK4)

	d = {"tiempo":rk1_t[:5] + rk1_t[-5:], "posicion":rk1_y[:5] + rk1_y[-5:], "velocidad":rk1_u[:5] + rk1_u[-5:]}
	df_euler = pd.DataFrame(d)

	d = {"tiempo":rk4_t[:5] + rk4_t[-5:], "posicion":rk4_y[:5] + rk4_y[-5:], "velocidad":rk4_u[:5] + rk4_u[-5:]}
	df_rk4 = pd.DataFrame(d)
	return df_euler, df_rk4




def crear_grafico(resultados_RK1, resultados_RK4, nombre):
	"""Recibe una lista de tuplas con los resultados de los metodos
	   RK1 (Euler) y RK4. Crea un grafico con una columna correspondiente
	   a los graficos de RK1 y otra columna para los graficos de RK4.
	   Los graficos que contiene cada columna son los de pos vs t,
	   vel vs t y energia vs t."""
   
	rk1_y, rk1_u, rk1_e, rk1_t = separar_en_listas(resultados_RK1)
	rk4_y, rk4_u, rk4_e, rk4_t = separar_en_listas(resultados_RK4)
	
	fig, ((ax1, ax2), (ax3, ax4), (ax5,ax6)) = plt.subplots(3, 2, sharey=True)
	fig.suptitle(f"{nombre}")

	
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
	plt.show()

# ----------------------------- Comienzo del programa -----------------------------------------------------------------------
# Verificamos que tipo de caso tenemos en funcion del valor del coeficiente de amortiguación
caso = "no amortiguado"
if b > 0:
    caso = "amortiguado"


valores_euler = realizar_metodo(metodo_euler,f1, 0, rango_maximo, y, u, paso)
valores_rk4 = realizar_metodo(runge_kutta4,f1, 0, rango_maximo, y, u, paso)

df_euler, df_rk4 = crear_tablas(valores_euler, valores_rk4)
crear_grafico(valores_euler, valores_rk4, f"Caso {caso} paso {paso}")
crear_grafico_overlap(valores_euler, valores_rk4, f"Caso {caso} paso {paso}") # Esto guarda los graficos en la carpeta de figuras del repositorio.
print(" ------- Tabla de valores Método Euler ------------")
print(df_euler)
print(" ---- Tabla de valores Método Runge-Kutta 4 -------")
print(df_rk4)
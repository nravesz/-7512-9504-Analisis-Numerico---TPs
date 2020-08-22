from funciones import *
import common
from metodos import realizar_metodo, metodo_euler, runge_kutta4
import numpy as np
import math

y= np.float(math.radians(30))
u= np.float(math.radians(100)) # cambiar para amortiguado / velocidad inicial

b = 0.5 # cambiar para sin o con amortiguado
m = 1
g = 9.81
l = 1

f1 = Funcion(
            "-b/m * u - g/l * y ",
            lambda y,u: -(b/m) * u - (g/l) * y ,
            b,
            m,
            g,
            l
            )




paso = 0.02 # cambiar para probar otros pasos
rango_maximo = 20
valores_euler = realizar_metodo(metodo_euler,f1, 0, rango_maximo, y, u, paso)
valores_rk4 = realizar_metodo(runge_kutta4,f1, 0, rango_maximo, y, u, paso)

common.crear_grafico(valores_euler, valores_rk4, f"Caso amortiguado paso {paso}")
common.crear_grafico_overlap(valores_euler, valores_rk4, f"Caso amortiguado paso {paso}") # Esto guarda los graficos en la carpeta de figuras del repositorio.
from funciones import f1
import common
from metodos import realizar_metodo, metodo_euler, runge_kutta4
import numpy as np

y= np.float(0.5235987755982988)
u= np.float(0)


paso = 0.02
rango_maximo = 20
valores_euler = realizar_metodo(metodo_euler,f1, 0, rango_maximo, y, u, paso)
valores_rk4 = realizar_metodo(runge_kutta4,f1, 0, rango_maximo, y, u, paso)

common.crear_grafico(valores_euler, valores_rk4)
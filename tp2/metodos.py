from funciones import f1, f2
import numpy as np
def metodo_euler(funcion ,y ,u , paso):
    y1 = y + paso * u
    u1 = u + paso * funcion.evaluar_expresion(y, u)
    return y1, u1

def realizar_metodo(metodo, funcion, inicio_intervalo, fin_intervalo, y, u, paso):
    total_pasos = rango_maximo/paso
    valores = []
    tiempo = 0
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

y= np.float(0.523599)
u= np.float(0)
paso = 0.02
rango_maximo = 20
valores_euler = realizar_metodo(metodo_euler,f1, 0, rango_maximo, y, u, paso)
valores_rk4 = realizar_metodo(runge_kutta4,f1, 0, rango_maximo, y, u, paso)


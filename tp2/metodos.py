from funciones import f1, f2
def metodo_euler(funcion ,y ,u , paso):
    y1 = y + paso * u
    u1 = u + paso * funcion.evaluar_expresion(y, u)
    return y1, u1

y= float(0.523599)
u= float(0)
paso = 0.02
rango_maximo = 20
total_pasos = rango_maximo/paso
valores = []
tiempo = 0
e = f2.evaluar_expresion(y,u)
valores.append((y,u,e,tiempo))
print("y : ",y)
print("u : ",u)
print("Energia: ", e)
print("Tiempo: ", tiempo)

for i in range(0, int(total_pasos)):
    y, u = metodo_euler(f1, y, u, paso)
    e = f2.evaluar_expresion(y,u)
    tiempo = tiempo + paso
    valores.append((y,u,e, tiempo))
    
    print("y : ",y)
    print("u : ",u)
    print("Energia: ", e)
    print("Tiempo: ", tiempo)
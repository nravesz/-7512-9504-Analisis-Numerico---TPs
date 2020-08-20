import numpy as np
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

b = 0
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



f2 = Funcion(
            "m*g*l*(1-cos(y))+0.5*m*(l*u)**2",
            lambda y,u: m*g*l*(1-np.cos(y))+0.5*m*(l*u)**2,
            b,
            m,
            g,
            l
            )

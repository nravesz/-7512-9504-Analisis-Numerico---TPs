import parser
from math import cos
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
        code = parser.expr(self.expresion).compile()
        y= float(valor_y)
        u = float(valor_u)
        b=self.b
        m = self.m
        g = self.g
        l = self.l
        return eval(code)

f1 = Funcion(
            "f1",
            "-b/m * u - g/l * y ",
            0,
            1,
            9.81,
            1
            )

f2 = Funcion(
            "E",
            "m*g*l*cos(y)+0.5*m*(l*u)**2",
            0,
            1,
            9.81,
            1
            )


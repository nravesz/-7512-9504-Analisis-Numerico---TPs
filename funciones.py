import numpy as np
import matplotlib.pyplot as plt

class Funcion():
	
	def __init__(self, denominacion, expresion, derivada_primera, derivada_segunda):
		self.denominacion = denominacion
		self.expresion = expresion
		self.derivada_primera = derivada_primera
		self.derivada_segunda = derivada_segunda

	def evaluar_funcion(self, x):
		return self.expresion(x)

	def evaluar_derivada_primera(self, x):
		return self.derivada_primera(x)
	
	def evaluar_derivada_segunda(self, x):
		return self.derivada_segunda(x)
	
	def imprimir_nombre(self):
		print(denominacion)


f1 = Funcion("f1(x)",
			lambda x: x**2 - 2,
			lambda x: 2*x,
			lambda x: 2
			)
f2 = Funcion("f2(x)",
			lambda x: x**5 - 6.6 * x**4 + 5.12 * x**3 + 21.312 * x**2 - 38.016 * x + 17.28,
			lambda x: 5 * x**4 -26.4 * x**3 + 15.36 * x**2 + 42.624 * x - 38.016,
			lambda x: 20 * x**3 - 79.2 * x**2 +30.72 * x + 42.624)
f3 = Funcion("f3(x)",
			lambda x: (x - 1.5) * np.exp(-4 * (x - 1.5) ** 2),
			lambda x: (-8 * x + 12) * (x - 1.5) * np.exp(-4 * (x - 1.5) ** 2) + np.exp(-4 * (x - 1.5)**2),
			lambda x: (-24 * x + (x - 1.5) * (8 *x - 12)**2 + 36) * np.exp(-4 * (x - 1.5)**2)
			)
	
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
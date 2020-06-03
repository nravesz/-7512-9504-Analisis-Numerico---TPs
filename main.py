from common import *
from funciones import f1, f2, f3
import os

FUNCIONES = [f1, f2, f3]
METODOS = ["biseccion", "NR", "NRM", "secante", "brentq"]

def escribir_raices(raices, tolerancia, nombre_funcion):
	with open("raices.csv", "a") as archivo:
		for i, metodo in enumerate(METODOS):
			archivo.write(f'{raices[i]},{tolerancia},{metodo},{nombre_funcion}\n')

def escribir_encabezado():
	with open("raices.csv", "a") as archivo:
		archivo.write("raiz,tolerancia,metodo,funcion\n")

def main():

	if os.path.exists("raices.csv"):
  		os.remove("raices.csv")
	escribir_encabezado()
	tolerancia_alta = 1e-5
	tolerancia_baja = 1e-13
	for funcion in FUNCIONES:
		graficar_funcion(funcion) # Parte A
		nombre_funcion = funcion.denominacion
		if nombre_funcion == "f3(x)":
			escribir_raices(conseguir_raices(funcion, tolerancia_alta, 1.4, 1.1, 2.0), tolerancia_alta, nombre_funcion) # Parte B y C
			graficar_errores(funcion, tolerancia_alta, 1.4, 1.1, 2.0) #¿Parte 4?
			escribir_raices(conseguir_raices(funcion, tolerancia_baja, 1.4, 1.1, 2.0), tolerancia_baja, nombre_funcion)
			graficar_errores(funcion, tolerancia_baja, 1.4, 1.1, 2.0)
		else:
			escribir_raices(conseguir_raices(funcion, tolerancia_alta, 1.0, 0.0, 2.0), tolerancia_alta, nombre_funcion)
			graficar_errores(funcion, tolerancia_alta, 1.0, 0.0, 2.0)
			escribir_raices(conseguir_raices(funcion, tolerancia_baja, 1.0, 0.0, 2.0), tolerancia_baja, nombre_funcion)
			graficar_errores(funcion, tolerancia_baja, 1.0, 0.0, 2.0)
		
		obtener_graficos_orden_de_convergencia(funcion)

main()
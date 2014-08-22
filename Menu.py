# -*- encoding: utf-8 -*-
from Opcion import Opcion
import os
import Interfaz

class Menu():
	def __init__(self, objeto):
		opcionQuit = Opcion('q', 'self.salir()', 'salir')
		self.opciones = [opcionQuit]
		self.debeCorrer = False
		self.mensaje = []
		self.objeto = objeto
		self.dictOpciones = {'q': opcionQuit}

	def salir(self):
		self.debeCorrer = False
		Interfaz.infog('\n..... bay.....\n')

	def imprimirMenu(self):
		lista = self.dictOpciones.items()
		lista.sort()
		for opcion in lista:
			Interfaz.cyan(opcion[1].imprimir())
		Interfaz.info("Atributos parseados:%i A procesar:%i" % (len(self.objeto.atributos) -1, len(self.objeto.atributosAProcesar)))

	def imprimirOpcionInvalida(self):
		Interfaz.err('Opcion Invalida')

	def imprimirError(self,opcion):
		Interfaz.err('hubo un error al ejecutar ' + self.dictOpciones[opcion].descripcion)

	def correr(self):
		self.debeCorrer = True
		mensaje = ""
		while self.debeCorrer:
			self.imprimirMenu()
			print(mensaje)
			opcion = str(raw_input('Ingrese alguna de las opciones\n\n'))
			self.ejecutar(opcion)

	def getOpciones(self):
		return self.opciones

	def agregarOpcion(self, nombre,execs, descripcion="",ayuda=""):
		opcion = Opcion(nombre,execs,descripcion,ayuda)
		self.dictOpciones[opcion.getNombre()] = opcion

	def ejecutar(self, opcion):

		if opcion in self.dictOpciones.keys():
				opcion = self.dictOpciones[opcion]
				try:
					exec(opcion.execs)
				except Exception as inst:
					Interfaz.err(str(inst))
		else:
			self.imprimirOpcionInvalida()

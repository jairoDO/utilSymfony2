from Opcion import Opcion
import os

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
		print ('\n..... bay.....\n')


	def imprimirMenu(self):
		lista = self.dictOpciones.items()
		lista.sort()
		for opcion in lista:
			opcion[1].imprimir()

	def imprimirOpcionInvalida(self):
		print 'Opcion Invalida'

	def imprimirError(self,opcion):
		print 'hubo un error al ejecutar ', self.dictOpciones[opcion].descripcion

	def correr(self):
		self.debeCorrer = True
		mensaje = ""
		while self.debeCorrer:
			self.imprimirMenu()
			print(mensaje)
			opcion = str(raw_input('Ingrese alguna de las opciones\n\n'))
			try:
				mensaje = self.ejecutar(opcion)
			except:
				self.imprimirError(opcion)

	def getOpciones(self):
		return self.opciones

	def agregarOpcion(self, nombre,execs, descripcion="",ayuda=""):
		opcion = Opcion(nombre,execs,descripcion,ayuda)
		self.dictOpciones[opcion.getNombre()] = opcion

	def ejecutar(self, opcion):

		if opcion in self.dictOpciones.keys():
				opcion = self.dictOpciones[opcion]
				exec(opcion.execs)
		else:
			self.mensaje.append('Opcion Invalida')
			self.imprimirOpcionInvalida()

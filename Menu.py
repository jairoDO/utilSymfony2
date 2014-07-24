from Opcion import Opcion

class Menu():
	def __init__(self, objeto):
		opcionQuit = Opcion('q', 'self.debeCorrer = False')
		self.opciones = [opcionQuit]
		self.debeCorrer = False
		self.mensaje = []
		self.objeto = objeto
		self.dictOpciones = {'q': opcionQuit}

	def imprimirMenu(self):
		for opcion in self.opciones:
			opcion.imprimir()

	def imprimirOpcionInvalida(self):
		print 'Opcion Invalida'

	def imprimirError(self,opcion):
		print 'hubo un error al ejecutar ', opcion.nombre

	def correr(self):
		self.debeCorrer = True
		while self.debeCorrer:
			self.imprimirMenu()
			opcion = input('Ingrese alguna de las opciones')
			try:
				self.ejecutar(opcion)
			except:
				self.imprimirError(opcion)

	def getOpciones(self):
		return self.opciones

	def agregarOpcion(self, opcion):
		self.opciones = opcion
		self.dictOpciones[opcion.getIdentificador()] = opcion

	def ejecutar(self, opcion):
		if opcion in self.dictOpciones.keys():
				opcion = self.dictOpciones[opcion]
				exec(opcion.execs)
		else:
			self.mensaje.append('Opcion Invalida')
			self.imprimirOpcionInvalida()

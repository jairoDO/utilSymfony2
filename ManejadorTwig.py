from GeneradorTwig import *

class ManejadorTwig():
	def __init__(self):
		self.atributos = dict()
		self.atributosAProcesar = []
		self.generadores = dict()
		self.generadores['boolean'] = GeneradorBolleano()
		self.generadores['decimal'] = GeneradorDecima()
		self.generadores['text'] = GeneradorText()
		self.generadores['string'] = GeneradorString()
		self.generadores.append()
		self.generadorGrup = GeneradorGrupo()
		self.mensajes = []

	def imprimirError(self, error):
		print error

	def validarEntradaAtributo(self, inputs):
		keys = inputs(',')
		for indice in keys:
			if not indice.strip() in self.atributos.keys():
				return False
		return True

	def crearGrupo(self,nombre, inputs):
		result = []
		for key in inputs:
			result.append(self.atributos[key.strip()].copy())
		return (nombre, result)

	def agregarAtibutosAPropocesar(self):
		inputs = input('Ingrese un indice o los indices seguido por coma ejemplo 1, 2, 3, 5')
		if self.validarEntradaAtributo(inputs):
			for key in inputs.split(','):
				self.atributosAProcesar.append(self.atributos[key.strip()].copy())
		else:
			self.imprimirError('Alguno de los indice no son correctos')


	def configurarGrupo(self):
		nombre = input('Ingrese el nombre del Agrupador')
		inputs = input('Ingrese los indices de los atributos seguidos por coma ejemplo 1, 2,3 ,4,2,2,3,4')
		if self.validarEntradaAtributo(inputs):
			self.atributosAProcesar.append(self.crearGrupo(nombre, inputs))
		else:
			self.imprimirError('Alguno de los indices no son correctos')

	def generarTwig(self):
		result = ""
		for atributoTwig in self.atributosAProcesar:
			if isinstance(atributoTwig, tuple):
				grupoStr = self.generadorGrupo().generar(atributoTwig[0])
				grupos = ""
				for atributo in atributoTwig[1]:
					generador = self.generadores[atributo.tipo]
					generador.grupo = True
					grupos += generador.generar(atributo)
				result += grupoStr % grupos
		return result
from GeneradorTwig import *
import os
import re

class ManejadorTwig():
	def __init__(self):
		self.atributos = dict()
		self.atributosAProcesar = []
		self.generadores = dict()
		self.generadores['boolean'] = GeneradorBooleano()
		self.generadores['decimal'] = GeneradorDecimal()
		self.generadores['text'] = GeneradorText()
		self.generadores['string'] = GeneradorString()
		self.generadores['datetime'] = GeneradorDatetime()
		self.generadores['default'] = GeneradorDefault()
		self.generadorGrupo = GeneradorGrupo()
		self.mensajes = []
		self.parsearValor = re.compile('(?P<indice>\d+)$|(?P<rangoInferior>\d+)..(?P<rangoSuperior>\d+)')

	def imprimirError(self, error):
		print error

	def parsearValorInput(self, inputString):
		result = []
		for x in inputString.split(','):
			dictGrupo = self.parsearValor.match(x.strip()).groupdict()
			if dictGrupo['indice'] is None:
				listaRango = range(int(dictGrupo['rangoInferior']), int(dictGrupo['rangoSuperior']) + 1)
				result += listaRango 
			else:
				result.append(x.strip())
		return result

	def validarEntradaAtributo(self, inputs):
		keys = inputs.split(',')
		for indice in keys:
			matcher = self.parsearValor.match(indice)
			if (matcher is None) :
				return False
			else:
				dictGrupo = matcher.groupdict()
				if not (dictGrupo['rangoSuperior'] is None) and int(dictGrupo['rangoSuperior']) + 1 > len(self.atributos):
					return False
				elif (not (dictGrupo['indice'] is None)) and int(dictGrupo['indice']) > len(self.atributos):
					return False

		return True

	def crearGrupo(self,nombre, inputs):
		result = []
		for key in inputs.split(','):
			result.append(self.atributos[int(key)])
		return (nombre, result)

	def agregarAtibutosAPropocesar(self):
		inputs = raw_input('Ingrese un indice o los indices seguido por coma ejemplo 1, 2, 3, 5\n\n')
		if self.validarEntradaAtributo(inputs):
			for key in self.parsearValorInput(inputs):
				#import pdb;pdb.set_trace()
				self.atributosAProcesar.append(self.atributos[int(key)])
		else:
			self.imprimirError('Alguno de los indice no son correctos')


	def configurarGrupo(self):
		nombre = raw_input('Ingrese el nombre del Agrupador\n\n')
		inputs = raw_input('Ingrese los indices de los atributos seguidos por coma ejemplo 1, 2,3 ,4,2,2,3,4\n\n')
		if self.validarEntradaAtributo(inputs):
			self.atributosAProcesar.append(self.crearGrupo(nombre, inputs))
		else:
			self.imprimirError('Alguno de los indices no son correctos')

	def mostrarAtributos(self):
		result = ''
		for indice, atributo in enumerate(self.atributos):
			result += "%s - %s : prop:%s\n" % (indice, atributo.nombre,str(atributo.propiedades))
		print result

	def generarTodo(self):
		os.system('clear')
		result = ""
		import pdb;pdb.set_trace()
		for atributoTwig in self.atributos:
			generador = self.getGenerador(atributoTwig.get('tipo'))
			generador.grupo = False
			result += "\n{%% set field = form.%s %%}" % atributoTwig.nombre
			result += generador.generarTwig(atributoTwig) + '\n'
		print '\n'*5
		print result
		print '\n'*5

	def mostrarAGenerar(self):
		os.system('clear')
		print '\ncola para generar:\n'

		for elemento in self.atributosAProcesar:
			if isinstance(elemento, tuple):
				print "Grupo %s" % elemento[0]
				for atributoGrupo in elemento[1]:
					print '\t -%s' % atributoGrupo.nombre
			else:
				print "- %s" % (elemento.nombre)

	def getGenerador(self,key):
		if key in self.generadores.keys():
			return self.generadores[key]
		else:
			return self.generadores['default']

	def generarTwig(self):
		os.system('clear')
		result = ""
		for atributoTwig in self.atributosAProcesar:
			if isinstance(atributoTwig, tuple):
				grupoStr = self.generadorGrupo.plantillaGrupo % atributoTwig[0]
				grupos = ""
				for atributo in atributoTwig[1]:
					generador = self.getGenerador(atributo.get('tipo'))
					generador.grupo = True
					grupos += generador.generar(atributo)
				result += grupoStr % grupos
			else:
				generador = self.getGenerador(atributoTwig.get('tipo'))
				generador.grupo = False
				result += "\n{%% set field = form.%s %%}" % atributoTwig.nombre
				result += generador.generarTwig(atributoTwig) + '\n'
		print result
		return result
# -*- encoding: utf-8 -*-
from GeneradorTwig import *
from ManejadorForm import ManejadorForm
import Interfaz
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
		self.generadores['image'] = GeneradorImage()
		self.generadores['OneToMany'] = GeneradorOneToMany()
		self.manejadorForm = ManejadorForm()
		self.generadorGrupo = GeneradorGrupo()
		self.path = None
		self.mensajes = []
		self.versionBootstap = 2
		self.parsearValor = re.compile('(?P<indice>\d+)$|(?P<rangoInferior>\d+)..(?P<rangoSuperior>\d+)')

	def imprimirError(self, error):
		print error

	def cambiarBootstrap(self):
		versionAnterior = self.versionBootstap
		self.versionBootstap = 2 + (self.versionBootstap +1) % 2 
		Interfaz.info('Se cambio de la version:%i por la version:%i' % (versionAnterior, self.versionBootstap))

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
		salvarProcesar = [x for x in self.atributosAProcesar]
		self.atributosAProcesar = [x for x in self.atributos]
		self.generarTwig()
		self.atributosAProcesar = salvarProcesar

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
			generador = self.generadores[key]
		else:
			generador =  self.generadores['default']

		if self.versionBootstap == 2:
			generador.bootstrap2 = True
		else:
			generador.bootstrap2 = False

		return generador

	def eliminarAtributosAsociadosImagen(self, atributoImage):
		nombre = atributoImage.nombre.partition('File')[0]
		for atributo in self.atributosAProcesar:
			if atributo.nombre.startswith(nombre) and atributo != atributoImage:
				self.atributosAProcesar.remove(atributo)


	def preProcesar(self):
		for atributo in self.atributosAProcesar:
			if atributo.get('tipo') == 'image':
				atributo_imagen = atributo
				self.eliminarAtributosAsociadosImagen(atributo)

	def definirPath(self):
		path = raw_input(Interfaz.buildColor('azul','Ingrese el nombre del path del traductor sin espacio en blanco. ejemplo:campus.modulos.aval.form\n'))
		if (path.find(' ') != -1):
			Interfaz.err('Ingresó con espacio')
		else :
			self.path = path

	def generarTwig(self):
		os.system('clear')
		result = ""
		self.preProcesar()
		for atributoTwig in self.atributosAProcesar:
			if isinstance(atributoTwig, tuple):
				grupoStr = self.generadorGrupo.plantillaGrupo % atributoTwig[0]
				grupos = ""
				for atributo in atributoTwig[1]:
					atributo.setPathTraductor(self.path)
					generador = self.getGenerador(atributo.get('tipo'))
					generador.grupo = True
					grupos += generador.generar(atributo)
				result += grupoStr % grupos
			else:
				if atributoTwig.nombre.lower() in ('id','translations', 'translationsproxy','create_at', 'update_at'):
					pass
				else:
					if atributoTwig.get('OneToMany', False): 
						generador = self.getGenerador('OneToMany')
					elif atributoTwig.get('ManyToOne', False): 
						generador = self.getGenerador('ManyToOne')
					else:
						generador = self.getGenerador(atributoTwig.get('tipo'))
					generador.grupo = False
					atributoTwig.setPathTraductor(self.path)
					result += "\n{%% set field = form.%s %%}" % atributoTwig.nombre
					result += generador.generarTwig(atributoTwig) + '\n'
		Interfaz.infog(result)
		return result

	def generarForm(self):
		self.manejadorForm.atributosAProcesar = self.atributosAProcesar
		self.manejadorForm.clase = self.clase
		self.manejadorForm.namespace = self.namespace
		Interfaz.infog(self.manejadorForm.generar())
		return

	def capitalizarConEspacios(self,string):
		result = ''
		for i, caracter in enumerate(string):
			if caracter.isupper() and i!=0:
				result += ' ' + caracter
			else :
				result += caracter
		return result.title()

	def generarConGuionBajo(self, string):
		result = []
		anterior = 0
		for i, x in enumerate(string):
			if x.isupper():
				result.append(string[anterior:i].lower())
				anterior = i

		result.append(string[anterior:].lower())
		if '' in result:
			result.remove('')
		if len(result) == 1:
			return result[0]
		return '_'.join(result)

	def generarTraducciones(self):
		tabulador = '  '

		for i, x in enumerate(self.namespace.partition('\\Entity')[2].split('\\')):
			if x != '':
				tabulador = '  '*i
				print '%s%s:' % (tabulador,self.generarConGuionBajo(x))
		tabulador = '  '*(i+1)
		print '%s%s:' % (tabulador,self.generarConGuionBajo(self.clase).lower())
		muchoAUno= []
		print '%s%s' % ('  '*(i+2), 'form:')
		print '%s%s' % ('  '*(i+3), 'label:')

		tabulador = '  ' * (i+4)
		for atributo in self.atributosAProcesar:
			if not atributo.nombre in ('id','createdBy','updatedBy','created','updated','translationsproxy', 'translations'):
				if atributo.get('OneToMany', False):
					muchoAUno.append(atributo)
				else:
					print tabulador + self.generarConGuionBajo(atributo.nombre) + ': ' + self.capitalizarConEspacios(atributo.nombre)
		if len(muchoAUno) > 0:
			print '%s%s' % ('  '* (i+3), 'legend:')
		for atributo in muchoAUno:
			print '%s%s: %s' % (tabulador, self.generarConGuionBajo(atributo.nombre), self.capitalizarConEspacios(atributo.nombre))
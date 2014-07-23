# -*- coding: utf-8 *-*
import getopt

class ValidadorGenerico():
	def __init__(self, obligatorias=[], opcionales=[],banderas=[]):
		self.error = False
		self.mensajes = []
		self.obligatorias = set(obligatorias)
		self.obligatoriasConGuion = set(['--'+ str(x) for x in self.obligatorias])			
		self.opcionales = set(opcionales)
		self.opcionalesConGuion = set(['--'+ str(x) for x in self.opcionales])
		self.banderas = set(banderas)
		self.banderasConGuion = set(['--'+ str(x) for x in self.banderas])
		self.opciones = self.opcionales.union(self.obligatorias)
		self.opcionesConGuion = set([ '--' + str(x) for x in self.opciones])
		self.opcionesParciadas = dict()
		self.parseado = False

	def setOpciones(self,obligatorias,opcionales,banderas):
		self.parseado = False
		self.obligatorias = set(obligatorias)
		self.obligatoriasConGuion = set(['--'+ str(x) for x in self.obligatorias])
		self.opcionales = set(opcionales)
		self.opcionalesConGuion = set(['--'+ str(x) for x in self.opcionales])
		self.banderas = set(banderas)
		self.banderasConGuion = set(['--'+ str(x) for x in self.banderas])
		self.opciones = self.opcionales.union(self.obligatorias)
		self.opcionesConGuion = set([ '--' + str(x) for x in self.opciones])

	def getOpcionesParsiadas(self):
		result = dict()
		for item in self.opcionesParciadas:
			result[item[0][2:]] = item[1]
		return result

	def estanConValores(self,argTuple):
		opciones = [x for x in self.opcionesConGuion]
		for x in argTuple:
			if x[0] in opciones and x[1] == '':
				self.mensajes.append('La opcion: %s necesita valor' % x[0])
				return False
		return True

	def sonParametrosCorrectos(self,argv):
		try:
			optsTuple, args = getopt.getopt(argv , '' , [str(x) + '=' for x in self.opciones] + [str(x) for x in self.banderas])
		except:
			self.error = True
			self.mensajes.append('Existen opciones no válidas')
			return False
		opts = [x for x,y in optsTuple ]
		if not set(opts).issubset(self.opcionesConGuion.union(self.banderasConGuion)):
			self.error = True
			diferencias = [str(x) for x in self.banderas.difference(set(args))]
			self.mensajes.append('Existen opciones no válidas : %s' % (','.join(diferencias)))

		elif not (set(opts).issuperset(self.obligatoriasConGuion)):
			self.error = True
			diferencias = [str(x) for x in self.obligatoriasConGuion.difference(set(opts))]
			import pdb;pdb.set_trace()
			self.mensajes.append('Le faltan los siguientes campos obligatorios:%s' %  (','.join(diferencias)) )
			return False
		elif not set(opts).issuperset(self.banderasConGuion):
			self.error = True
			diferencias = [str(x) for x in self.banderas.difference(set(args))]
			self.mensajes.append('La siguientes banderas no son valídas: %s' % (','.join(diferencias)))
		elif set(opts).issubset(self.opcionesConGuion.union(self.banderasConGuion)):
			self.opcionesParciadas = optsTuple
			return self.estanConValores(optsTuple)

	def validar(self):
		pass

class ValidadorEntradaTwig(ValidadorGenerico):
	"""docstring for ClassName"""
	def __init__(self):
		opcionesObligatorias = ['file']
		super(ClassName, self).__init__(opcionesObligatorias)

	# def validar(self,argv):
	# 	if  self.parametrosCorrectos():
	# 		if argv[1]
	# 	else:
	# 		return False
		
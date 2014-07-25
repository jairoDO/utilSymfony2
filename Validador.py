# -*- coding: utf-8 *-*
import getopt
import os
class ValidadorGenerico():
	def __init__(self, obligatorias=[], opcionales=[],banderas=[]):
		self.error = False
		self.optsTuple = None
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

	def getOpcion(self,key,default=''):
		return self.opcionesParciadas.get(key,default)

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
		for item in self.optsTuple:
			result[item[0][2:]] = item[1]
		self.opcionesParciadas = result
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
			self.optsTuple = optsTuple
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
			self.mensajes.append('Le faltan los siguientes campos obligatorios:%s' %  (','.join(diferencias)) )
			return False
		elif not set(opts).issuperset(self.banderasConGuion):
			self.error = True
			diferencias = [str(x) for x in self.banderas.difference(set(args))]
			self.mensajes.append('La siguientes banderas no son valídas: %s' % (','.join(diferencias)))
		elif set(opts).issubset(self.opcionesConGuion.union(self.banderasConGuion)):
			return self.estanConValores(optsTuple)

	def validar(self):
		pass

class ValidadorEntradaArchivo(ValidadorGenerico):
	"""docstring for ClassName"""
	def __init__(self):
		opcionesObligatorias = ['file']
		ValidadorGenerico.__init__(self, opcionesObligatorias)


	def validar(self,argv):
	 	if  self.sonParametrosCorrectos(argv):
	 		self.getOpcionesParsiadas()
	 		if os.path.exists(self.getOpcion('file')):
	 			return True
 			else:
 				self.mensajes.append('No existe el archivo %s' % self.getOpcion('file'))
	 	else:
	 		return False
	 	
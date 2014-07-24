import os
import re
from Atributo import Atributo

class Procesador():
	def _init_(self):
		self.procesadores = []

class ProcesadorGenerico():

	def __init__(self,patron,propiedad,opcion=None):
		if opcion is None:
			self.patron = re.compile(patron, re.MULTILINE | re.DOTALL)
		else:
			self.patron = re.compile(patron,opcion)
		self.propiedad = propiedad
		self.opcion = opcion
		self.procesado = None

	def machea(self, string):
		matcher = self.patron.match(string)
		#import pdb;pdb.set_trace()
		if matcher is None:
			return False	
			self.procesado = None
		else:
			self.procesado = matcher.groups()
			return True

	def procesar(self,string):
		if self.machea(string) :
			return self.devolverProcesado()
		else:
			return False

	""" este serviria de interfaz
	"""
	def devolverProcesado(self):
		pass

	def getPropiedad():
		return self.propiedades

class ProcesadorTipo(ProcesadorGenerico):
	def __init__(self):
		ProcesadorGenerico.__init__(self, '(.+)type="(.+)"(.*)', "tipo")

	def devolverProcesado(self):
		if self.procesado is None:
			return None
		else:
			posicionfinal = self.procesado[1].find('"') if self.procesado[1].find('"') != -1  else len(self.procesado[1])
			return self.procesado[1][0:posicionfinal]

class Parseador():
	atributos = []
	def __init__(self, name_file = ''):
		self.procesadores = [ProcesadorTipo()]
		if os.path.exists(name_file) :
			self.file = open(name_file,'rw')
			self.fileString = self.file.read()
			self.atributos = []
		else:
			self.file = None

	def agregarProcesador(self,procesador):
		if (isinstance(procesador, ProcesadorGenerico)):
			self.procesadores.append(procesador)

	def getNameSpace(self,string):
		patron = re.compile('namespace(\s+)(.+);', re.DOTALL )
		namespace = patron.search(string)
		return namespace.group(2).split(';')[0]

	def getDirectorio(self,string):
		return string.split('Entity')[-1].replace('\\','')
		
	def getAtributosProcesados(self):
		""" Devuelve una lista con los atributos que se encuentrar en el archivo, procesados, y aplicadando cada procesador
		"""
		fileString = self.fileString
		listaDeAtributosCrudos = self.parsearAtributos(fileString)
		listaDeAtributosAnotaciones = self.crearDictAnotaciones(fileString)
		listaAtributos = []
		for nombre , anotacion in listaDeAtributosAnotaciones.items():
			splitIGual = nombre.split("=")
			if len(splitIGual) > 1:
				nombre = splitIGual[0].strip()
				valorDefault =  splitIGual[1].strip()
				atributo = Atributo(nombre,anotacion)
				atributo.propiedades['default'] = valorDefault
			else:
				atributo = Atributo(nombre, anotacion)
			self.procesarAtributo(atributo)
			listaAtributos.append(atributo)

		return listaAtributos

	def setFile(self, Files):
		if type(Files) is file:
			self.file = Files
			self.fileString = self.file.read()

	def setFileExsist(self, name_file):
		if os.path.exists(name_file) :
			self.file = open(name_file,'rw')
			self.fileString = self.file.read()
			self.atributos = []
		else:
			self.file = None
			return False

	def getFile(self):
		return self.file

	def getListaAtributos(self):
		return self.atributos

	def parsearAtributos(self, string):
		""" devuelve todos los atributos que tiene una entidad sea o no con anotaciones
		"""
		patron = re.compile("(private|protected|public){1}(\s+)\$(.+);(\s*|\n+)*|cons\s(.+)\s=\s(.+);")
		result = []
		for x in patron.finditer(string):
			result.append(x.group(3))
		return result

	def crearDictAnotacionesRecursivo(self, string, dicAnotaciones):
			""" crea un diccionario con los atributos qeu tienen anotaciones 
			"""
			comienzo = string.find('/**')

			if comienzo == -1:
				return dicAnotaciones
			else:
				preAnotacion = string[comienzo:]
				restoCadena = string[comienzo:]
				finAnotacion = string.find('*/')
				if finAnotacion == -1:
					return dicAnotaciones
				else:
					anotacion = string[comienzo:finAnotacion+2]
					linea = string[finAnotacion:].split('\n')[1]
					lineaProcesada = self.parsearAtributos(linea)
					if len(lineaProcesada) > 0:
						dicAnotaciones[lineaProcesada[0]] = anotacion
					self.crearDictAnotacionesRecursivo(string[finAnotacion+len(linea):],dicAnotaciones)
	
	def crearDictAnotaciones(self, string):
		""" crea y devuelve un diccionario donde cada key es un atributo y el valor su anotacion
		"""
		dicts = {}
		self.crearDictAnotacionesRecursivo(string,dicts)
		#import pdb;pdb.set_trace()
		return dicts


	def parsearAtributosAnotaciones(self, string):
		patron = re.compile("^/\*\*\n(.*)\*\*/(\s+)(private|protected|public){1}(\s+)\$(.*);$",re.MULTILINE | re.DOTALL)
		result = []
		for x in patron.finditer(string):
			print x.groups()
			result.append(x.group(1))
		#import pdb; pdb.set_trace()
		return result

	def procesarAtributo(self, atributo):
		"""Procesa un atributo segun su anotacion, es decir por cada procesador aplica el macheo y agrega su propiedad
		"""
		for procesador in self.procesadores:
			if procesador.machea(atributo.anotacion):
				atributo.propiedades[procesador.propiedad] = procesador.devolverProcesado()

	def capitalizarConEspacios(self,string):
		result = ''
		for i, caracter in enumerate(string):
			if caracter.isupper() and i!=0:
				result += ' ' + caracter
			else :
				result += caracter
		return result.title()

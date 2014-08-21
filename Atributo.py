
class Atributo():
	def __init__(self,nombre,anotacion=''):
		self.nombre = nombre
		self.anotacion = anotacion
		self.propiedades = {}

	def agregarPropiedad(self,key, propiedad):
		self.propiedades[key] = propiedad

	def get(self, propiedad, default='default'):
		if propiedad in self.propiedades:
			return self.propiedades[propiedad]
		else:
			return default

	def setPathTraductor(self, path):
		if not path:
			pass
		else:
			self.propiedades['pathTraductor'] = path

	def getPathTraductor(self):
		return self.get('pathTraductor') + '.' + self.getNombre()
	
	def getNombre(self):
		if self.get('tipo') == 'image':
			return self.nombre.partition('File')[0]

		return self.nombre

	def __str__(self):
		result = "Nombre:" + self.nombre + '\n'
		for propiedad, value in self.propiedades.items():
			result += "\tpropiedad %s: valor : %s \n" % ( propiedad, value)
		return result
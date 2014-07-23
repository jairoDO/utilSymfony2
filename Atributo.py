
class Atributo():
	def __init__(self,nombre,anotacion=''):
		self.nombre = nombre
		self.anotacion = anotacion
		self.propiedades = {}

	def agregarPropiedad(self,key, propiedad):
		self.propiedades[key] = propiedad

	def get(self, propiedad):
		if propiedad in self.propiedades:
			return self.propiedades[propiedad]
		else:
			return False

	def getPathTraductor(self):
		return self.get('pathTraductor') + '.' + self.nombre

	def __str__(self):
		result = "Nombre:" + self.nombre + '\n'
		for propiedad, value in self.propiedades.items():
			result += "\tpropiedad %s: valor : %s \n" % ( propiedad, value)
		return result
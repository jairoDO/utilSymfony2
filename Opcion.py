class Opcion():
	def __init__(self,nombre,execs, descripcion="",ayuda=""):
		self.nombre = nombre
		self.execs = execs
		self.descripcion = descripcion
		self.ayuda = ayuda

	def getNombre(self):
		return self.nombre

	def imprimir(self):
		print "%s ) - %s" % (self.nombre, self.descripcion)
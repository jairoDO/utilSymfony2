class Opcion():
	def __init__(self,nombre,execs, descripcion="",ayuda=""):
		self.nombre = nombre
		self.execs = execs
		self.descripcion = descripcion
		self.ayuda = ayuda

	def ejecutar(self):
		exec(self.execs)
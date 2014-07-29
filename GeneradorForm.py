class GeneradorGenerico():
	def __init__(self,tipo):
		self.plantilla = "->add('%s','%s',%s)"
		self.tipo = tipo

	def generar(self,atributo):
		return self.plantilla % (atributo.nombre, 'null', 'array()')
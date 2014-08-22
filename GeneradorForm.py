# -*- coding: utf-8 *-*

class GeneradorGenerico():
	def __init__(self,tipo='default',tipoField ='null'):
		self.plantilla = "\n\t\t\t->add('%s', '%s', %s)"
		self.tipo = tipo
		self.tipoField = tipoField
		self.opcion = dict()

	def procesarOpcion(self, atributo):
		if atributo.get('required'):
			self.opcion['required'] = True
		else:
			self.opcion['required'] = False

	def getTipo(self):
		return self.tipoField

	def procesarAtributo(self, atributo):
		pass

	def generarOpcionString(self):
		result = []
		lista = list(self.opcion.items())
		lista.sort()
		for key, value in lista:
			if isinstance(value,str) and not value.startswith('array') and not value.startswith('$'):				
				result.append("'%s' => '%s'," % (key, value))
			else:
				result.append("'%s' => %s," % (key, value))

		resultString = ''
		if result != []:
			resultString = "\n\t\t\t\t".join([''] + result) + "\n\t\t\t"

		return "array(%s)" % resultString

	def generarForm(self,atributo):
		self.procesarOpcion(atributo)
		self.procesarAtributo(atributo)
		return self.plantilla % (atributo.nombre, self.getTipo(), self.generarOpcionString())

class GeneradorBooleano(GeneradorGenerico):
	def __init__(self):
		GeneradorGenerico.__init__(self,'boolean','checkbox')

class GeneradorString(GeneradorGenerico):
	def __init__(self):
		GeneradorGenerico.__init__(self, 'string','text')


class GeneradorImage(GeneradorGenerico):
	def __init__(self):
		GeneradorGenerico.__init__(self, 'image')

	def generarForm(self, atributo):
		plantilla ="""
			->add('%s', null, %s)
			->add('%sDelete', 'checkbox', %s)"""

		self.procesarOpcion(atributo)
		opcionString = self.generarOpcionString()
		return plantilla % (atributo.nombre, opcionString, atributo.getNombre(), opcionString)

	def getTipo(self):
		return 'file'

class GeneradorDate(GeneradorGenerico):
	def __init__(self):
		GeneradorGenerico.__init__(self, 'datetime','date')


	def procesarAtributo(self, atributo):
		self.opcion.update({'input': 'datetime','widget': 'choice','empty_value' : """array('year' => 'Ano', 'month' => 'Mes', 'day' => 'Dia')""",
                'required' : False,
                'years': '$years'})

class GeneradorText(GeneradorGenerico):
	def __init__(self):
		GeneradorGenerico.__init__(self, 'text', 'textarea')

class GeneradorOneToMany(GeneradorGenerico):
	def __init__(self):
		GeneradorGenerico.__init__(self, 'OneToMany', 'collection')

	def procesarAtributo(self, atributo):
		result = {}
		if 'persist' in atributo.get('OneToMany').get('cascade', []):
			result.update({'allow_add': False})
		else:
			result.update({'allow_add': False})

		if 'remove' in atributo.get('OneToMany').get('cascade', []):
			result.update({'allow_delete':True})
		else:
			result.update({'allow_add': False})

		nombreType = atributo.get('OneToMany')['targetEntity'].replace('Entity','Form') + 'Type()'

		result.update({'type': 'new ' + nombreType})
		result.update({'by_reference': False})
		result.update({'error_bubbling': False})
		self.opcion.update(result)

class GeneradorDecimal(GeneradorGenerico):
	def __init__(self):
		GeneradorGenerico.__init__(self,'decimal', 'number')

	def procesarAtributo(self,atributo):
		self.opcion.update({'grouping': True,'presicion': 3})

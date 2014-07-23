from Atributo import Atributo

class GeneradorGenerico():
	def __init__(self, plantilla,tipo=None, grupo=False):
		self.plantilla = plantilla
		self.tipo = tipo
		self.grupo = grupo

	def generar(self,atributo):
		pass #serviria como interfaz

class GeneradorBooleano(GeneradorGenerico):
	def __init__(self):
		plantilla = """
<div class="checkbox">
    <label>
      <input type="checkbox"> {{ form_label(field, '%s'|trans, { label_attr: { class: 'control-label' } }) }}
    </label>
</div>"""
		GeneradorGenerico.__init__(self, plantilla, 'boolean')

	def generar(self, atributo):
		return self.plantilla % (atributo.getPathTraductor())

class GeneradorText(GeneradorGenerico):
	
	def __init__(self):
		plantilla = """
<div class="form-group">
    {{ form_label(field, '%s'|trans, { label_attr: {class: 'col-lg-2 control-label'} }) }}
    <div class="col-lg-10">
        {{ form_widget(field, { attr: {class: 'form-control'} }) }}
        {{ form_errors(field) }}
    </div>
</div>"""
		GeneradorGenerico.__init__(self, plantilla, 'text')

	def generar(self, atributo):
		return self.plantilla % (atributo.getPathTraductor())

class GeneradorString(GeneradorGenerico):

	def __init__(self):
		plantilla = """
<div class="form-group">
    {{ form_label(field, '%s'|trans, { label_attr: {class: 'col-lg-2 control-label'} }) }}
    <div class="%s">
        {{ form_widget(field, { attr: {class: 'form-control'} }) }}
        {{ form_errors(field) }}
    </div>
</div>"""
		GeneradorGenerico.__init__(self, plantilla, 'string')

	def generar(self, atributo):
		if not atributo.get('length'):
			divClase = "col-lg-10"
		elif 2 <= atributo.get('length') <= 45:
			divClase = "col-lg-2"
		else:
			divClase = "col-lg-10"

		return self.plantilla % (atributo.getPathTraductor(), divClase)

class GeneradorDecimal(GeneradorGenerico):
	def __init__(self):
		plantilla = """
<div class="form-group">
    {{ form_label(field, '%s'|trans, { label_attr: {class: 'col-lg-2 control-label'} }) }}
    <div class="col-lg-2">
        {{ form_widget(field, { attr: {class: 'form-control'} }) }}
        {{ form_errors(field) }}
    </div>
</div>"""
		GeneradorGenerico.__init__(self, plantilla, 'decimal')

	def generar(self, atributo):
		return self.plantilla % (atributo.getPathTraductor())

class GeneradorBooleanoGrupo(GeneradorGenerico):

	def __init__(self):
		plantilla = """
        {%% set field = form.%s %%}
        <label class="checkbox-inline">
            {{ form_widget(field) }} {{ '%s'|trans }}
        </label>"""

		self.plantillaGrupo = """
<div class="form-group">
    <label class="col-lg-2 control-label">{{ '%s'|trans }}</label>
    <div class="col-lg-10">%s
    </div>
</div>
"""        
		GeneradorGenerico.__init__(self, plantilla, 'boolean', True)

	def generarBase(self, atributo):
		return self.plantilla % (atributo.nombre, atributo.getPathTraductor())

	def generar(self, nombre, listaAtributo):
		generados = ""
		for atributo in listaAtributo:
			generados +=  self.generarBase(atributo)

		return self.plantillaGrupo % (nombre, generados)

class GeneradorTwig():
	pass
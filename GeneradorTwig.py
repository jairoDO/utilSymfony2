from Atributo import Atributo

class GeneradorGenerico():

	def __init__(self, plantilla="", tipo=None, plantillaGrupo="",plantilla2=""):
		self.plantilla = plantilla
		self.plantilla2 = plantilla2
		self.tipo = tipo
		self.grupo = False
		self.bootstrap2 = False
		self.plantillaGrupo = plantillaGrupo

	def generarTwig(self,atributo):
		if self.grupo and self.plantillaGrupo != "":
			return self.generarGrupo(atributo)
		else:
			if self.bootstrap2:
				return self.generar2(atributo)
			else:
				return self.generar(atributo)


	def generarGrupo(self, atributo):
		pass #serviria como interfaz

	def generar2(self, atributo):
		pass  #serviria como interfaz

	def generar(self,atributo):
		pass #serviria como interfaz

class GeneradorDefault(GeneradorGenerico):

	def __init__(self):
		plantilla = """
<div class="">	
    <label>
      <input type=""> {{ form_label(field, '%s'|trans, { label_attr: { class: 'control-label' } }) }}
    </label>
</div>"""

		plantilla2 = """
        <div class="control-group">
            {{ form_label(field, '%s'|trans, { label_attr: { class: 'control-label' } }) }}
            <div class="controls">
                {{ form_widget(field, { attr: { class: 'span6' } }) }}
                {{ form_errors(field) }}
            </div>
        </div>"""

		plantillaGrupo = """
    {%% set field = form.%s %%}
    <label class="-inline">
        {{ form_widget(field) }} {{ '%s'|trans }}
    </label>"""

		GeneradorGenerico.__init__(self, plantilla, 'default', plantillaGrupo, plantilla2)

	def generar(self,atributo):
		return self.plantilla % (atributo.getPathTraductor())

	def generar2(self,atributo):
		return self.plantilla2 % (atributo.getPathTraductor())

	def generarGrupo(self,atributo):
		return self.plantillaGrupo % (atributo.nombre)

class GeneradorBooleano(GeneradorGenerico):

	def __init__(self):
		plantilla = """
<div class="checkbox">	
    <label>
      <input type="checkbox"> {{ form_label(field, '%s'|trans, { label_attr: { class: 'control-label' } }) }}
    </label>
</div>"""

		self.plantillaGrupo = """
        {%% set field = form.%s %%}
        <label class="checkbox-inline">
            {{ form_widget(field) }} {{ '%s'|trans }}
        </label>"""

		GeneradorGenerico.__init__(self, plantilla, 'boolean')

	def generar(self, atributo):
		return self.plantilla % (atributo.getPathTraductor())

	def generaGrupo(self,atributo):
		return self.plantillaGrupo % (atributo.nombre, atributo.getPathTraductor)

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
		
		plantilla2 = """
<div class="control-group">
    {{ form_label(field, '%s'|trans, { label_attr: { class: 'control-label' } }) }}
    <div class="controls">
        {{ form_widget(field, { attr: { class: 'span12', rows: 8 } }) }}
        {{ form_errors(field) }}
    </div>
</div>
"""
		GeneradorGenerico.__init__(self, plantilla, 'text',"", plantilla2)

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
		plantilla2 ="""
<div class="control-group">
    {{ form_label(field, '%s'|trans, { label_attr: { class: 'control-label' } }) }}
    <div class="controls">
        {{ form_widget(field, { attr: { class: 'span12' } }) }}
        {{ form_errors(field) }}
    </div>
</div>     
		"""
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

class GeneradorDatetime(GeneradorGenerico):
	def __init__(self):
		plantilla = """
<div class="control-group">
    {{ form_label(field, '%s'| trans, { label_attr: { class: 'control-label' } }) }}
    <div class="controls">
        {{ form_widget(field['day'], { attr: { class: 'span2' } }) }}
        {{ form_widget(field['month'], { attr: { class: 'span2' } }) }}            
        {{ form_widget(field['year'], { attr: { class: 'span2' } }) }}            
        {{ form_errors(field) }}
    </div>
</div>"""

		GeneradorGenerico.__init__(self, plantilla , 'datetime', "", plantilla)

	def generar(self, atributo):
		return self.plantilla % (atributo.getPathTraductor())

	def generar2(self, atributo):
		return self.plantilla2  % (atributo.getPathTraductor())

class GeneradorImage(GeneradorGenerico):
	def __init__(self):
		plantilla = """
<div class="control-group">
    {{ form_label(field, '%s'|trans, { label_attr: { class: 'control-label' } }) }}
    <div class="controls">
        {%% if form.vars.value.%s %%}
            <img class="img-polaroid" src="{{ ('uploads/%s/'~form.vars.value.%s)|imagine_filter('small') }}" />
            <label class="checkbox">{{ form_widget(form.%sDelete) }} 'abm.accion.eliminar'|trans </label>
        {%% endif %%}
        {{ form_widget(field) }}
        {{ form_errors(field) }}
    </div>
</div>"""
		
		GeneradorGenerico.__init__(self, plantilla , 'image', "", plantilla)

	def generar(self, atributo):
		return self.plantilla % (atributo.getPathTraductor(), atributo.nombre, atributo.propiedades['archivo'], atributo.nombre, atributo.nombre)

	def generar2(self, atributo):
		return self.plantilla2 % (atributo.getPathTraductor(), atributo.nombre, atributo.archivo, atributo.nombre, atributo.nombre)


class GeneradorGrupo():
	def __init__(self):
		self.plantillaGrupo = """
<div class="form-group">
    <label class="col-lg-2 control-label">{{ '%s'|trans }}</label>
    <div class="col-lg-10">%s
    </div>
</div>
""" 

	def generar(self, nombre):
		generados = "%s"
		return self.plantillaGrupo % (nombre, generados)


class GeneradorTwig():
	pass
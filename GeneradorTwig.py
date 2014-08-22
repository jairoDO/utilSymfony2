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
		return self.generar(atributo)

	def generar(self,atributo):
		pass #serviria como interfaz

class GeneradorDefault(GeneradorGenerico):

	def __init__(self):
		plantilla = """
<div class="control-group">
    {{ form_label(field, '%s'|trans, { label_attr: { class: 'control-label' } }) }}
    <div class="controls">
        {{ form_widget(field, { attr: { class: 'span6' } }) }}
        {{ form_errors(field) }}
    </div>
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

		GeneradorGenerico.__init__(self, plantilla2, 'default', plantillaGrupo, plantilla2)

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

		plantillaGrupo = """
        {%% set field = form.%s %%}
        <label class="checkbox-inline">
            {{ form_widget(field) }} {{ '%s'|trans }}
        </label>"""

		GeneradorGenerico.__init__(self, plantilla, 'boolean', plantillaGrupo,plantilla)

	def generar(self, atributo):
		return self.plantilla % (atributo.getPathTraductor())

	def generarGrupo(self,atributo):
		return self.plantillaGrupo % (atributo.nombre, atributo.getPathTraductor())

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

	def generador2(self, atributo):
		return self.plantilla2 % atributo.getPathTraductor()

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
		GeneradorGenerico.__init__(self, plantilla, 'string',"", plantilla2)

	def generar2(self, atributo):
		return self.plantilla2 % atributo.getPathTraductor()

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
		GeneradorGenerico.__init__(self, plantilla, 'decimal', "", plantilla)

	def generar2(self, atributo):
		return self.plantilla2 % (atributo.getPathTraductor())

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
		return self.plantilla % (atributo.getPathTraductor(), atributo.getNombre(), atributo.propiedades['archivo'], atributo.getNombre(), atributo.getNombre())

	def generar2(self, atributo):
		return self.plantilla2 % (atributo.getPathTraductor(), atributo.getNombre(), atributo.propiedades['archivo'	], atributo.getNombre(), atributo.getNombre())

class GeneradorOneToMany(GeneradorGenerico):
	def __init__(self):
		plantilla = """
{# collection: %s #}
<fieldset>
    <legend>{{ '%slegend.%s'|trans }}</legend>

    {{ form_errors(form.%s) }}

    <div data-collection="%s" data-prototype="{{ _self.%s(form.%s.vars.prototype)|e }}">
        {%% for %s in form.%s %%}
            {{ _self.%s(%s) }}
        {%% endfor %%}
    </div>

    <div class="form-group">
        <div class="col-lg-offset-2 col-lg-10">
            <button class="btn btn-default btn-sm" data-collection-add="%s">
                <span class="glyphicon glyphicon-plus"></span>
            </button>
        </div>
    </div>
</fieldset>
{# /collection: %s #}

{# Macros #}
{%% macro %s(%s) %%}
    <div class="form-group">
        {{ form_label(%s.%s, '%s%s'|trans, { label_attr: {class: 'col-lg-2 control-label'} }) }}
        <div class="col-lg-10">
            <div class="input-group">
            	{{ form_widget(seccion.seccion, { attr: {class: 'form-control'} }) }}
	            <span class="input-group-btn">
		            <button class="btn btn-default" data-collection-del="%s" data-collection-parent-to-remove=".form-group">
		                <span class="glyphicon glyphicon-minus"></span>
		            </button>
	            </span>
            </div>
            {{ form_errors(%s.%s) }}
        </div>
    </div>
{%% endmacro %%}
{# /Macros#}
"""
		GeneradorGenerico.__init__(self, plantilla, 'OneToMany',  plantilla)

	def generar(self, atributo):
		path  = atributo.getPathTraductor()
		nombreCorto = self.getNombreSimple(atributo.get('OneToMany').get('targetEntity'))
		pathLegend = self.getNombrelegend(path)
		nombre = atributo.getNombre()
		pathLabel = self.getPathLabel(path,nombre)
		return self.plantilla % (nombre, pathLegend, nombre, nombre,nombre,nombre,nombre,nombreCorto,nombre,nombre,nombreCorto,nombre,nombre,nombre,nombreCorto,nombreCorto,nombreCorto,pathLabel,nombreCorto,nombre,nombreCorto,nombreCorto)

	def getNombreSimple(self,nombre):
		return nombre.split('\\')[-1].lower()

	def getPathLabel(self, path,nombre):
		return path.partition(nombre)[0]

	def getNombrelegend(self,nombre):
		return nombre.partition('label')[0]

class GeneradorGrupo():
	def __init__(self):
		self.plantillaGrupo = """
<div class="form-group">
    <label class="col-lg-2 control-label">{{ '%s'|trans }}</label>
    <div class="col-lg-10">%s
    </div>
</div>
""" 
		self.plantillaAsignacion = "\n\t{%% set field = form.%s %%}"

	def generar(self, nombre):
		generados = "%s"
		return self.plantillaGrupo % (nombre, generados)


class GeneradorTwig():
	pass
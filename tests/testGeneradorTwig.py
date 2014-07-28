import unittest
import os
import sys

sys.path.append('../')
from GeneradorTwig import *
from Atributo import Atributo
#from ImpresorTwig import ImpresorTwig

class TddGenerarTwig(unittest.TestCase):

	def setUp(self):				
		self.generador = GeneradorTwig()

	def test_generarTwigAtributo_boolean(self):
		atributo = Atributo('tieneBeneficios')
		atributo.agregarPropiedad('tipo' , 'boolean')
		atributo.agregarPropiedad('pathTraductor','entidad.capacitacion.aval.form.label')
		resultado = """
<div class="checkbox">
    <label>
      <input type="checkbox"> {{ form_label(field, 'entidad.capacitacion.aval.form.label.tieneBeneficios'|trans, { label_attr: { class: 'control-label' } }) }}
    </label>
</div>"""
		self.failUnlessEqual(resultado, GeneradorBooleano().generar(atributo))

	def test_generarTwigAtributo_text(self):
		atributo = Atributo('descripcion')
		atributo.agregarPropiedad('tipo','text')
		atributo.agregarPropiedad('pathTraductor','entidad.capacitacion.aval.form.label')
		resultado = """
<div class="form-group">
    {{ form_label(field, 'entidad.capacitacion.aval.form.label.descripcion'|trans, { label_attr: {class: 'col-lg-2 control-label'} }) }}
    <div class="col-lg-10">
        {{ form_widget(field, { attr: {class: 'form-control'} }) }}
        {{ form_errors(field) }}
    </div>
</div>"""
		self.failUnlessEqual(resultado, GeneradorText().generar(atributo))

	def test_generarTwigAtributo_string(self):
		atributo = Atributo('nombre')
		atributo.agregarPropiedad('tipo','string')
		atributo.agregarPropiedad('pathTraductor','entidad.capacitacion.aval.form.label')
		resultado = """
<div class="form-group">
    {{ form_label(field, 'entidad.capacitacion.aval.form.label.nombre'|trans, { label_attr: {class: 'col-lg-2 control-label'} }) }}
    <div class="col-lg-10">
        {{ form_widget(field, { attr: {class: 'form-control'} }) }}
        {{ form_errors(field) }}
    </div>
</div>"""
	
		self.failUnlessEqual(resultado, GeneradorString().generar(atributo))

	def test_generarTwigAtributo_string_length_2(self):
		atributo = Atributo('idioma')
		atributo.agregarPropiedad('tipo','string')
		atributo.agregarPropiedad('length', 2)
		atributo.agregarPropiedad('pathTraductor','entidad.capacitacion.aval.form.label')
		resultado = """
<div class="form-group">
    {{ form_label(field, 'entidad.capacitacion.aval.form.label.idioma'|trans, { label_attr: {class: 'col-lg-2 control-label'} }) }}
    <div class="col-lg-2">
        {{ form_widget(field, { attr: {class: 'form-control'} }) }}
        {{ form_errors(field) }}
    </div>
</div>"""
	
		self.failUnlessEqual(resultado, GeneradorString().generar(atributo))

	def test_generarTwigAtributo_string_length_45(self):
		atributo = Atributo('tipo')
		atributo.agregarPropiedad('tipo','string')
		atributo.agregarPropiedad('length', 45)
		atributo.agregarPropiedad('pathTraductor','entidad.capacitacion.aval.form.label')
		resultado = """
<div class="form-group">
    {{ form_label(field, 'entidad.capacitacion.aval.form.label.tipo'|trans, { label_attr: {class: 'col-lg-2 control-label'} }) }}
    <div class="col-lg-2">
        {{ form_widget(field, { attr: {class: 'form-control'} }) }}
        {{ form_errors(field) }}
    </div>
</div>"""
	
		self.failUnlessEqual(resultado, GeneradorString().generar(atributo))

	def test_generarTwigAtributo_decimal(self):
		atributo = Atributo('tipo')
		atributo.agregarPropiedad('tipo','decimal')
		atributo.agregarPropiedad('length', 45)
		atributo.agregarPropiedad('pathTraductor','entidad.capacitacion.aval.form.label')
		resultado = """
<div class="form-group">
    {{ form_label(field, 'entidad.capacitacion.aval.form.label.tipo'|trans, { label_attr: {class: 'col-lg-2 control-label'} }) }}
    <div class="col-lg-2">
        {{ form_widget(field, { attr: {class: 'form-control'} }) }}
        {{ form_errors(field) }}
    </div>
</div>"""
	
		self.failUnlessEqual(resultado,GeneradorDecimal().generar(atributo))

	def test_generarTwigDatetime(self):
		atributo = Atributo('fecha')
		atributo.agregarPropiedad('tipo','datetime')
		atributo.agregarPropiedad('pathTraductor', 'entidad.capacitacion.aval.form.label')
		resultado = """
<div class="control-group">
    {{ form_label(field, 'entidad.capacitacion.aval.form.label'| trans, { label_attr: { class: 'control-label' } }) }}
    <div class="controls">
        {{ form_widget(field['day'], { attr: { class: 'span2' } }) }}
        {{ form_widget(field['month'], { attr: { class: 'span2' } }) }}            
        {{ form_widget(field['year'], { attr: { class: 'span2' } }) }}            
        {{ form_errors(field) }}
    </div>
</div>"""		
		
		self.failUnlessEqual(resultado,GeneradorDatetime().generar(atributo))

	def test_generarTwigAtributoBooleanoGrupo_simple(self):
		atributo = Atributo('esAlgunaPropiedad')
		atributo.agregarPropiedad('tipo','boolean')
		atributo.agregarPropiedad('pathTraductor','entidad.capacitacion.aval.form.label')
		resultado = """
        {% set field = form.esAlgunaPropiedad %}
        <label class="checkbox-inline">
            {{ form_widget(field) }} {{ 'entidad.capacitacion.aval.form.label.esAlgunaPropiedad'|trans }}
        </label>"""

		self.failUnlessEqual(resultado, GeneradorBooleanoGrupo().generarBase(atributo))


	def test_generarTwigAtributoImage(self):
		atributo = Atributo('foto')
		atributo.agregarPropiedad('tipo','image')
		atributo.agregarPropiedad('pathTraductor','entidad.institucion.aval.form.label')
		atributo.agregarPropiedad('archivo','Institucion')

		resultado = """
<div class="control-group">
    {{ form_label(field, 'entidad.institucion.aval.form.label'|trans, { label_attr: { class: 'control-label' } }) }}
    <div class="controls">
        {%% if form.vars.value.foto %%}
            <img class="img-polaroid" src="{{ ('uploads/Institucion/'~form.vars.value.foto)|imagine_filter('small') }}" />
            <label class="checkbox">{{ form_widget(form.fotoDelete) }} 'abm.accion.eliminar'|trans </label>
        {%% endif %%}
        {{ form_widget(field) }}
        {{ form_errors(field) }}
    </div>
</div>"""
	
		self.failUnlessEqual(resultado, GeneradorImage().generar(atributo))

	def test_generarTwigAtributoBooleanoGrupo(self):
		atributo = Atributo('esAlgunaPropiedad')
		atributo.agregarPropiedad('tipo','boolean')
		atributo.agregarPropiedad('pathTraductor','entidad.capacitacion.aval.form.label')
		atributo2 = Atributo('esOtraPropiedad')
		atributo2.agregarPropiedad('tipo','boolean')
		atributo2.agregarPropiedad('pathTraductor','entidad.capacitacion.aval.form.label')
		lista = [atributo,atributo2]

		resultado = """
<div class="form-group">
    <label class="col-lg-2 control-label">{{ 'admin.certificado._form.destinado_a'|trans }}</label>
    <div class="col-lg-10">
        {% set field = form.esAlgunaPropiedad %}
        <label class="checkbox-inline">
            {{ form_widget(field) }} {{ 'entidad.capacitacion.aval.form.label.esAlgunaPropiedad'|trans }}
        </label>
        {% set field = form.esOtraPropiedad %}
        <label class="checkbox-inline">
            {{ form_widget(field) }} {{ 'entidad.capacitacion.aval.form.label.esOtraPropiedad'|trans }}
        </label>
    </div>
</div>
"""		
		self.failUnlessEqual(resultado[570:], GeneradorBooleanoGrupo().generar('admin.certificado._form.destinado_a',lista)[570:])

#	def test_imprimir_checbox(self):
#		atributo
if __name__ == "__main__":
	unittest.main()
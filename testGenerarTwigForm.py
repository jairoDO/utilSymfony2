import unittest
import os
from Parseador import Parseador, ProcesadorTipo
from Atributo import Atributo
#from ImpresorTwig import ImpresorTwig

class TddGenerarHtmlForm(unittest.TestCase):

	def setUp(self):				
		self.parseador = Parseador()

	def test_getNameSpace_correcto_una_linea(self):
		self.failUnlessEqual('gse\appBundle\Entity\certificad', self.parseador.getNameSpace("namespace gse\appBundle\Entity\certificad;"))

	def test_getNameSpace_correcto_multiple_linea(self):
		string = """
		<?php

		namespace Gse\Campus2Bundle\Entity\Certificado;

		use Doctrine\ORM\Mapping as ORM;
		use Symfony\Component\Validator\Constraints as Assert;
		"""
		self.failUnlessEqual('Gse\Campus2Bundle\Entity\Certificado', self.parseador.getNameSpace(string))

	def test_getDirectorio_bien(self):
		string = "Gse\AppBundle\Entity\Certificado"
		self.failUnlessEqual('Certificado',self.parseador.getDirectorio(string))


	def test_getDirectorio_base(self):
		string = "Gse\AppBundle\Entity"
		self.failUnlessEqual('',self.parseador.getDirectorio(string))

	def test_capitalizar_con_espacio_una_palabra(self):
		string = "alto"
		self.failUnlessEqual('Alto',self.parseador.capitalizarConEspacios(string))

	def test_capitalizar_con_espacio_dos_palabra(self):
		string = "AltoBaile"
		self.failUnlessEqual('Alto Baile',self.parseador.capitalizarConEspacios(string))

	def test_generarTwigAtributo_boolean(test):
		atributo = Atributo('tieneBeneficios')
		atributo.agregarPropiedad('tipo' , 'boolean')
		atributo.agregarPropiedad('pathTraductor','entidad.capacitacion.aval.form.label')
		resultado = """<div class="checkbox">
    <label>
      <input type="checkbox"> {{ form_label(field, 'entidad.capacitacion.aval.form.label.tieneBeneficios'|trans, { label_attr: { class: 'control-label' } }) }}
    </label>
  </div>"""
		self.failUnlessEqual(resultado, self.parseador.generarTwigBooleano(atributo))

	def test_generarTwigAtributo_text(self):
		atributo = Atributo('descripcion')
		atributo.agregarPropiedad('tipo','text')
		atributo.agregarPropiedad('pathTraductor','entidad.capacitacion.aval.form.label')
		resultado = """<div class="form-group">
    {{ form_label(field, 'entidad.capacitacion.aval.form.label.descripcion'|trans, { label_attr: {class: 'col-lg-2 control-label'} }) }}
    <div class="col-lg-10">
        {{ form_widget(field, { attr: {class: 'form-control'} }) }}
        {{ form_errors(field) }}
    </div>
</div>"""
		self.failUnlessEqual(resultado,self.generarTwigText(atributo))

	def test_generarTwigAtributo_string(self):
		atributo = Atributo('nombre')
		atributo.agregarPropiedad('tipo','string')
		atributo.agregarPropiedad('pathTraductor','entidad.capacitacion.aval.form.label')
		resultado = """<div class="form-group">
    {{ form_label(field, 'entidad.capacitacion.aval.form.label.nombre'|trans, { label_attr: {class: 'col-lg-2 control-label'} }) }}
    <div class="col-lg-10">
        {{ form_widget(field, { attr: {class: 'form-control'} }) }}
        {{ form_errors(field) }}
    </div>
</div>"""
	
	self.failUnlessEqual(resultado,self.generarTwigText(atributo))

	def test_generarTwigAtributo_string_length_2(self):
		atributo = Atributo('idioma')
		atributo.agregarPropiedad('tipo','string')
		atributo.agregarPropiedad('length', 2)
		atributo.agregarPropiedad('pathTraductor','entidad.capacitacion.aval.form.label')
		resultado = """<div class="form-group">
    {{ form_label(field, 'entidad.capacitacion.aval.form.label.idioma'|trans, { label_attr: {class: 'col-lg-2 control-label'} }) }}
    <div class="col-lg-2">
        {{ form_widget(field, { attr: {class: 'form-control'} }) }}
        {{ form_errors(field) }}
    </div>
</div>"""
	
	self.failUnlessEqual(resultado,self.generarTwigText(atributo))

	def test_generarTwigAtributo_string_length_44(self):
		atributo = Atributo('tipo')
		atributo.agregarPropiedad('tipo','string')
		atributo.agregarPropiedad('length', 45)
		atributo.agregarPropiedad('pathTraductor','entidad.capacitacion.aval.form.label')
		resultado = """<div class="form-group">
    {{ form_label(field, 'entidad.capacitacion.aval.form.label.tipo'|trans, { label_attr: {class: 'col-lg-2 control-label'} }) }}
    <div class="col-lg-2">
        {{ form_widget(field, { attr: {class: 'form-control'} }) }}
        {{ form_errors(field) }}
    </div>
</div>"""
	
	self.failUnlessEqual(resultado,self.generarTwigText(atributo))

	def test_generarTwigAtributo_decimal(self):
		atributo = Atributo('tipo')
		atributo.agregarPropiedad('tipo','decimal')
		atributo.agregarPropiedad('length', 45)
		atributo.agregarPropiedad('pathTraductor','entidad.capacitacion.aval.form.label')
		resultado = """<div class="form-group">
    {{ form_label(field, 'entidad.capacitacion.aval.form.label.tipo'|trans, { label_attr: {class: 'col-lg-2 control-label'} }) }}
    <div class="col-lg-2">
        {{ form_widget(field, { attr: {class: 'form-control'} }) }}
        {{ form_errors(field) }}
    </div>
</div>"""
	
	self.failUnlessEqual(resultado,self.generarTwigText(atributo))

#	def test_imprimir_checbox(self):
#		atributo
if __name__ == "__main__":
	unittest.main()
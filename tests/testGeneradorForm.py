# -*- coding: utf-8 *-*
import unittest
import os
import sys

sys.path.append('../')
from GeneradorForm import *
from Atributo import Atributo

class TddGenerarForm(unittest.TestCase):

	def test_generadorGenerico_generarOpcionString_vacio(self):
		generador = GeneradorGenerico()
		resultado = "array()"
		self.failUnlessEqual(resultado, generador.generarOpcionString())

	def test_generadorGenerico_generarOpcionString_con_required(self):
		generador = GeneradorGenerico()
		generador.opcion = {'required': True}
		resultado = """array(
				'required' => True,
			)"""
		self.failUnlessEqual(resultado, generador.generarOpcionString())

	def test_generadorGenerico_generarOpcionString_empty_value(self):
		generador = GeneradorGenerico()
		generador.opcion = {'empty_value': ''}
		resultado = """array(
				'empty_value' => '',
			)"""
		self.failUnlessEqual(resultado, generador.generarOpcionString())

	def test_generadorGenerico_generarOpcionString_con_required_y_max_length(self):
		generador = GeneradorGenerico()
		generador.opcion = {'required': True}
		generador.opcion['max_length'] = 3
		resultado = """array(
				'max_length' => 3,
				'required' => True,
			)"""

		self.failUnlessEqual(resultado, generador.generarOpcionString())

	def test_generarTwigAtributo_boolean_requerido(self):
		atributo = Atributo('tieneBeneficios')
		atributo.agregarPropiedad('tipo' , 'boolean')
		atributo.agregarPropiedad('pathTraductor','entidad.capacitacion.aval.form.label')
		atributo.agregarPropiedad('required', True)
		resultado = """
			->add('tieneBeneficios', 'checkbox', array(
				'required' => True,
			))"""

		self.failUnlessEqual(resultado, GeneradorBooleano().generarForm(atributo))

	def test_generarTwigAtributo_boolean_not_requerido(self):
		atributo = Atributo('tieneBeneficios')
		atributo.agregarPropiedad('tipo' , 'boolean')
		atributo.agregarPropiedad('required', False)
		resultado = """
			->add('tieneBeneficios', 'checkbox', array(
				'required' => False,
			))"""

		self.failUnlessEqual(resultado, GeneradorBooleano().generarForm(atributo))


	def test_generarTwigAtributo_text(self):
		atributo = Atributo('descripcion')
		atributo.agregarPropiedad('tipo','text')
		atributo.agregarPropiedad('required', False)

		resultado = """
			->add('descripcion', 'textarea', array(
				'required' => False,
			))"""

		self.failUnlessEqual(resultado, GeneradorText().generarForm(atributo))

	def test_generarTwigAtributo_string(self):
		atributo = Atributo('nombre')
		atributo.agregarPropiedad('tipo','string')
		atributo.agregarPropiedad('required', False)
		resultado = """
			->add('nombre', 'text', array(
				'required' => False,
			))"""

		self.failUnlessEqual(resultado, GeneradorString().generarForm(atributo))

	def test_generarTwigAtributo_string_length_2(self):
		atributo = Atributo('idioma')
		atributo.agregarPropiedad('tipo','string')
		atributo.agregarPropiedad('length', 2)
		atributo.agregarPropiedad('required', False)
		resultado = """
			->add('idioma', 'text', array(
				'required' => False,
			))"""
	
		self.failUnlessEqual(resultado, GeneradorString().generarForm(atributo))

	def test_generarTwigAtributo_string_length_45(self):
		atributo = Atributo('tipo')
		atributo.agregarPropiedad('tipo','string')
		atributo.agregarPropiedad('length', 45)
		atributo.agregarPropiedad('required', False)
		resultado = """
			->add('tipo', 'text', array(
				'required' => False,
			))"""
	
		self.failUnlessEqual(resultado, GeneradorString().generarForm(atributo))

	def test_generarTwigAtributo_decimal(self):
		atributo = Atributo('tipo')
		atributo.agregarPropiedad('tipo','decimal')
		atributo.agregarPropiedad('length', 45)
		atributo.agregarPropiedad('required', False)
		resultado = """
			->add('tipo', 'number', array(
				'grouping' => True,
				'presicion' => 3,
				'required' => False,
			))"""
	
		self.failUnlessEqual(resultado,GeneradorDecimal().generarForm(atributo))

	def test_generarTwigDate(self):
		atributo = Atributo('fecha')
		atributo.agregarPropiedad('tipo','date')
		atributo.agregarPropiedad('required', False)
		
		resultado = """
			->add('fecha', 'date', array(
				'empty_value' => array('year' => 'Ano', 'month' => 'Mes', 'day' => 'Dia'),
				'input' => 'datetime',
				'required' => False,
				'widget' => 'choice',
				'years' => $years,
			))"""		

		self.failUnlessEqual(resultado,GeneradorDate().generarForm(atributo))

	def test_generarTwigAtributoImage(self):
		atributo = Atributo('fotoFile')
		atributo.agregarPropiedad('tipo','image')
		atributo.agregarPropiedad('archivo','Institucion')
		atributo.agregarPropiedad('required', False)
		resultado = """
			->add('fotoFile', null, array(
				'required' => False,
			))
			->add('fotoDelete', 'checkbox', array(
				'required' => False,
			))"""
	
		self.failUnlessEqual(resultado, GeneradorImage().generarForm(atributo))

#	def test_imprimir_checbox(self):
#		atributo
if __name__ == "__main__":
	unittest.main()
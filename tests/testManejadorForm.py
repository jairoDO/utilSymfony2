import unittest
import os
import sys

sys.path.append('../')
from Parseador import Parseador, ProcesadorTipo, ProcesadorGenerico
from Atributo import Atributo
from ManejadorForm import ManejadorForm
from Validador import ValidadorEntradaArchivo

class TddManejadorForm(unittest.TestCase):

	def setUp(self):
		self.manejador = ManejadorForm()
		self.manejador.namespace =  'Gse\AppBundle\Entity'
		self.manejador.clase = 'Institucion'

	def primera_diferencia(self, primero, segundo):
		contador = 0
		for primer , segund in zip(list(primero), list(segundo)):
			if primer != segund:
				print 'diferencia \033[91m %s != %s \033[0m' % (primero[contador - 10 :contador + 10],segundo[contador -10:contador+ 10])
				diff = (str(list(primero[contador - 10 :contador])), str(list(primero[contador])), str(list(primero[contador:contador + 10])),str(list(segundo[contador -10:contador+ 1])), str(list(segundo[contador])), str(list(segundo[contador:contador +10])))
				print 'diferencia \033[91m %s \033[0m \033[92m %s \033[0m  \033[91m%s !=   %s \033[0m  \033[92m %s \033[0m \033[91m %s \033[0m' % diff
				
				print 'en la posicion \033[91m %i \033[0m' % contador
				return False
			contador +=1

	def test_crear_nameSpace(self):
		resultado ="Gse\AppBundle\Form\Admin"
		self.manejador.namespace =  'Gse\AppBundle\Entity\Admin'
		self.failUnlessEqual(resultado, self.manejador.crearNameSpace())

	def test_crear_nameSpace(self):
		resultado ="Gse\AppBundle\Form"
		self.manejador.namespace =  'Gse\AppBundle\Entity'
		self.failUnlessEqual(resultado, self.manejador.crearNameSpace())

	def test_crear_nombre(self):
		resultado ="gse_app_institucion"
		self.manejador.namespace =  'Gse\AppBundle\Entity'
		self.clase = 'Institucion'
		self.failUnlessEqual(resultado, self.manejador.crearNombre())

	def test_crear_nombre_subcarpeta(self):
		resultado ="gse_app_admin_institucion"
		self.manejador.namespace =  'Gse\AppBundle\Entity\Admin'
		self.clase = 'Institucion'
		self.failUnlessEqual(resultado, self.manejador.crearNombre())

	def test_crear_nameSpace_vacio(self):
		self.manejador.namespace =  ''
		self.failUnlessEqual('', self.manejador.crearNameSpace())

	def test_generar_vacio(self):
		self.manejador.atributosAProcesar = []
		resultado = ''
		self.failUnlessEqual(resultado, self.manejador.generar())

	def test_generar_un_atributo(self):
		atributo = Atributo('esAlgunaPropiedad')
		atributo.agregarPropiedad('tipo','boolean')
		atributo.agregarPropiedad('required', False)
		atributo.agregarPropiedad('pathTraductor','entidad.capacitacion.aval.form.label')
		self.namespace = 'Gse\AppBundle\Entity'
		self.clase = 'Institucion'
		self.manejador.atributosAProcesar = [atributo]
		resultado = """<?php

namespace Gse\AppBundle\Form;

use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\Form\FormEvent;
use Symfony\Component\Form\FormEvents;
use Symfony\Component\OptionsResolver\OptionsResolverInterface;
use Symfony\Component\Form\FormInterface;

class InstitucionType extends AbstractType
{
	public function buildForm(FormBuilderInterface $builder, array $options)
	{
		$builder
			->add('esAlgunaPropiedad', 'checkbox', array(
				'required' => False,
			));
	}

	public function setDefaultOptions(OptionsResolverInterface $resolver)
	{
		$resolver->setDefaults(array(
			'data_class' => 'Gse\AppBundle\Entity\Institucion',
		));
	}

	public function getName()
	{
		return 'gse_app_institucion';
	}
}
"""
		self.primera_diferencia(resultado, self.manejador.generar())
		self.failUnlessEqual(resultado, self.manejador.generar())

if __name__ == "__main__":
	unittest.main()
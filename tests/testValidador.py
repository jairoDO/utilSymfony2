# -*- coding: utf-8 *-*

import unittest
import os
import sys

sys.path.append('../')
from Parseador import Parseador
from Validador import ValidadorEntradaArchivo, ValidadorGenerico

class TestValidadorGenerico(unittest.TestCase):
	def setUp(self):
		self.validador = ValidadorGenerico()

	def test_validar_bien_obligatorios_bien_opcionales(self):
		opcionales = ['opcional1', 'opcional2']
		obligatorias = ['obligatoria1', 'obligatoria2']
		banderas = ['x','tag']
		argv = '--opcional1=1 --opcional2=Ere   --obligatoria1=4 --x --tag --obligatoria2=3 '.split()
		self.validador.setOpciones( obligatorias,opcionales, banderas)

		self.assertTrue(self.validador.sonParametrosCorrectos(argv))
		self.failUnlessEqual({'opcional1':'1', 'opcional2': 'Ere', 'obligatoria1':'4','obligatoria2':'3','x':'','tag':''}, self.validador.getOpcionesParsiadas())

	def test_validar_bien_obligatoria_falta_opcionales(self):
		opcionales = ['opcional1', 'opcional2']
		obligatorias = ['obligatoria1', 'obligatoria2']
		banderas = ['x','tag']
		argv = '--opcional1=1  --obligatoria1=4 --x --tag --obligatoria2=3 '.split()

		self.validador.setOpciones(obligatorias,opcionales, banderas)

		self.assertTrue(self.validador.sonParametrosCorrectos(argv))
		self.failUnlessEqual({'opcional1':'1', 'obligatoria1':'4','obligatoria2':'3','x':'','tag':''}, self.validador.getOpcionesParsiadas())

	def test_validar_falta_obligatoria_falta_opcionales(self):
		opcionales = ['opcional1', 'opcional2']
		obligatorias = ['obligatoria1', 'obligatoria2']
		banderas = ['x','tag']
		argv = '--opcional1=1  --x --tag --obligatoria2=3 '.split()

		self.validador.setOpciones(obligatorias,opcionales, banderas)

		self.assertTrue(not self.validador.sonParametrosCorrectos(argv))

	def test_validar_bien_obligatoria_bien_opcionales_con_datos_desconocido(self):
		opcionales = ['opcional1', 'opcional2']
		obligatorias = ['obligatoria1', 'obligatoria2']
		banderas = ['x','tag']
		argv = '--opcional1=1 --opcional2=2 --opcional3=5 --obligatoria1=4 --x --tag --obligatoria2=3 '.split()

		self.validador.setOpciones(obligatorias,opcionales, banderas)

		self.assertTrue(not self.validador.sonParametrosCorrectos(argv))
		self.failUnlessEqual('Existen opciones no válidas', self.validador.mensajes[0])

	def test_validar_bien_obligatoria_bien_opcionales_sin_valores(self):
		opcionales = ['opcional1', 'opcional2']
		obligatorias = ['obligatoria1', 'obligatoria2']
		banderas = ['x','tag']
		argv = '--opcional1=1 --opcional2= --obligatoria1=4 --x --tag --obligatoria2=3 '.split()

		self.validador.setOpciones(obligatorias,opcionales, banderas)

		self.assertTrue(not self.validador.sonParametrosCorrectos(argv))
		self.failUnlessEqual('La opcion: --opcional2 necesita valor', self.validador.mensajes[0])

class TestValidadorTwig(unittest.TestCase):

	def setUp(self):
		self.validador = ValidadorEntradaArchivo()

	def test_archivo_valido(self):
		filePrueba = open('prueba.php','wr')
		argv = '--file=prueba.php'.split()
		self.assertTrue(self.validador.validar(argv))

	def test_archivo_invalido(self):
		argv = '--file=invalido'.split()
		self.assertTrue(not self.validador.validar(argv))
		self.failUnlessEqual('No existe el archivo invalido',self.validador.mensajes[0])

	def tearDown(self):
		if os.path.exists('prueba.php'):
			os.remove('prueba.php')

if __name__ == "__main__":
	unittest.main()
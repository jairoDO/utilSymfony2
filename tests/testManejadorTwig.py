import unittest
import os
import sys

sys.path.append('../')
from Parseador import Parseador, ProcesadorTipo, ProcesadorGenerico
from Atributo import Atributo
from Generador import 
from Validador import ValidadorEntradaArchivo

class TddManejadorTwig(unittest.TestCase):

	def setUp(self):
		self.validador = ValidadorEntradaArchivo()
		self.parseador = Parseador()
		self.generador =  Generador()

	def test_setear_orden(self):
		self.manejador.agregarAtributo(atributo)
		self.manejador.setOrden(atributo,2)

	def testGenerarTodo(self):
		result = """

		"""
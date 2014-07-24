import unittest
import os
import sys

sys.path.append('..')
from Parseador import Parseador, ProcesadorTipo
from Atributo import Atributo


class TestInterfaz(unittest.TestCase):
	def setUp(self):
		self.interfaz = Interfaz()
		self.parseador =  Parseador()

	def test_interfaz_print_mensaje(self):
		mensaje = """
		1) Mostrar los atributos parseados
		2) Definir Grupos de campos
		3) Definir Orden
		4) Elegir version de bootstrap
		5) Generar
		6) Generar y salir
		7) salir
		"""

	def test_mostrar_atributos(self):
		pass
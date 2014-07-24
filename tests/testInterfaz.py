import unittest
import os
import sys

sys.path.append('..')
from Menu import Menu
from Opcion import Opcion
from Parseador import Parseador, ProcesadorTipo
from Atributo import Atributo


class TestInterfaz(unittest.TestCase):

	def setUp(self):
		self.interfaz = Interfaz()

	def test_argumento_valido(self):
		argv = ['archivoInvalido']

class  TddMenu(unittest.TestCase):

	def setUp(self):
		self.menu = Menu()

	def test_menu_empty(self):
		menu = Menu()
		self.assertTrue(len(menu.getOpciones()) == 1)

	def test_menu_invalida(self):
		self.menu.ejecutar('opcionInvalida')
		self.failUnlessEqual(self.menu.mensaje.pop(), 'Opcion Invalida')


	def test_menu_quit(self):
		self.menu.ejecutar('q')
		self.assertTrue(not self.menu.debeCorrer)

if __name__ == "__main__":
	unittest.main()
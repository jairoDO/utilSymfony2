import unittest
import os
from Interfaz import Interfaz
from ValidadorTwig import ValidadorTwig

class TestInterfaz(unittest.TestCase):

	def setUp(self):
		self.interfaz = Interfaz(ValidadorTwig())

	def test_argumento_valido(self):
		argv = ['archivoInvalido']

import unittest
import os
import sys

sys.path.append('../')
from Parseador import Parseador, ProcesadorTipo, ProcesadorGenerico
from Atributo import Atributo
from ManejadorTwig import ManejadorTwig
from Validador import ValidadorEntradaArchivo

class TddManejadorTwig(unittest.TestCase):

	def setUp(self):
		self.manejador = ManejadorTwig()

##*********************  test validar positivos ******************************************
	def test_validar_normal(self):
		inputConsola = "1,2,4,5"
		self.manejador.atributos = [Atributo('nombre' + str(i)) for i in range(0,7)]
		self.failUnlessEqual(True, self.manejador.validarEntradaAtributo(inputConsola))

	def test_validar_simple_rango(self):
		inputConsola = "1..4"
		self.manejador.atributos = [Atributo('nombre' + str(i)) for i in range(0,7)]
		self.failUnlessEqual(True, self.manejador.validarEntradaAtributo(inputConsola))

	def test_validar_compuesto(self):
		inputConsola = "1,2..4,5"
		self.manejador.atributos = [Atributo('nombre' + str(i)) for i in range(0,7)]
		self.failUnlessEqual(True,self.manejador.validarEntradaAtributo(inputConsola))

#************************* test validar negativos *****************************************
	def test_validar_malInput_simple(self):
		inputConsola = "malInput"
		self.manejador.atributos = [Atributo('nombre' + str(i)) for i in range(0,7)]
		self.failUnlessEqual(False, self.manejador.validarEntradaAtributo(inputConsola))

	def test_validar_malInput_compuesto(self):
		inputConsola = "1,2,3,malInput,3"
		self.manejador.atributos = [Atributo('nombre' + str(i)) for i in range(0,7)]
		self.failUnlessEqual(False, self.manejador.validarEntradaAtributo(inputConsola))


	def test_validar_malInput_compuesto_en_rango(self):
		inputConsola = "1,2,3,1..r,3"
		self.manejador.atributos = [Atributo('nombre' + str(i)) for i in range(0,7)]
		self.failUnlessEqual(False, self.manejador.validarEntradaAtributo(inputConsola))


	def test_validar_normal_rango_grande(self):
		inputConsola = "1,2,34,5"
		self.manejador.atributos = [Atributo('nombre' + str(i)) for i in range(0,7)]
		self.failUnlessEqual(False, self.manejador.validarEntradaAtributo(inputConsola))

	def test_validar_simple_rango_falla(self):
		inputConsola = "1..4"
		self.manejador.atributos = [Atributo('nombre' + str(i)) for i in range(0,1)]
		self.failUnlessEqual(False, self.manejador.validarEntradaAtributo(inputConsola))

	def test_validar_compuesto_falla(self):
		inputConsola = "1,2..4,5"
		self.manejador.atributos = [Atributo('nombre' + str(i)) for i in range(0,4)]
		self.failUnlessEqual(False, self.manejador.validarEntradaAtributo(inputConsola))

#********************************* test parseo ***********************************************
	def test_parsear_input_normal(self):
		inputConsola = "1,2,34,5"
		self.failUnlessEqual(['1','2','34', '5'], self.manejador.parsearValorInput(inputConsola))

	def test_parsear_simple_rango(self):
		inputConsola = "1..4"
		self.failUnlessEqual([1, 2, 3, 4], self.manejador.parsearValorInput(inputConsola))

	def test_parsear_compuesto(self):
		inputConsola = "1, 2..5, 7"
		self.failUnlessEqual(['1', 2, 3, 4,5, '7'], self.manejador.parsearValorInput(inputConsola))

if __name__ == "__main__":
	unittest.main()
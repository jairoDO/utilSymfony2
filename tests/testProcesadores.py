import unittest
import os
import sys

sys.path.append('../')
from Parseador import Parseador, ProcesadorTipo, ProcesadorGenerico, ProcesadorImage
from Validador import *
from Atributo import Atributo

class TddProcesadores(unittest.TestCase):

	def test_procesador_tipo_image_multiple_linea(self):
		anotacion = """/**
    * @Assert\\Image()
    */"""
		procesador = ProcesadorImage()
		self.assertTrue(procesador.machea(anotacion))
		self.failUnlessEqual('image', procesador.devolverProcesado())

	def test_procesador_tipo_image_una_linea(self):
		anotacion = """ @Assert\\Image """
		procesador = ProcesadorImage()
		self.assertTrue(procesador.machea(anotacion))
		self.failUnlessEqual('image', procesador.devolverProcesado())		


	def test_procesar_tipo_string(self):
		anotacion = """
    /**
     * @var string $nombreCorto
     *
     * @ORM\Column(name="nombreCorto", type="string", length=90, nullable=true)
     *
     * @Assert\NotBlank(groups={"configuracion"})
     */"""
		procesador = ProcesadorTipo()
		self.assertTrue(procesador.machea(anotacion))
		self.failUnlessEqual('string', procesador.devolverProcesado())

if __name__ == "__main__":
	unittest.main()
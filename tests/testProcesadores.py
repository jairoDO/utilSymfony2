import unittest
import os
import sys

sys.path.append('../')
from Parseador import Parseador, ProcesadorTipo, ProcesadorGenerico, ProcesadorImage, ProcesadorNotBlank, ProcesadorUnoAMucho, ProcesadorEntityTarget, ProcesadorMappedBy, ProcesadorCascade
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


	def test_procesar_NotBlank_una_linea_no_required(self):
		anotacion = """
    /**
     * @var string $nombreCorto
     *
     * @ORM\Column(name="nombreCorto", type="string", length=90, nullable=true)
     *
     */"""

		procesador = ProcesadorNotBlank()
		self.assertTrue(not procesador.machea(anotacion))
		self.failUnlessEqual( False, procesador.devolverProcesado())

	def test_procesar_NotBlank_una_linea(self):
		anotacion = """@Assert\NotBlank(groups={"configuracion"})"""
		procesador = ProcesadorNotBlank()
		self.assertTrue(procesador.machea(anotacion))
		self.failUnlessEqual( True, procesador.devolverProcesado())

	def test_procesar_NotBlank_multilinea(self):
		anotacion = """
    /**
     * @var string $nombreCorto
     *
     * @ORM\Column(name="nombreCorto", type="string", length=90, nullable=true)
     *
     * @Assert\NotBlank(groups={"configuracion"})
     */"""
		procesador = ProcesadorNotBlank()
		self.assertTrue(procesador.machea(anotacion))
		self.failUnlessEqual( True, procesador.devolverProcesado())

	def test_procesar_unoAMucho(self):
		anotacion = """
   /**
     * @var ArrayCollection
     *
     * @ORM\OneToMany(
     *      targetEntity="Gse\MesaAyudaBundle\Entity\Departamento\Miembro",
     *      mappedBy="departamento",
     *      cascade={"persist", "remove"}
     *  )
     */
		"""
		procesador = ProcesadorUnoAMucho()
		self.assertTrue(procesador.machea(anotacion))
		expected = {'targetEntity': 'Gse\MesaAyudaBundle\Entity\Departamento\Miembro', 'mappedBy': 'departamento'}
		import pdb; pdb.set_trace()
		l = procesador.devolverProcesado()
		print str(l)
		self.failUnlessEqual(expected, procesador.devolverProcesado())

	def test_procesaar_targetEntity(self):
		anotacion = """
					(
     *      targetEntity="Gse\MesaAyudaBundle\Entity\Departamento\Miembro",
     *      mappedBy="departamento",
     *      cascade={"persist", "remove"}
     *  )
		"""
		procesador = ProcesadorEntityTarget()

		self.assertTrue(procesador.machea(anotacion))
		self.failUnlessEqual("Gse\MesaAyudaBundle\Entity\Departamento\Miembro", procesador.devolverProcesado())

	def test_procesar_mappedBy(self):
		anotacion = """
					(
     *      targetEntity="Gse\MesaAyudaBundle\Entity\Departamento\Miembro",
     *      mappedBy="departamento",
     *      cascade={"persist", "remove"}
     *  )
		"""
		procesador = ProcesadorMappedBy()

		self.assertTrue(procesador.machea(anotacion))
		self.failUnlessEqual("departamento", procesador.devolverProcesado())		

	def test_procesar_cascade(self):
		anotacion = """
					(
     *      targetEntity="Gse\MesaAyudaBundle\Entity\Departamento\Miembro",
     *      mappedBy="departamento",
     *      cascade={"persist", "remove"}
     *  )
		"""
		procesador = ProcesadorCascade()

		self.assertTrue(procesador.machea(anotacion))
		self.failUnlessEqual(["persist", "remove"], procesador.devolverProcesado())		

if __name__ == "__main__":
	unittest.main()
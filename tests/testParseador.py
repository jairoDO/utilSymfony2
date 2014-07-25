import unittest
import os
import sys

sys.path.append('../')
from Parseador import Parseador, ProcesadorTipo, ProcesadorGenerico
from Validador import *
from Atributo import Atributo

class TddParseador(unittest.TestCase):

	def setUp(self):
		self.parseador = Parseador()

	def test_agregar_procesador_valido(self):
		cantidadProcesadores = len(self.parseador.procesadores)
		self.parseador.agregarProcesador(ProcesadorGenerico('','generica'))
		self.assertTrue(len(self.parseador.procesadores) == cantidadProcesadores + 1)
		self.parseador.procesadores.pop()

	def test_agregar_procesador_invalido(self):
		cantidadProcesadores = len(self.parseador.procesadores)

		self.parseador.agregarProcesador(Atributo('sinImportancia')) # le paso cualquier clase	
		self.assertTrue(len(self.parseador.procesadores) == cantidadProcesadores)


	def test_parsear_archivo_invalido(self):
		nameFile = "invalido"
		self.parseador.setFileExsist(nameFile)

		self.assertTrue(self.parseador.getFile() is None)

	def test_parsear_archivo_valido(self):
		Files = open('prueba.php','w+b')
		Files.write('hola Mundo')
		self.parseador.setFile(Files)
		self.assertTrue(isinstance(self.parseador.getFile(),file))

	def test_parsear_un_atributo(self):
		string = "\tprivate $argumento1;"
		self.failUnlessEqual(self.parseador.parsearAtributos(string), ['argumento1'])

	def test_parsear_dos_atributo(self):
		string = "\tprivate $argumento1;\n"
		string += "\tprivate $argumento2;\n"

		self.failUnlessEqual( self.parseador.parsearAtributos(string), ['argumento%i' %(x) for x in range(1,3)])

	def test_parsear_varios_atributos(self):
		listaAtributos = ['\tprivate  $argumento%i;' % (x) for x in range(0,5)]
		string = '\n'.join(listaAtributos)

		self.failUnlessEqual( self.parseador.parsearAtributos('\n' + string ), ['argumento%i' % x for x in range(0,5)])
	
	def test_parsear_un_atributo_con_anotaciones_varias_lineas(self):
		string = "/**\ntexto con \n* \n asdfsafsad sdfsd anotaciones **/\n\tpublic $argument;"
		self.failUnlessEqual(['texto con \n* \n asdfsafsad sdfsd anotaciones '], self.parseador.parsearAtributosAnotaciones(string))


#	def test_parsear_varios_atributos_con_anotaciones_varias_lineas(self):
#		string = "/**\ntexto con \n* \n asdfsafsad sdfsd anotaciones **/\n\tpublic $argument;\n\t/**\ntexto con \n* \n asdfsafsad sdfsd anotaciones **/\n\tpublic $argument2;"
#		self.failUnlessEqual(['texto con \n* \n asdfsafsad sdfsd anotaciones ','texto con \n* \n asdfsafsad sdfsd anotaciones '], self.parseador.parsearAtributosAnotaciones(string))
	
	def test_crear_dict_anotacion_una_limpia(self):
		string = "/**\ntexto con \n* \n asdfsafsad sdfsd anotaciones **/\n\tpublic $argument;\n"
		self.failUnlessEqual({'argument':'/**\ntexto con \n* \n asdfsafsad sdfsd anotaciones **/'}, self.parseador.crearDictAnotaciones(string))

	def test_crear_dict_anotacion_una_sucia(self):
		string = "meto suciedad/**\ntexto con \n* \n asdfsafsad sdfsd anotaciones **/\n\tpublic $argument;\nmeto suciedad"
		self.failUnlessEqual({'argument':'/**\ntexto con \n* \n asdfsafsad sdfsd anotaciones **/'}, self.parseador.crearDictAnotaciones(string))
	
	def test_crear_dict_anotacion_una_no_es_atributo(self):
		string = "/**\ntexto con \n* \n asdfsafsad sdfsd anotaciones **/\n\tpublic $argument;\n\t/**blas,dlf sdf\n\nsdfdsfasdf**/\n\t funciotn asdsdf($parma1) \n"
		self.failUnlessEqual({'argument':'/**\ntexto con \n* \n asdfsafsad sdfsd anotaciones **/'}, self.parseador.crearDictAnotaciones(string))


	def test_crear_dict_anotacion_varias_anotaciones(self):
		string = "/**\ntexto con \n* \n asdfsafsad sdfsd anotaciones **/\n\tpublic $argument;\n\t/**\ntexto con \n* \n asdfsafsad sdfsd anotaciones **/\n\tpublic $argument2;"
		self.failUnlessEqual({'argument2':'/**\ntexto con \n* \n asdfsafsad sdfsd anotaciones **/', 'argument':'/**\ntexto con \n* \n asdfsafsad sdfsd anotaciones **/'}, self.parseador.crearDictAnotaciones(string))

	def test_crear_dict_anotacion_varias_anotaciones_limpias_sucias(self):
		string = """"
		namespace Gse\Campus2Bundle\Entity\Aval;

		use Doctrine\ORM\Mapping as ORM;
		use Symfony\Component\Validator\Constraints as Assert;
		use Symfony\Bridge\Doctrine\Validator\Constraints\UniqueEntity;

		/**
		 * TipoCapacitacion
		 *
		 * @ORM\Table("campus__aval_tipo_capacitacion", uniqueConstraints={
		 *   @ORM\UniqueConstraint(name="aval_tipoCapacitacion_unique", columns={"aval_id", "tipoCapacitacion_id"})
		 * })
		 * @ORM\Entity
		 *
		 * @UniqueEntity(fields={"aval", "tipoCapacitacion"}, errorPath="aval")
		 */
		class TipoCapacitacion
		{
		    /**
		     * @var integer
		     *
		     * @ORM\Column(name="id", type="integer")
		     * @ORM\Id
		     * @ORM\GeneratedValue(strategy="AUTO")
		     */
		    private $id;

		    /**
		     * @var \Gse\Campus2Bundle\Entity\Aval
		     *
		     * @ORM\ManyToOne(targetEntity="\Gse\Campus2Bundle\Entity\Aval", inversedBy="tipoCapacitaciones")
		     */
		    private $aval;
		"""

		self.failUnlessEqual(['aval','id'], self.parseador.crearDictAnotaciones(string).keys())

	def test_getNameSpace_correcto_una_linea(self):
		self.failUnlessEqual('gse\appBundle\Entity\certificad', self.parseador.getNameSpace("namespace gse\appBundle\Entity\certificad;"))

	def test_getNameSpace_correcto_multiple_linea(self):
		string = """
		<?php

		namespace Gse\Campus2Bundle\Entity\Certificado;

		use Doctrine\ORM\Mapping as ORM;
		use Symfony\Component\Validator\Constraints as Assert;
		"""
		self.failUnlessEqual('Gse\Campus2Bundle\Entity\Certificado', self.parseador.getNameSpace(string))

	def test_getDirectorio_bien(self):
		string = "Gse\AppBundle\Entity\Certificado"
		self.failUnlessEqual('Certificado',self.parseador.getDirectorio(string))


	def test_getDirectorio_base(self):
		string = "Gse\AppBundle\Entity"
		self.failUnlessEqual('',self.parseador.getDirectorio(string))

	def test_capitalizar_con_espacio_una_palabra(self):
		string = "alto"
		self.failUnlessEqual('Alto',self.parseador.capitalizarConEspacios(string))

	def test_capitalizar_con_espacio_dos_palabra(self):
		string = "AltoBaile"
		self.failUnlessEqual('Alto Baile',self.parseador.capitalizarConEspacios(string))


	def tearDown(self):
		if os.path.exists('prueba.php'):
			os.remove('prueba.php')


if __name__ == "__main__":
	unittest.main()
import unittest
import os
from Parseador import Parseador, ProcesadorTipo
from Atributo import Atributo

class TddGenerarHtmlForm(unittest.TestCase):

	def setUp(self):
		self.parseador = Parseador()

	def test_parsear_archivo_invalido(self):
		nameFile = "invalido"
		self.parseador.setFileExsist(nameFile)

		self.assertTrue(self.parseador.getFile() is None)

	def test_parsear_archivo_valido(self):
		File = open('prueba.php','wr')
		self.parseador.setFile(File)
		self.assertTrue(type(self.parseador.getFile()) is file)

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

############################################ Test para los procesadores ###############################################################
	def test_procesador_tipo_bien(self):
		anotacion = '/**\n\tcolumn(type="integer")**/'
		procesador = ProcesadorTipo()
		self.failUnlessEqual("integer", procesador.procesar(anotacion))

	def test_procesador_tipo_sin_matchear(self):
		anotacion = '/**\n\tcolumn()**/'
		procesador = ProcesadorTipo()
		self.failUnlessEqual(False , procesador.procesar(anotacion))

	def test_procesador_tipo_con_basura(self):
		anotacion = """ /**
					     * @var string
					     *
					     * @ORM\Column(name="presentacion", type="text", nullable=true)
					     * @Assert\NotBlank(groups={"generales", "generales_noForm", "edicion_completa"})
					     */
					     """
		procesador = ProcesadorTipo()
		self.failUnlessEqual("text" , procesador.procesar(anotacion))

	def test_procesar_atributo_con_tipo(self):
		atributo = Atributo('argument1','/**\n\tcolumn(type="integer")**/')
		self.parseador.procesarAtributo(atributo)

		self.failUnlessEqual('integer', atributo.propiedades['tipo'])

	def tearDown(self):
		if os.path.exists('prueba.php'):
			os.remove('prueba.php')


if __name__ == "__main__":
	unittest.main()
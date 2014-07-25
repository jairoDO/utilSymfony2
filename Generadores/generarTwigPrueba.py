import sys
sys.path.append('..')
from GeneradorUtil import Parseador
from ManejadorTwig import ManejadorTwig
from Menu import Menu
from Validador import ValidadorEntradaArchivo

def main():
	validador = ValidadorEntradaArchivo()

	if validador.validar(sys.argv[1:]):
		menu = Menu()
		parseador = Parseador(validador.opcionesParseadas['file'])
		manejador = ManejadorTwig()
		manejador.atributos = parseador.getAtributosProcesados()
		menu.agregarOpcion('1','agregar Atributos')
		menu.correr()
	for atributo in listaAtributos:
		print atributo
	for atributo in listaAtributos:
		print atributo.nombre

if __name__ == "__main__":
	main()
import sys
sys.path.append('..')
from GeneradorUtil import Parseador
from Menu import Menu
from Validador import ValidadorEntradaArchivo

def main():
	menu = Menu()
	parseador = Parseador(sys.argv[1:])
	listaAtributos = parseador.getAtributosProcesados()
	import pdb; pdb.set_trace()
	for atributo in listaAtributos:
		print atributo
	for atributo in listaAtributos:
		print atributo.nombre

if __name__ == "__main__":
	main()
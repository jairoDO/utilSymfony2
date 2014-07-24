import sys
from GeneradorUtil import Parseador

def main():
	parseador = Parseador(sys.argv[1])
	listaAtributos = parseador.getAtributosProcesados()
	import pdb; pdb.set_trace()
	for atributo in listaAtributos:
		print atributo
	for atributo in listaAtributos:
		print atributo.nombre

if __name__ == "__main__":
	main()
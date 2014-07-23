import sys
from GeneradorUtil import Parseador

def main():
	parseador = Parseador(sys.argv[1])
	listaAtributos = parseador.getAtributosProcesados()
	namespace = parseador.getNameSpace(parseador.fileString)
	directorio = parseador.getDirectorio(namespace)
	#import pdb;pdb.set_trace()
	for i , item in enumerate(directorio.split('\\')):
		print ('\t'*i) + item + ':\n'

	tabulador = '\t'* (len(directorio.split('\\')))
	for atributo in listaAtributos:
		if not atributo.nombre in ('id','createdBy','updatedBy','created','updated'):
			print tabulador + atributo.nombre + ': ' + parseador.capitalizarConEspacios(atributo.nombre)

if __name__ == "__main__":
	main()
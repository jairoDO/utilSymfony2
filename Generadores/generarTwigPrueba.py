#!/usr/bin/env python
import sys
sys.path.append('..')
from Parseador import Parseador
from ManejadorTwig import ManejadorTwig
from Menu import Menu
from Validador import ValidadorEntradaArchivo
from Opcion import Opcion

def main():
	validador = ValidadorEntradaArchivo()

	if validador.validar(sys.argv[1:]):
		manejador = ManejadorTwig()
		menu = Menu(manejador)

		parseador = Parseador(validador.getOpcion('file'))
		menu.agregarOpcion('a',"self.objeto.agregarAtibutosAPropocesar()",'agrega Atributos a procesar')
		menu.agregarOpcion('ag',"self.objeto.configurarGrupo()", 'guia para crear un grupo de elementos twig')
		menu.agregarOpcion('g','self.objeto.generarTwig()','Genera el twig')
		menu.agregarOpcion('ma','self.objeto.mostrarAtributos()','Muesta los atributos Parseados')
		menu.agregarOpcion('mp','self.objeto.mostrarAGenerar()','Muestra la Cola con los Atributos a Generar')
		menu.agregarOpcion('t','self.objeto.generarTodo()','Genera generarTodo')
		manejador.atributos = parseador.getAtributosProcesados()
		
		menu.correr()
	else:
		print validador.mensajes.pop()

if __name__ == "__main__":
	main()
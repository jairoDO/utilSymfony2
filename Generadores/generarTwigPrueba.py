#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys
sys.path.append('..')
import os
from Parseador import Parseador
from ManejadorTwig import ManejadorTwig
from Menu import Menu
from Validador import ValidadorEntradaArchivo
from Opcion import Opcion


def main():
	validador = ValidadorEntradaArchivo()
	os.system('clear')
	if validador.validar(sys.argv[1:]):
		manejador = ManejadorTwig()
		menu = Menu(manejador)

		parseador = Parseador(validador.getOpcion('file'))
		menu.agregarOpcion('a',"self.objeto.agregarAtibutosAPropocesar()",'agrega Atributos a procesar')
		menu.agregarOpcion('ag',"self.objeto.configurarGrupo()", 'guia para crear un grupo de elementos twig')
		menu.agregarOpcion('g','self.objeto.generarTwig()','Genera el twig')
		menu.agregarOpcion('ma','self.objeto.mostrarAtributos()','Muesta los atributos Parseados')
		menu.agregarOpcion('mp','self.objeto.mostrarAGenerar()','Muestra la Cola con los Atributos a Generar')
		menu.agregarOpcion('t','self.objeto.generarTodo()','Genera twig para todo los atributos')
		menu.agregarOpcion('cb','self.objeto.cambiarBootstrap()', 'Cambía la versíon de bootstrap con cual se van a generar twig')
		menu.agregarOpcion('dp','self.objeto.definirPath()', 'Define el path base del traductor')
		manejador.atributos = parseador.getAtributosProcesados()
		menu.correr()
	else:
		print validador.mensajes.pop()

if __name__ == "__main__":
	main()
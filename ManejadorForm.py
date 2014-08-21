# -*- encoding: utf-8 -*-
from GeneradorForm import *
import Interfaz
import os
import re

class ManejadorForm():
	def __init__(self):
		self.atributos = dict()
		self.atributosAProcesar = []
		self.generadores = dict()
		self.generadores['boolean'] = GeneradorBooleano()
		self.generadores['decimal'] = GeneradorDecimal()
		self.generadores['text'] = GeneradorText()
		self.generadores['string'] = GeneradorString()
		self.generadores['datetime'] = GeneradorDate()
		self.generadores['default'] = GeneradorGenerico()
		self.generadores['image'] = GeneradorImage()
		self.path = None
		self.namespace = None
		self.clase = None
		self.mensajes = []
		self.versionBootstap = 2
		self.plantilla = """<?php

namespace %s;

use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\Form\FormEvent;
use Symfony\Component\Form\FormEvents;
use Symfony\Component\OptionsResolver\OptionsResolverInterface;
use Symfony\Component\Form\FormInterface;

class %sType extends AbstractType
{
	public function buildForm(FormBuilderInterface $builder, array $options)
	{
		$builder%s;
	}

	public function setDefaultOptions(OptionsResolverInterface $resolver)
	{
		$resolver->setDefaults(array(
			'data_class' => '%s',
		));
	}

	public function getName()
	{
		return '%s';
	}
}
"""
	def getGenerador(self,key):
		if key in self.generadores.keys():
			generador = self.generadores[key]
		else:
			generador =  self.generadores['default']

		return generador

	def crearNombre(self):
		inicial, entity, resto = self.namespace.partition('Entity')
		empresa , bundle, resto2 = inicial.split('\\')
		subcarpetas = []
		for carpeta in resto.split('\\'):
			if carpeta != '':
				subcarpetas.append(carpeta.lower())
		return '_'.join([empresa.lower(), bundle.split('Bundle')[0].lower()] + subcarpetas + [self.clase.lower()])

	def crearNameSpace(self):
		if self.namespace == '':
			return ''
		inicial, entity, resto = self.namespace.partition('Entity')
		return inicial + 'Form' + resto

	def generar(self):
		if self.atributosAProcesar == []:
			return ''
		else:
			adds = ''
			for atributo in self.atributosAProcesar:
				generador = self.getGenerador(atributo.get('tipo'))
				adds += generador.generarForm(atributo)

			return self.plantilla % (self.crearNameSpace(), self.clase, adds, self.namespace + '\\' + self.clase, self.crearNombre())
 #!/usr/bin/python  
 # -*- coding: utf-8 -*-   
 """  
      Script que parsea los argumentos y opciones de línea de comandos  
      permitiendo usar listas para guardar argumentos con múltiples opciones  
 """  
 import sys, re, os, copy  
 from types import *  
 # Imprimir en pantalla el script y sus argumentos y opciones  
 print 'ARGV:', " ".join(sys.argv[0:]),"\n"  
 # Información de ayuda de uso del script  
 def help() :  
      """Ayuda sobre opciones del script en línea de comandos"""  
      print "usage:",sys.argv[0], "[options]\n"  
      print " -h this message\n"  
      print " -i input file/s\n"  
      print " -o output file\n"  
      exit()  
 # Definir el tipo de las variables que guardarán las opciones  
 INP_input = []  
 INP_output = ''  
 # Asignar a cada argumento una de las anteriores variables  
 options = {'h': 'help', 'help': 'help', 'i': 'INP_input', 'input': 'INP_input', 'o': 'INP_output', 'output': 'INP_output'}  
 argv_var = str()  
 # Leer los argumentos y opciones  
 for _argv in sys.argv[1:] :  
      # Leer los argumentos que comienzan con guión  
      if re.match("^-", _argv) :  
           for _opt,_var in options.iteritems() :  
                if re.compile("^-%s$" % (_opt)).match(_argv) :  
                     argv_var = copy.deepcopy(_var)  
                     if type(vars()[argv_var]) is FunctionType :  
                          vars()[argv_var]()  
                     break  
      # Anotar las opciones de cada argumento  
      else :  
           if argv_var is not None :  
                if type(vars()[argv_var]) is ListType :  
                     vars()[argv_var].append(_argv)  
                else:  
                     vars()[argv_var] += _argv  
 # Imprimir en pantalla todo lo anotado  
 print "Script:",sys.argv[0],"\n"  
 print "Argumentos y opciones:\n",  
 for _opt,_var in options.iteritems() :  
      if vars()[_var] is not None and type(vars()[_var]) is not FunctionType:  
           #print _opt,pprint(type(vars()[_var]))  
           if type(vars()[_var]) is ListType:  
                print " -"+_opt+": "+str(", ".join(vars()[_var]))  
           else :  
                print " -"+_opt+": "+str(vars()[_var])  
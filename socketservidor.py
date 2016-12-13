# -*- coding: utf-8 -*-
import socket
import sys 
import os
from thread import *
import shlex, subprocess
from subprocess import Popen
HOST = '' #ESCUCHA POR TODAS LAS INTERFACES
PORT = 8886#USAMOS UN PUERTO DE NUMERACION ALTA PARA NO INTERFERIR

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'socket creado'

try:
	s.bind((HOST, PORT))
except socket.error, msg:
	print "Error al crear socket. error code :" + str(msg[0]) + ', Error mensaje :' + msg[1] 
	sys.exit()
print 'enlace via socket activo'

s.listen(5)#encolara un maximo de 5 conexioness

def hilo_cliente(conn):
	conn.send('bienvenido al server\n')
	while True:
		data=conn.recv(1024)
		respuesta = '\nIngrese un datos de las listas'
		if not data:
			break
	    #10 funciones reservadas
		if data == ('version').lower() or data == ('version').upper():
			version = sys.version
			print 'recibe' + data
			conn.sendall(version)
		if data == ('arquitectura').lower() or data == ('arquitectura').upper():
			comando = 'arch'
			r = subprocess.check_output(comando)
			print 'recibe :' + data
			conn.sendall(r)
		if data == ('cpu').lower() or data==('cpu').upper():
			cpu=['cat', '/proc/cpuinfo']
			r = subprocess.check_output(cpu)
			print 'recibe :' + data
			conn.sendall(r)
		if data == ('memoria').lower() or data==('memoria').upper():
			memoria = ['free','-g']
			r = subprocess.check_output(memoria)
			print 'recibe :' + data
			conn.sendall(r)
		if data == ('ficheros y directorios').lower() or data == ('ficheros y directorios').upper():
			comando = 'ls'
			r = subprocess.check_output(comando)
			print 'recibe :' + data
			conn.sendall(r)	
		if data == ('registro de archivos').lower() or data == ('registro de archivos').upper():
			comando = ['ls', '-l']
			r = subprocess.check_output(comando)
			print 'recibe :' + data
			conn.sendall(r)	
		if data == ('dispositivos usb').lower() or data == ('dispositivos usb').upper():
			comando = ['lsusb','-tv']
			r = subprocess.check_output(comando)
			print 'recibe :' + data
			conn.sendall(r)	
		if data == ('unidades y ficheros montados').lower() or data == ('unidades y ficheros montados').upper():
			comando = ['cat','/proc/mounts']
			r = subprocess.check_output(comando)
			print 'recibe :' + data
			conn.sendall(r)	
		if data == ('fecha y hora').lower() or data == ('fecha y hora').upper():
			comando = 'date'
			r = subprocess.check_output(comando)
			print 'recibe :' + data
			conn.sendall(r)	
		if data == ('dispositivos pci').lower() or data == ('dispositivos pci').upper():
			comando = ['lspci','-tv']
			r = subprocess.check_output(comando)
			print 'recibe :' + data
			conn.sendall(r)	
				
		#Frases humanas
		if data == ('chilate').lower() or data == ('chilate').upper():
			chilate = "Bebida creada por los salvadoreños la cual contiene extracto de maíz, el cual se le mezcla agua y se convierte en una especie de atol; el cual se acompaña de un dulce de atado o batido de dulce."
			conn.sendall(chilate)
		if data == ('python').lower() or data == ('python').upper():
			python = "Es un lenguaje de programación interpretado cuya filosofía hace hincapié en una sintaxis que favorezca un código legible."
			conn.sendall(python)
		if data == ('tamal').lower() or data == ('tamal').upper():
			tamal = "Plato que consiste en masa de harina de maíz rellena de carne, pollo, chile u otros ingredientes, envuelta en hojas de mazorca de maíz o plátano y cocida al vapor o al horno; según los países, varían los ingredientes y presenta distintas formas."
			conn.sendall(tamal)
		if data == ('charamusca').lower() or data == ('charamusca').upper():
			charamusca = "Dulce de azúcar en forma de tirabuzón, acaramelado y duro."
			conn.sendall(charamusca)
		if data == ('mango fruta').lower() or data == ('mango fruta').upper():
			mango = "El mango es una fruta de la Zona Intertropical de pulpa carnosa y dulce. Destaca entre sus principales características su buen sabor. Dicha pulpa puede ser o no fibrosa, siendo la variedad llamada mango de hilacha la que mayor cantidad de fibra contiene."
			conn.sendall(mango)
		if data == ('platano').lower() or data == ('platano').upper():
			platano = "Fruto del platanero, comestible, de forma alargada y algo curvada, pulpa de color blanco y piel lisa de color amarillo que se desprende con facilidad."
			conn.sendall(platano)
		if data == ('refresco').lower() or data == ('refresco').upper():
			refresco = "Bebida sin alcohol elaborada generalmente con extractos vegetales, agua y azúcar que se toma fría para quitar la sed."
			conn.sendall(refresco)
		if data == ('budin').lower() or data == ('budin').upper():
			budin = "Se denomina budín o pudín a un postre de la cocina inglesa y estadounidense que suele estar compuesto de diferentes ingredientes dependiendo de la región: migas de pan, bizcocho, arroz, sémola, etc. aglutinado con huevo y aderezado a veces con custard o frutas diversas."
			conn.sendall(budin)
		if data == ('base de datos').lower() or data == ('base de datos').upper():
			base = "Una base de datos o banco de datos es un conjunto de datos pertenecientes a un mismo contexto y almacenados sistemáticamente para su posterior uso."
			conn.sendall(base)
		if data == ('carne de pollo').lower() or data == ('carne de pollo').upper():
			pollo = "La carne de pollo, es muy frecuente encontrarla en muchos platos y preparaciones de la culinaria de todo el mundo. Su carne se considera un alimento básico y es por esta razón por la que se incluye en el índice de precios al consumo."
			conn.sendall(pollo)

	#cerrar conexion
	conn.close()
while 10:
	#espera para aceptar conexion
	conn, addr = s.accept()
	print 'conectado con :' + addr[0] + ':' + str(addr[1])
	
	start_new_thread(hilo_cliente, (conn,))
	
s.close()


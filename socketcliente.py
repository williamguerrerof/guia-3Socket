# -*- coding: utf-8 -*-
import socket
import sys 
import os
from thread import *
TCP_IP = '192.168.122.1'
TCP_PORT = 8886
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while True:
	print 'Funciones reservadas','\n1. version','\n2. narquitectura','\n3. cpu','\n4. memoria','\n5. ficheros y directorios','\n6. registro de archivos','\n7. dispositivos usb','\n8. unidades y ficheros montados','\n9. fecha y hora','\n10. dispositivos pci'
	print '\nFrases','\n1. chilate','\n2. python','\n3. tamal','\n4. charamusca','\n5. mango fruta','\n6. platano','\n7. refresco','\n8. budin','\n9. base de datos','\n10. carne de pollo'
	data = s.recv(BUFFER_SIZE)
	print "el server dijo :", data
	msg = raw_input('ingrese un texto :')
	if msg != 0:
		s.send(msg)
		print "mensaje enviado :", msg
	else:
		break
		print 'hasta luego'
		s.close()

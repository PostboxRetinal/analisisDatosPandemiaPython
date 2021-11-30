#Algoritmo de manejo y consulta de datos COVID-19
# Ideado y desarrollado por Sebastián Balanta
import time
import subprocess
import csv
import os

def main():
	'''Función principal, se encarga de leer y escribir datos 
	(none) -> (none)'''
	print("Algoritmo de Búsqueda y consulta pacientes COVID-19 \n")
	time.sleep(1)
	try:
		menu()
	except KeyboardInterrupt:
		salida = input('\n*¿Desea salir del programa? S/N: * ').lower()
		if salida == 'n':
			print('\n Ok, no ha pasado nada ;) \n')
			time.sleep(2)
			menu()
		else:
			exit()
#
def menu():
	'''Menú, se encarga de llamar la función solicitada, llamada previamente por main
	(none) -> (none)'''
	flag = 0
	while flag != 1:

		print('MENÚ PRINCIPAL\n')
		print('1. Cantidad de hombres menores de edad contagiados en el pais')
		print('2. Cantidad de hombres contagiados que se han recuperado a la fecha')
		print('3. Contagiados que proceden de un pais especifico')
		print('4. Salir\n')

		opc = input('Ingrese la opc deseada: ')

		while opc.isdigit() == False:
			
			print('Ingrese sólo caractéres de tipo entero, intente nuevamente')
			opc = input('Ingrese la opc deseada: ')

		else:
			opc = int(opc)
			if opc == 1:
				h_menores()
				esperar()
				limpiar()

			elif opc == 2:
				h_contagiados()
				esperar()
				limpiar()

			elif opc == 3:
				contagiados_ext()
				esperar()
				limpiar()

			elif opc == 4:
				flag = 1
				limpiar()

			else:
				time.sleep(0.5)
				print('Opción inválida!')
				esperar()
	print('Hasta pronto')
	time.sleep(0.5)
	exit()		
#
def h_menores():
	'''Esta función se encarga de filtrar los registros que contengan hombres menores a 18 años (menores de edad) y los exporta a un archivo .txt
	(none) -> (none) 
	'''
	flag = 1
	r_menores = 'h_menores.txt'
	ruta = input('Ingrese ruta de archivo a usar: ')
	while flag == 1:
		if not os.path.exists(ruta):
			print('Ruta o nombre de archivo inválido, revise nuevamente')
			ruta = input('Ingrese ruta de archivo a usar: ')
		else:
			flag = 0

	while flag == 0:
		if not ruta:
			print('No ingresaste nada, intenta de nuevo')
			ruta = input('Ingrese ruta de archivo a usar: ')
		else:
			flag = 1

	try: 	
		with open(ruta,'r',encoding='UTF-8') as BBDD:
			lectura = csv.reader(BBDD)
			next(lectura)
			with open(r_menores,'w',encoding='UTF-8') as archivo_menores:
				for linea in lectura:
					linea_edad = int(linea[7])
					sexo = linea[9]
					if linea_edad < 18 and sexo =='M':
						nueva_linea = csv.writer(archivo_menores, delimiter='\t')
						nueva_linea.writerow(linea)
					else:
						continue
			limpiar()
			print('Salida enviada a',r_menores)
	except FileNotFoundError:
		print('¡Este archivo no existe!')
#
def h_contagiados():
	'''Esta función se encarga de filtrar los registros que contengan hombres recueperados de COVID-19 y los exporta a un archivo .txt
	(none) -> (none) 
	'''
	flag = 1
	r_recuperados = 'h_recuperados.txt'
	ruta = input('Ingrese ruta de archivo a usar: ')
	while flag == 1:
		if not os.path.exists(ruta):
			print('Ruta o nombre de archivo inválido, revise nuevamente')
			ruta = input('Ingrese ruta de archivo a usar: ')
		else:
			flag = 0

	while flag == 0:
		if not ruta:
			print('No ingresaste nada, intenta de nuevo')
			ruta = input('Ingrese ruta de archivo a usar: ')
		else:
			flag = 1
	try:
		with open(ruta,'r',encoding='UTF-8') as BBDD:
			lectura = csv.reader(BBDD)
			next(lectura)
			with open(r_recuperados,'w',encoding='UTF-8') as archivo_recuperados:
				for linea in lectura:
					estado = linea[15]
					sexo = linea[9]
					if estado == 'Recuperado' and sexo == 'M':
						nueva_linea = csv.writer(archivo_recuperados, delimiter='\t')
						nueva_linea.writerow(linea)
					else:
						continue
			limpiar()
			print('Salida enviada a',r_recuperados)
	except FileNotFoundError:
		print('¡Este archivo no existe!')
#
def contagiados_ext():
	'''Esta función se encarga de filtrar los registros que contengan casos provenientes de otro país y los exporta a un archivo "nombre_pais.txt"
	(none) -> (none)
	'''
	paises = []
	flag = 1
	num = 1
	ruta = input('Ingrese ruta de archivo a usar: ')
	while flag != 0:
		if not os.path.exists(ruta):
			print('Ruta o nombre de archivo inválido, revise nuevamente')
			ruta = input('Ingrese ruta de archivo a usar: ')
		else:
			flag = 0

	while flag != 1:
		if not ruta:
			print('No ingresaste nada, intenta nuevamente')
			ruta = input('Ingrese ruta de archivo a usar: ')
		else:
			flag = 1
		with open(ruta,'r',encoding='UTF-8') as BBDD:
			lectura = csv.reader(BBDD)
			next(lectura)
			#Filtro para listar países disponibles
			for linea in lectura:	
				if linea[14] not in paises:
					paises.append(linea[14])
				else:
					continue
			#Ciclo para listar los países del arreglo
			for pais in paises:
				if pais == "":
					continue
				else:
					print(num,pais)
					num += 1
			print()

			#Filtro de país
			input_pais = input('Digite nombre del país que desea filtrar por: ').upper()

			while flag != 0:
				if not input_pais:
					print('No ingresaste nada!, Intenta nuevamente')
					input_pais = input('Digite nombre del país que desea filtrar por: ').upper()
				elif input_pais not in paises:
					print('País no encontrado, intenta con otro nombre o escribirlo correctamente')
					input_pais = input('Digite nombre del país que desea filtrar por: ').upper()
				else:
					flag = 0

			r_contagiados_ext = input_pais.lower() + '.txt'
			r_contagiados_ext = r_contagiados_ext.strip(' ')
		with open(ruta,'r',encoding='UTF-8') as BBDD:
			lectura2 = csv.reader(BBDD)
			next(lectura2)
			with open(r_contagiados_ext,'w',encoding='UTF-8') as archivo_contagiados_ext:
				for info in lectura2:
					linea_pais = info[14]
					if input_pais == linea_pais:
						nueva_linea = csv.writer(archivo_contagiados_ext, delimiter='\t')
						nueva_linea.writerow(info)
					else:
						continue
				print('Salida exportada a: ',r_contagiados_ext)
				
#
def esperar():
	'''Esta función se encarga de esperar una interacción del usuario
	(none) -> (none)'''
	subprocess.run('pause',shell=True)
#
def limpiar():
	'''Esta función es como mi firma, se encarga de limpiar la pantalla
	(none) -> (none)'''
	subprocess.run('cls',shell=True)
#

main()
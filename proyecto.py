#Proyecto 3er corte
# Creado por Santiago Sánchez y Sebastián Balanta
import time
import subprocess
import csv

def main():
	'''Función principal, se encarga de leer y escribir datos 
	(none) -> (none)'''
	print("Algoritmo de Búsqueda y consulta pacientes COVID-19 Balamon's \n")
	time.sleep(1)
	menu()
#--------------------------------------------
def separar(lista):
	if len(lista) < 2:
		return lista

	else:
		long_mitad = len(lista) // 2
		long_der = separar(lista[:long_mitad])
		long_izq = separar(lista[long_mitad:])
		return mezclar(long_der,long_izq)
#	
def mezclar(long_derecha, long_izquierda):
	x = 0
	y = 0
	final = []

	while(x < len(long_derecha) and y < len(long_izquierda)):
		if (long_derecha[x] < long_izquierda[y]):
			final.append(long_derecha[x])
			x += 1
		else:
			final.append(long_izquierda[y])
			y += 1

	final += long_derecha[x:]
	final += long_izquierda[y:]
 
	return final
#--------------------------------------------
def menu():
	'''Función principal, se encarga de leer la opcion solicitada y llamar las funciones requeridas
	(None) -> (None)'''
	flag = 0
	while flag != 1:
		print('MENÚ PRINCIPAL\n')
		print('1. Cantidad de hombres menores de edad contagiados en el pais')
		print('2. Cantidad de hombres contagiados que se han recuperado a la fecha')
		print('3. Contagiados que proceden de un pais especifico')
		print('4. Países de donde ha llegado el virus a Colombia')
		print('5. Salir\n')

		opc = int(input('Ingrese la opc deseada: '))
		if opc == 1:
			h_menores()
			esperar()

		elif opc == 2:
			h_contagiados()
			esperar()

		elif opc == 3:
			contagiados_ext()
			esperar()

		elif opc == 4:
			virus_a_colombia()
			esperar()

		elif opc == 5:
			flag == 1

		elif not opc:
			print('No ingresaste nada!')

		else:
			print('Opción inválida!')
	print('Hasta pronto')
	time.sleep(1)
	exit()		
#
def h_menores():
	'''Esta función se encarga de filtrar los registros que contengan hombres menores a 18 años (menores de edad) y los exporta a un archivo .txt 
	(list) -> (list)'''
	ruta = input('Ingrese ruta de archivo a usar: ')
	flag = 1
	r_menores = 'h_menores.txt'
	while flag == 1:
		if not ruta:
			print('No ingresaste nada, intenta de nuevo')
			ruta = input('Ingrese ruta de archivo a usar: ')
		else:
			flag = 0
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
	print('Salida enviada a ','h_menores.txt')
#
def h_contagiados():
	print('Hombres contagiados')
	'''Esta función se encarga de filtrar los registros que contengan hombres menores a 18 años (menores de edad) y los exporta a un archivo .txt 
	(list) -> (list)'''
	ruta = input('Ingrese ruta de archivo a usar: ')
	flag = 1
	hombres_recuperados = 'h_recuperados.txt'
	while flag == 1:
		if not ruta:
			print('No ingresaste nada, intenta de nuevo')
			ruta = input('Ingrese ruta de archivo a usar: ')
		else:
			flag = 0
	with open(ruta,'r',encoding='UTF-8') as BBDD:
		lectura = csv.reader(BBDD)
		next(lectura)
		with open(hombres_recuperados,'w',encoding='UTF-8') as archivo_recuperados:
			for linea in lectura:
				estado = linea[15]
				sexo = linea[9]
				if estado == 'Recuperado' and sexo == 'M':
					nueva_linea = csv.writer(archivo_recuperados, delimiter='\t')
					nueva_linea.writerow(linea)
				else:
					continue
	print('Salida enviada a ',hombres_recuperados)
#
def contagiados_ext():
	print('Contagiados')
#
def virus_a_colombia():
	print('Países de donde proviene el virus: ')
#
def esperar():
	'''Esta función se encarga de esperar una interacción del usuario (none) -> (none)'''
	subprocess.run('pause',shell=True)

main()
def leerArchivo():

	#nombreArchivo = input("Ingrese el nombre del archivo: ")

	archivo = open("texto.txt", 'r')

	for linea in archivo:
		print(linea)

	return archivo


def escribirArchivo(listaSecuencia):

	#nombre = input("\n Ingrese el nombre del archivo a escribir (Sin extension): ")

	archivo = open("salida.txt" ,'w')

	archivo.write("*********************************************\n")

	for secuencia in listaSecuencia:
		
		archivo.write(secuencia)		
		archivo.write("\n")

	archivo.write("*********************************************\n")

def separador():

	
	
	return 

def main():

	# Leer archivo de secuencia 
	archivo = leerArchivo()

	# Separador

	separador()

	# Escribir archivo de salida
	escribirArchivo(["cv","cv"])

main()
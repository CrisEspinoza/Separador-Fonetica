def readFile():
	file = open("texto.txt", 'r')
	return file

def writeFile(letter):
	archivo = open("salida.txt" ,'a')
	archivo.write(str(letter))		

def readFileWordReservate():
	file = open("posibilidades.txt", 'r')
	listWord = []
	for word in file:
		aux = word.split()
		aux.append(len(aux[0]))
		listWord.append(aux)
	return listWord

def separate(file):
	listWord = readFileWordReservate();
	for row in file:
		rowSeparate = row.split()
		for word in rowSeparate:
			analysis(word,listWord)

def analysis(word,listWord):
	writeFile("Secuencia a evaluar es: " + word + "\n")
	count = 0 
	countLetter = 0
	maximo = 0
	lenWord = len(word)
	while count < lenWord:
		for element in listWord:
			if ((lenWord - count) >= element[1] ):
				for x in range(0,len(element[0])):
					if(element[0][x] == word[x]):
						countLetter = countLetter + 1
					else:
						countLetter = 0
						break
				if (maximo < countLetter):
					maximo = countLetter
				countLetter = 0
		writeFile(word[:maximo] + "\n")
		word = word[maximo:]
		count = maximo + count
		maximo = 0

def main():
	# Leer archivo de secuencia 
	file = readFile()
	# Separador
	separate(file)

main()
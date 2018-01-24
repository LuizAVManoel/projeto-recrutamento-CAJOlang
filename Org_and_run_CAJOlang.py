'''
Aplicação que organiza e roda programas CAJOlang
Autor: Luiz Augusto Vieira Manoel
2018.1
'''

import sys
from datetime import datetime
#				Variáveis do sistema				#
#CAJOlang tem três posições na memória para inteiros,
intCAJO = [None]*3
#duas posições na memória para file descriptors
fdCAJO = [None]*2
#e uma área temporaria que guarda um inteiro.
temp_area = 0
#####################################################

###			Bloco de intruções CAJOlang			  ### 
#Função que copia o que está na área temporaria para posição POS da memória int (intCAJO)
def CAJO_COPY_TO_MEMORY(POS):
	intCAJO[POS] = temp_area

#Copia o que está na posição POS da memória int (intCAJO) para área temporaria
def CAJO_COPY_FROM_MEMORY(POS):
	temp_area = intCAJO[POS]

#Seta o valor de number para posição POS da memória int (intCAJO)
def CAJO_SET_MEMORY(number,POS):
	intCAJO[POS] = number

#Adiciona o valor da posição POS da memória int (intCAJO) ao valor da área temporaria
def CAJO_ADD(POS):
	temp_area += intCAJO[POS]

#Subtrai o valor da posição POS da memória int (intCAJO) do valor da área temporaria
def CAJO_SUBTRACT(POS):
	temp_area -= intCAJO[POS]

#Imprime o valor que está na área temporaria
def CAJO_PRINT():
	print("temp_area = "+str(temp_area))

#Abre o arquivo de nome fileName no modo mode e armazena na posição POS da 
#	memória de file descriptors (fdCAJO). Mode --> 0 = read e 1 = write
def CAJO_OPEN(fileName, POS, mode):  #Conferir o tamanho de fileName
	if mode == 0:
		arq = open(fileName,'r')
	elif mode == 1:
		arq = open(fileName,'w')
	
	fdCAJO[POS] = arq

#Fecha o file descriptor na posição POS de fdCAJO
def CAJO_CLOSE(POS):
	fdCAJO[POS].close()

#Le um inteiro do file descriptor na posição POS de fdCAJO para área temporaria
def CAJO_READ(POS): #verificar 16BIT
	inteiro = fdCAJO[POS].read()
	temp_area = int(inteiro)

#Escreve o inteiro da área temporaria no arquivo de posição POS de fdCAJO
def CAJO_WRITE(POS): #verificar 16BIT
	fdCAJO[POS].write(str(temp_area))
#####################################################

#Função que recebe o nome do arquivo .cl como parâmetro e o executa
def executeCAJO(CAJOfileName):
	arquivoCL = open(CAJOfileName,'r') 
	
	#Todas linhas do arquivo .cl serão lidas na variável lines como lista
	#	ou seja, cada elemento da lista lines é uma linha do arquivo .cl
	lines = arquivoCL.readlines()
	
	#Variável de iteração do while. O valor dela significa a linha que será iterada
	execLine = 1 
	
	while execLine < len(lines):
		#Função split separa a linha: comando[0] é o comando principal e 
		#	as próximas posições (se houver) são os parâmetros
		comando = lines[execLine].split()
		
		#Bloco de instruções jump
		if comando[0] == "CAJO_JUMP_IF_NEGATIVE_TO":
			if temp_area < 0:
				execLine = int(comando[1])
		elif comando[0] == "CAJO_JUMP_IF_POSITIVE_TO":
			if temp_area > 0:
				execLine = int(comando[1])
		elif comando[0] == "CAJO_JUMP_IF_ZERO_TO":
			if temp_area == 0:
				execLine = int(comando[1])		
		elif comando[0] == "CAJO_JUMP":
			execLine = int(comando[1])
			
		else:
			#Bloco de instruções comuns
			if comando[0] == "CAJO_COPY_TO_MEMORY":
				CAJO_COPY_TO_MEMORY(comando[1])
			elif comando[0] == "CAJO_COPY_FROM_MEMORY":
				CAJO_COPY_FROM_MEMORY(comando[1])
			elif comando[0] == "CAJO_SET_MEMORY":
				CAJO_SET_MEMORY(comando[1],comando[2])
			elif comando[0] == "CAJO_ADD":
				CAJO_ADD(comando[1])
			elif comando[0] == "CAJO_SUBTRACT":
				CAJO_SUBTRACT(comando[1])
			elif comando[0] == "CAJO_PRINT":
				CAJO_PRINT()
			elif comando[0] == "CAJO_OPEN":
				CAJO_OPEN(comando[1],comando[2],comando[3])
			elif comando[0] == "CAJO_CLOSE":
				CAJO_CLOSE(comando[1])
			elif comando[0] == "CAJO_READ":
				CAJO_READ(comando[1])
			elif comando[0] == "CAJO_WRITE":
				CAJO_WRITE(comando[1])
		
			execLine += 1
		
	
	arquivoCL.close()

'''
A classe CAJOlang_program possui dois atributos:
	CAJOnumber: inteiro que identifica o minuto que o programa vai rodar cada hora que passa.
	fileName: nome do arquivo .cl
	
Além disso, possui o método execute. Esse método executa o programa CAJO de nome "filename"
	através da função executeCAJO quando o minuto da hora do sistema é igual ao CAJOnumber.
'''
class CAJOlang_program(object):
	
	def __init__(self,CAJOnumber,fileName):
		self.CAJOnumber = CAJOnumber;
		self.fileName = fileName

	def execute(self):
		now = datetime.now()
		if(self.CAJOnumber == now.minute):
			executeCAJO(self.fileName)
			
#Para cada linha do stdin é criado um objeto da classe CAJOlang_program			
for line in sys.stdin:
	CAJOfile = open(line,'r')
	CAJOnumber = int(CAJOfile.readline())
	CL = CAJOlang_program(CAJOnumber,line)
	CLlist.append(CL)
	CAJOfile.close()

while(1):
	for CLfile in CLlist:
		CLfile.execute()
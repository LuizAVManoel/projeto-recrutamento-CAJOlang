'''
Aplicação que organiza e roda programas CAJOlang
Autor: Luiz Augusto Vieira Manoel
2018.1
'''

from datetime import datetime
#				Variáveis do sistema				#
#CAJOlang tem três posições na memória para inteiros,
A = 0 
B = 0 
C = 0
#duas posições na memória para file descriptors
FD0 = ""
FD1 = "" 
#e uma área temporaria que guarda um inteiro.
temp_area = 0
#####################################################

#Função que recebe o nome do arquivo .cl como parâmetro e o executa
def executeCAJO(fileName):
	arquivoCL = open(fileName,'r') 
	
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
		
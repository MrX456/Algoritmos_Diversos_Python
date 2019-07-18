#Digitar nome de 4 pessoas e embaralhar ordem
from random import shuffle

pessoa1 = input('Digite o primeiro nome ')
pessoa2 = input('Digite o segundo nome ')
pessoa3 = input('Digite o terceiro nome ')
pessoa4 = input('Digite o quarto nome ')

lista = [pessoa1, pessoa2, pessoa3, pessoa4]

shuffle(lista)
print(lista)

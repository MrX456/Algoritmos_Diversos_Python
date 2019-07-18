#Ler um input e mostrar somente parte inteira do número digitado
from math import trunc

num = float(input('Digite um número decimal : '))

print('A parte inteira do número {0} é {1}'.format(num,trunc(num)))

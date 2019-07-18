#Calcular a hipotenusa de um triangulo retangulo recebendo valores dos catetos
from math import pow, sqrt

cat1 = float(input('Digite o valor do primeiro cateto : '))
cat2 = float(input('Digite o valor do segundo cateto : '))

hipQuad = pow(cat1,2) + pow(cat2,2)
hip = sqrt(hipQuad)

print('A hipotenusa do triângulo é {0:.2f}'.format(hip))

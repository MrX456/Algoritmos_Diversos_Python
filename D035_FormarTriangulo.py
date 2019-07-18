#Ler comprimeto de 3 retas e dizer se elas podem ou não formar um triângulo

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 :
    print('As retas acima podem formar um triângulo')
else :
    print('As retas acima não podem formar um triângulo')

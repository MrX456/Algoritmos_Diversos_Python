#Ler um numero e exibir tabuada

n = int(input('Digite um número para ver a tabuada: '))
c = 1

while c <= 10 :
    produto = n * c
    print('{0} x {1} = {2}'.format(n, c, produto))
    c += 1

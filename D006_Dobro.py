#Ler um numero e mostrar seu dobro, triplo e raiz quadrada

x = int(input('Digite um número : '))
dobro = x * 2
triplo = x * 3
raiz = x ** (1/2)

print(x)
print('Dobro : {0} \nTriplo : {1} \nRaiz Quadrada : {2}'.format(dobro, triplo, raiz))

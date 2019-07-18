#Ler valor e converter real para dólar(R$3,75)

real = float(input('Digite um valor em reais: '))

dolar = real / 3.75

print('R${0:.2f}'.format(real))
print('Você tem ${0:.2f} dólares'.format(dolar))

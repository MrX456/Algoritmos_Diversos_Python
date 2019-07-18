#Aluguel de carro, verificar qtde de Kms rodados e dias que foi alugado
#verificar valor a cobrar. Aluguel carro R$60 e R$0.15 por Km rodado

dia = int(input('Quantos dias carro ficou alugado? '))
kms = float(input('Quantos kms foram rodados? '))

total = (dia * 60) + (kms * 0.15)

print('o total a ser pago é R${0:.2f}'.format(total))

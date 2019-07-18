#Verificar velocidade de um carro e se for maior que 80km/h multar
#multa será de R$7,00 por km excedido

velocidade = int(input('Digite a velocidade do carro : '))

if velocidade > 80 :
    multa = float(velocidade - 80) * 7
    print('Velocidade maxima 80Km/h / velocidade do veículo {0}Km/h'.format(velocidade))
    print('Você foi multado em R${0:.2f}'.format(multa))
else :
    print('Velocidade ok')

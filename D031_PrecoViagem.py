#Dada uma distancia de uma viagem em km calcular o preço cobrando R$0,50 por
#km até 200km e 45 para viagens mais longas

distancia = float(input('Qual a distância da viagem: '))

print('Distâcia {:.1f}km'.format(distancia))

if distancia <= 200 :
    preco = distancia * 0.5
    print('A viagem vai custar R${:.2f}'.format(preco))
else :
    preco = distancia * 0.45
    print('A viagem vai custar R${:.2f}'.format(preco))

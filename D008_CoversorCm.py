#Ler valor em metros e converter para cm e mm

tamanho = float(input('Digite um valor em metros: '))
cm = tamanho * 100
mm = tamanho * 1000

print('{0} m')
print('centimetros : {0}cm \nmilimetros : {1}mm'.format(cm, mm))

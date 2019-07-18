#Calcular area de uma parede e quantidade de tinta necessaria para pinta-la
#cada litro pinta uma area de 2m^2

alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))
area = alt * lar

print('Área de parede {0:.2f}m^2'.format(area))

litros = area / 2
print('São necessarios {0:.2f}l de tinta para pintar esta parede'.format(litros))

#Ler um valor digitado (graus c) e converter a temperatura
#para fahrenheit e kelvin

temp = int(input('Digite a temperatura em celsius: '))

f = (temp * (9/5)) + 32
k = temp + 273.15

print('Celsius : {0}°c'.format(temp))
print('Fahrenheit : {0:.1f}°F'.format(f))
print('Kelvin : {0:.2f}°k'.format(k))

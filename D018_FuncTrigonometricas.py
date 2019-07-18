#Ler um angulo e exibir seno cosseno e tangente
import math

ang = float(input('Digite o valor de um ângulo em graus : '))

seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print('seno de {0}° é {1:.2f}'.format(ang, seno))
print('cosseno de {0}° é {1:.2f}'.format(ang, cosseno))
print('cosseno de {0}° é {1:.2f}'.format(ang, tang))

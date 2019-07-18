#Sortear um nome de 4 possiveis
import random

print('Maria Alessandra Paula Eliane')
sorteio = random.randint(1,4)

if sorteio == 1 :
    print('A pessoa sorteada foi Maria')
elif sorteio == 2 :
    print('A pessoa sorteada foi Alessandra')
elif sorteio == 3 :
    print('A pessoa sorteada foi Paula')
else:
    print('A pessoa sorteada foi Eliane')

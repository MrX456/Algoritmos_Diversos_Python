#Jogo da adivinhação, computador sorteia numero de 0 a 5 e usuario adivinha
import random

num = random.randint(0, 5)

print('-------------------')
print('Jogo da adivinhação')
print('-------------------')
palpite = int(input('De 0 a 5, qual numero sorteado pelo computador? \n'))

if palpite == num :
    print('Parabens você acertou!')
else :
    print('Você errou.')

print('Encerrando programa...')

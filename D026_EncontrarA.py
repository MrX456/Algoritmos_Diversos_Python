#Ler uma frase e mostrar quantas vezes aparece a letra a, qual posição aparece
#a primeira e a ultima

frase = input('Digite uma frase : ').strip()
frase = frase.lower()

print('A letra a aparece {0} vezes'.format(frase.count('a')))
print('A primeira letra a aparece na posição {0}'.format(frase.find('a') + 1))
print('A ultima letra a aparece na posição {0}'.format(frase.rfind('a') + 1))

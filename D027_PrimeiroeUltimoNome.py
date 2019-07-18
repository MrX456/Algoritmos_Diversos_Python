#Ler um nome completo e mostrar qual o primeiro e o ultimo nome

nome = input('Digite um nome completo : ').strip()
nome = nome.title()
nome = nome.split()
print('Prazer em te conhecer!')
print('O primeiro nome é {0}'.format(nome[0]))
print('O ultimo nome é {0}'.format(nome[len(nome)-1]))

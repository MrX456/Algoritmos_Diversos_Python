#Ler o nome completo de uma pessoa e mostrar em letras maiusculas
#letras minusculas, tamanho sem espaços, numero de letras do primeiro nome

nome = input('Digite seu nome completo : ')

print('Apenas maiusculas {0}'.format(nome.upper()))
print('Apenas minusculas {0}'.format(nome.lower()))
print('Quantidade de letras sem espaço {0}'.format(len(nome.replace(' ',''))))

dividir = nome.split()
print('Quantidade de letras primeiro nome {0}'.format(len(dividir[0])))

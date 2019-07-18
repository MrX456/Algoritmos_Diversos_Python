#Verificar se o nome de uma pessoa possui Silva

nome = input('Digite um nome completo : ').strip()
nome = nome.title()
print('Seu nome possui Silva? {0}'.format('Silva' in nome))


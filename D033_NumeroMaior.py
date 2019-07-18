#Ler 3 numeros e varificar quem é o maior e o menor

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite outro número: '))

menor = a
if b < a and b < c :
    menor = b
if c < a and c < b :
    menor = c;
print('O menor valor digitado foi {0}'.format(menor))

maior = a
if b > a and b > c :
    maior = b
if c > a and c > b:
    maior = c

print('O maior valor digitado foi {0}'.format(maior))




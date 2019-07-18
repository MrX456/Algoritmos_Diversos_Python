#Calcular média entre duas notas(0 a 10)

aluno = input('Digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

print('A média do aluno {0} é de {1:.1f}'.format(aluno, media))

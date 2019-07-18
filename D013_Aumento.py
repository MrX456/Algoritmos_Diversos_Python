#Ler salario de um funcionário e dar um aumento de 15%

func = input('Digite o nome do funcionario: ')
sal = float(input('Digite o salário de {0}: R$'.format(func)))

novoSal = sal + (sal * (15/100))

print('Salario inicial R${0:.2f}'.format(sal))
print('Novo salario com 15% de aumento R${0:.2f}'.format(novoSal))



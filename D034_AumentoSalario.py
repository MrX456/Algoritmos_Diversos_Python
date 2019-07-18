#Ler o salario de um funcionario e caso seja maior de 1250 ganha 10% de aumento
#se for inferior ganha 15%

sal = float(input('Digite o salario do funcionário : '))

if sal > 1250 :
    sal += sal * (10 / 100)
    print('O novo salário será de R${0:.2f}'.format(sal))
else :
    sal += sal * (15 / 100)
    print('O novo salário será de R${0:.2f}'.format(sal))

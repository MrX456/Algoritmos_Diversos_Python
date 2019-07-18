#Ler o preço de um produto e calcular automaticamente 5% de desconto

preco = float(input('Digite o valor do produto: '))

total = preco - (preco * (5 / 100))

print('Valor original R${0:.2f}'.format(preco))
print('Valor com desconto 5% R${0:.2f}'.format(total))

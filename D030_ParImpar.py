#Verificar se numero digitado pelo usuario é par ou impar

num = input('Digite um número : ')

if not(num.isnumeric()) :
    print('Digite apenas numeros')
else :
    if int(num) % 2 == 0 :
        print('O número {0} é par'.format(num))
    else :
        print('O número {0} é impar'.format(num))        

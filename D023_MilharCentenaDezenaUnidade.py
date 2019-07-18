#Ler numero até 9999 mostrar milhar, centena, unidade e dezena

num = input('Digite um numero até 9999 : ')

if not(num.isnumeric()) :
    print('Você deve digitar um número!')
else :
    if int(num) >= 0 and int(num) < 10 :
        print('Unidades {0}'.format(num[0]))
        print('Dezenas 0')
        print('Centenas 0')
        print('Milhar 0')
    elif int(num) >= 10 and int(num) < 100 :
        print('Unidades {0}'.format(num[1]))
        print('Dezenas {0}'.format(num[0]))
        print('Centenas 0')
        print('Milhar 0')
    elif int(num) >= 100 and int(num) < 1000 :
        print('Unidades {0}'.format(num[2]))
        print('Dezenas {0}'.format(num[1]))
        print('Centenas {0}'.format(num[0]))
        print('Milhar 0')
    elif int(num) >= 1000 and int(num) < 10000 :
        print('Unidades {0}'.format(num[3]))
        print('Dezenas {0}'.format(num[2]))
        print('Centenas {0}'.format(num[1]))
        print('Milhar {0}'.format(num[0]))
    else :
        print('Número fora do intervalo válido!')

#Verificar se o ano digitado é bissexto
from datetime import date

ano = int(input('Digite o ano a ser analisado.Coloque 0 para o ano atual : '))

if ano == 0 :
    ano = date.today().year
    
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print('O ano {0} é bissexto'.format(ano))
else :
     print('O ano {0} não é bissexto'.format(ano))

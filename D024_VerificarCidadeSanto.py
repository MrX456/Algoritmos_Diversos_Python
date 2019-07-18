#Ler o nome de uma cidade e verificar se começa com Santo

cidade = input('Digite o nome de uma cidade : ')
remove = cidade.replace(' ','')

if not(remove.isalpha()) :
     print('Nome invalido!')
else :
     cidade = cidade.title()
     if cidade.find('Santo') == 0 :
        print('A cidade {0} começa com Santo'.format(cidade))
     else :
        print('A cidade {0} não começa com Santo'.format(cidade))

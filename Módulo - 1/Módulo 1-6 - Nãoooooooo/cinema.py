nome = input('Qual é o seu nome ? ')
idade = int(input('Qual é a sua idade ? '))


if idade >= 18:
    print('Você tem acesso ao ingresso do clube de festas')

    print('-'*20)
    print('1 - Entrada padrão: R$ 35,00 \n2 - Entrada VIP: R$60,00')
    entrada = float(input('Escolha a sua entrada: '))
    print('-'*20)
    print()
    print('-'*20)
    estuda = input('Você é estudande de python ?(sim ou nao)\n ')
    print('-'*20)
    if estuda.lower() == 'sim':
        print('Você conseguiu um desconto de 50%')
        if entrada == 1:
            print(f'Valor: R${35 * 0.5:.2f}')
        elif entrada == 2:
            print(f'Valor: R${60 * 0.5:.2f}')
    else:
        print('Bem vinda(o), você recebeu a sua entrada')
else:
    print('Espere mais {} ano(s) para entrar no clube!'.format(18 - idade))

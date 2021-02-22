vermelho   = "\033[1;31m"  
fundo_vermelho = '\033[1;101m'
fundo_verde = '\033[1;42m'
preto = '\033[1;30m'
reset = "\033[0;0m"
negrito = '\033[;1m'



print(vermelho + '{:^60}'.format('MÉDICO GRINGO' + reset))
temperatura = float(input(negrito  + 'Qual é a sua temperatura ? \n'))

if temperatura > 37:
    print( fundo_vermelho +'Sinto muito, você está com febre, melhor tomar um antitérmico' + reset)
else:
    print( fundo_verde + preto +'Você não está com febre, volte para casa!' + reset )
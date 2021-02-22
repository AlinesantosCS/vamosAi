# Se não me engano .title() retorna a string como se fosse um título, ou seja, a primeira letra maiuscula

def sobre_marie():
    print("{0:^60}".format('Marie Curie'))
    print('Cientista responsável por descrever os elementos químicos Polônio e o Rádio e primeira mulher a ganhar um Prêmio Nobel — Física (1903) e Química (1911).')
   
def comparacao():
    idade = int(input('Qual é o seu ano de nascimento ? '))
    pais = input('Qual é o país de nascimento ? - sem acentos ')
    estado = input('Qual é o estado de nascimento ? - sem acentos ') 

    if idade > 1934:
        idade = idade - 1934
        print(f'Você é mais novo(a) que a Marie Curie diferença de {idade} anos')
    elif(idade < 1934):
        print(f'Você é mais velho(a) que a Marie Curie diferença de {idade} anos')
    
    if (pais == 'polonia'):
        print(f'Você nasceu no mesmo país que se chama {pais.capitalize()} que a Marie Curie. ')
    else:
        print(f'Você nasceu({pais.capitalize()}) em um pais diferente da Marie Curie, ela nasceu na Polônia. ')
    
    if (estado == 'varsovia'):
        print(f'Você nasceu no mesmo país que se chama {pais.capitalize()} que a Marie Curie. ')
    else:
        print(f'Você nasceu({estado.capitalize()}) em um estado diferente da Marie Curie, da qual foi Varsóvia. ')

sobre_marie() 
comparacao() 

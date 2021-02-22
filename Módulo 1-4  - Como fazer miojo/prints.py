""" Print normal """
nome = 'Aline'
sobrenome = 'Santos'
print(f'Nome inteiro: {nome} {sobrenome}')

""" Print com sep """
dia = "25"
mes = "12"
ano = "2020"
print(dia, mes, ano, sep='/')

""" Print f,{} e %s """
nome = "Carlos"
print(f"{nome}") # f-string
print("{}".format(nome)) # format
print("%s" % nome) # porcentagem

""" Utlizando sep e end """
ano1 = '1980'
ano2 = '1990'
ano3 = '2000'
ano4 = '2010'
texto = "Alterando o valor de sep"
print(texto)
print(ano1, ano2, ano3, ano4, sep='--->')
print()

texto = "Alterando o valor de sep e end"
print(texto)
print(ano1, ano2, ano3, ano4, sep='--->', end='...\n')


""" FORMATS """
texto = '{0} tem {idade} anos de idade'
print('Progama para calcular a idade de uma pessoa',end='\n\n')

nome = input('Entre com o nome da pessoa: \n')

a1 = int(input('Entre com o ano de nascimento: \n'))

a2 = int(input('Entre com ano atual: \n'))

print(texto.format(nome, idade = a2 - a1 ))

# :[preencher][alinhar][largura].[precisão]
"""
preencher -> Qualquer caracter
alinhar -> < esquerda >direita ^centro
largura -> largura miníma do campo
precisão -> largura máxima do campo

"""
# Programa para testar a função format()

s = 'Eu Adoro Python'
s = 'Eu Adoro Python'

# alinha a direita com espaços em branco
print("{0:>20}".format(s))

# alinha a direita com símbolos #
print("{0:#>20}".format(s))

# alinha ao centro usando espaços em branco a esquerda e a direita
print("{0:^20}".format(s))

# imprime só as primeiras oito letras
print("{0:.8}".format(s))

""" Quantidade decimais e espaçamento :.9 """
teste = 7.98562434234
print('O valor de teste formatado é {:.4f}'.format(teste))

yes_votes = 42_572_654
no_votes = 43_132_495

percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

""" Tabela """
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

    """ Colocar o 'eels ' do valor """
    animals = 'eels'
print(f'My hovercraft is full of {animals}.')

print(f'My hovercraft is full of {animals!r}.')

#    """ Formas de fazer o format """
# 01
print('{0} and {1}'.format('spam', 'eggs'))

print('{1} and {0}'.format('spam', 'eggs'))

# 02
print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))

# 03
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg')) 
                                                        



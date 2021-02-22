print('Você usou qual produto para higenizar as mãos antes de sair ?')
print('Alcool em gel - 1')
print('Sabão - 2')
print('Nenhum - 3')

higiene = input('Escolha um número: ')

if (higiene == '1') or (higiene == '2'):
    print('Você está pronto para sair de casa!')
else:
    print('Tristeza! Volte e lave as suas mãos!')

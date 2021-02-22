print('Digite três produtos')
produto_1 = input('Primeiro produto: ')
preco_1 = float(input('Qual o preço do produto acima? '))
print('-'*60)
produto_2 = input('Segundo produto:  ')
preco_2 = float(input('Qual o preço do produto acima? ' ))
print('-'*60)
produto_3 = input('Terceiro produto: ')
preco_3 = float(input('Qual o preço do produto acima? ' ))
print('-'*60)

if preco_2 < preco_1 and preco_2 < preco_3:
    print(f' O {produto_2} com o preço de {preco_2:.2f} reais é o mais barato')
elif preco_3 < preco_1 and preco_3 < preco_2:
    print(f' O {produto_3} com o preço de {preco_3:.2f} reais é o mais barato')
else:
    print(f' O {produto_1} com o preço de {preco_1:.2f} reais é o mais barato')


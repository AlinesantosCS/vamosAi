tomate_um_ano_atras = float(input('Qual foi o preço KG do tomate 1 ano atrás ? \n'))
tomate_hoje = float(input('Qual o preço do KG do tomate hoje ? \n'))

diferenca = tomate_um_ano_atras - tomate_hoje
inflacao = (diferenca / tomate_hoje) / tomate_hoje *100

print('A diferença de preço do KG do tomate em um ano é de: \n {:.2f}'.format(diferenca))
print('A inflação do KG do tomate em um ano é de \n{:.2f}%'.format(inflacao))


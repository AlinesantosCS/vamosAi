lista = [2,2,-2]
positivo_numero = 0
for numero in lista:
    if numero > 0:
        positivo_numero += numero # some o valor de n ao total já computado
print('A soma dos elementos negativos é igual a {}'.format(positivo_numero))

'''sum deve receber um iterável (ou seja, uma lista, uma tupla, etc, e ele retorna a soma dos elementos deste iterável). A cada iteração do for, a variável n assume um dos valores da lista, que no caso só tem números, e números não são iteráveis
'''

# COM FUNÇÃO
def positive_sum(arr):
    positivo_numero = 0
    for numero in arr:
     if numero > 0:
        positivo_numero += numero
    return print(positivo_numero )

lista = [2,2,-2]
positive_sum(lista)





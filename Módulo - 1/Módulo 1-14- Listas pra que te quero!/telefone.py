'''Escreva uma função que receba um array(lista) 
de 10 números inteiros (entre 0 e 9) . Esta função 
deve retornar uma string na qual esses números formam
 um número de telefone (estilo americano como no exemplo).'''

def create_phone_number(lista):
    # Escreve sua lógica aqui
    num1 = lista[0]
    num2 = lista[1]
    num3 = lista[2]
    num4 = lista[3]
    num5 = lista[4]
    num6 = lista[5]
    num7 = lista[6]
    num8 = lista[7]
    num9 = lista[8]
    num10 = lista[9]


    return (f'({num1}{num2}{num3}){num4}{num5}{num6} - {num7}{num8}{num9}{num10} ')

lista = (1,2,3,4,5,6,7,8,9,1)
print(create_phone_number(lista))


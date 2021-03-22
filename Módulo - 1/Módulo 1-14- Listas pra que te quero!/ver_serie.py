ver_series = ["Mandaloriano","Breaking bad","This is us"]


x = 0
while x < len(ver_series):
    print(f"A série {ver_series[x]} está na posicao {x}.")
    x = x + 1

def reverse_string(str):
 str = str[::-1]
   
 return (str)



str = ["1", "2", "3", "4"]
reverse_string (str)

'''
O reverse de listas em Python reverte a lista in place, 
alterando os valores da lista ao invés de criar uma lista nova 
escrita ao avesso. Como strings em Python são imutáveis, não faz muito sentido que elas suprtem o método reverse.
'''
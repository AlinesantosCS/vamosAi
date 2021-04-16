def reverse_string(str):
    str = str[::-1]
   
    return (str)


str = ["1", "2", "3", "4"]
reverse_string (str)

'''O reverse de listas em Python reverte a lista in place, alterando os valores da lista ao invés de criar uma lista nova escrita ao avesso. Como strings em Python são imutáveis, não faz muito sentido que elas suportem o método reverse.

Um slice como "abcdefghijklm"[1:9:2] pega os elementos da posição 1 até a 9, de 2 em 2. O slice [::-1], pega os elementos do início ao fim, andando de trás pra frente.
'''
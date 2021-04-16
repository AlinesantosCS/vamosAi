import math
from math import sqrt,floor
# Biblioteca random da classe random - 
# Numéros aleátorios de 0 a 1 em float
import random
import emoji



num = int(input("Digite um numero: "))
""" 
floor - arrendona para baixo
"""

#  Raiz quadrada - Arrendona pra cima
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num,math.ceil(raiz)))

numero_1 = random.random()
#  Números inteiros
numero_2 = random.randint(1,10)
print(numero_1)
print(numero_2)

# Py Pi é um indice de pacotes extras do Python
print(emoji.emojize("Olá mundo :bowtie:", use_aliases=True))
print(emoji.emojize("Python é :polegar_para_cima:", language='pt'))
print(emoji.emojize("Python is fun :red_heart:"))
print(emoji.emojize("Python is funnn :heart_eyes:"))
print(emoji.emojize("Python is fun :broken_heart:"))



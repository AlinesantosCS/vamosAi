# Converte uma string em uma lista.
s = list("Ordem e Progresso")
print(s)

# Converte uma lista em uma string.
l = ['O', 'r', 'd', 'e', 'm', ' ', 'e', ' ', 'P', 'r', 'o', 'g', 'r', 'e', 's', 's', 'o']
print(''.join(l))

'''
strings são imutáveis -> Não remover ou adiconar, ao não ser fazendo uma cópia da string assim, gasrando mais memória
Listas são mutáveis -> posso remver e adionar a própria lista sem precisar fazer uma cópia
'''

help(list)
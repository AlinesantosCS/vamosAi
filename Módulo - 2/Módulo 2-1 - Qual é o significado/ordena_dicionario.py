# dicionario = {"a": 2, "b": 3, "c": 1}

# # O método items() dos dicionários retorna o par (chave, valor)
# # como tuplas de tamanho 2
# print (dicionario.items())

# print(sorted(dicionario.items(), key=lambda x: x[1]))


# def ordena_dicionario(dicionario):
#   # Implemente a lógica da função aqui
#   ordena = (sorted(dicionario.items(), key=lambda x: x[1])
#   for ordernas in ordena:
#     print(ordernas)
#   return ordenas

dicionario = {"a": 2, "b": 3, "c": 1}
# ordena_dicionario(dicionario)

for item in sorted(dicionario, key = dicionario.get):
    print(dicionario[item])
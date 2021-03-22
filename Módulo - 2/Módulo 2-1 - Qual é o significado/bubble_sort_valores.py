
dicionario_inicio = {"a": 2, "b": 3, "c": 1}
dicionario_ordenado = {}

# retorna valor 
# print(dicionario_inicio['a'] )
# Adiciona uma nova chave
dicionario_inicio["d"] = 5
# print(dicionario_inicio)


for elemento_valores in sorted(dicionario_inicio.values()):
    # ordena os valores
    # print(elemento_valores)
    for elemento_chaves in dicionario_inicio:
        # pega as chaves
        #  print(elemento_chaves)
         if elemento_valores == dicionario_inicio[elemento_chaves]:
            #  quando os valores forem iguais aos valores do retorno de cada chave
            # print(elemento_valores)
           print('Validação de cada valor e suas respectivas chaves',dicionario_inicio[elemento_chaves])
           dicionario_ordenado[elemento_chaves] = dicionario_inicio[elemento_chaves]
           print(dicionario_ordenado[elemento_chaves])



# print(dicionario_inicio)
print(dicionario_ordenado)




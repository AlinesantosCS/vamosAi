dicionario_inicio = {"a": ["a", "b", "c"], "b": [1, 2, 3, "b"]}

for elemento in dicionario_inicio:
    if elemento in dicionario_inicio:
        dicionario_inicio[elemento] = True
       
    else:
         dicionario_inicio[elemento] = False
         
print(dicionario_inicio)




def procura_chave_na_lista(dicionario):
    # Implemente sua lógica aqui
    if dicionario.values() == [] and dicionario == {}:
        dicionario = {}
    else:
        for elemento in dicionario:
            if elemento in dicionario:
                dicionario[elemento] = True
            
            else:
                dicionario[elemento] = False
    return dicionario
            



dicionario_inicio = {"a": [], "b": [1, 2, 3, "b"]}
procura_chave_na_lista(dicionario_inicio)

       
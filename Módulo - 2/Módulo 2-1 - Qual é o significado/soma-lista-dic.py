def listas_para_dicionario(lista1, lista2):
  # Implemente a lógica da função aqui
  if len(lista1) != len(lista2) or lista1 == [] or lista2 == []:
    dic = {}
    return dic
  else:
    lista1.extend(lista2)
    # zip interes duas ou mais listas
    dic = dict(zip(lista1,lista2))
    # for elementoA in lista1:
    #     for elementoB in lista2:
    #         dic[elementoA] = elementoB
    return print(dic)

   
primeiro = ['a','b','c']
segundo = [10,10,10]
listas_para_dicionario(primeiro, segundo )
print(listas_para_dicionario)
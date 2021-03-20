# ls = ['a', 'b']

# print(dict([ls]))

# dict_as_list = [['a', 1], ['b', 2], ['c', 3]]
# dictionary = dict(dict_as_list)
# print(dictionary )

# a = ['bi','double','duo','two']
# b  = dict((k,2) for k in a)
# print(b)


#Outra forma
def lista_para_dicionario(lista):
  # Implemente a lógica da função aqui
  dic = {}

  if lista == []:
    dic = {}
  else:
    for elemento in lista:
        dic[elemento] = elemento
  return dic



lista =  [1,2,3,4]
print(lista_para_dicionario(lista))


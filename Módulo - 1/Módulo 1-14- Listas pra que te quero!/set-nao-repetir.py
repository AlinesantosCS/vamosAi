# SET
# a  = [1, 2, 2, 3, 3, 4]
# c = set(a )
# print(c)

# def distinct(seq):
#     seq = set(seq)

#     return print(seq)

# a  = [1, 2, 2, 3, 3, 4]
# distinct(a)


#  DUAS LISTAS
# primeira_lista = [1, 2, 3]
# segunda_lista= [3, 4, 5]

# lista_vazia= []

# for elemento in primeira_lista:
#     lista_vazia.append(elemento)

# for elemento in segunda_lista:
#     if elemento not in lista_vazia:
#         lista_vazia.append(elemento)

# print(lista_vazia)

# COM UMA LISTA SOMENTE
def distinct(seq):
  lista = []
  for elemento in seq:
    if elemento not in lista:
      lista.append(elemento)
  return lista

seq = [1,1,1,2,2,2,3,3,4,5,6,6,7,8,9,9]
distinct(seq)


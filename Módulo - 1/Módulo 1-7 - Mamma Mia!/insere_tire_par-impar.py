def insere_par_remove_impar(lista):
   
    for elemento in lista:
        if elemento % 2 == 0 or elemento == 0:
            lista.append(elemento)
        else:
            lista.pop(elemento)
    
    return print(lista)


lista = [1,2,3,4,0]
insere_par_remove_impar(lista)



# lista1 = [4, 3, 2, 5, 7, 6]
# lista2 = []
# for valor in lista1:
#     if valor % 2 == 0:
#         lista2.append(valor)

# print(lista2)
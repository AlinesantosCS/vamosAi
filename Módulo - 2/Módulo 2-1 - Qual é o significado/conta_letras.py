def conta_letras(string):
    # Implemente sua lógica aqui
    if string  == []:
     dic = {}
    else:
     dic = {}
     for elemento in string :
      dic[elemento] = string.count(elemento)
    
    return dic


string = ['a','b','c']
conta_letras(string)



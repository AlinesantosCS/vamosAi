# Preencha as funções
def cria_fila():
    stack = []
    return stack

def tamanho(fila):
    return len(fila)

def adiciona(fila, valor):
    
    fila.append(valor)
    return fila
  
def remove(fila):
    if fila == []:
        return None
    else:
        return fila.pop(0)


fila = [1,2,3,5]
elemento = 5
teste = adiciona(fila, elemento)
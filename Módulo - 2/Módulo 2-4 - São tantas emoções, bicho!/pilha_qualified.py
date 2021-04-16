# Preencha as funções
def cria_pilha():
    stack = []
    return stack

def tamanho(pilha):
    return len(pilha)
def adiciona(pilha, elemento):
    
    pilha.append(elemento)
    return pilha

def remove(pilha):
    if pilha == []:
        return None
    else:
        return pilha.pop()


pilha = [1,2,3]
elemento = 5
teste = adiciona(pilha, elemento)

def insere_par_remove_impar(lista):
    novaLista = cria_pilha()
    for elemento in lista:
        if elemento % 2 == 0 or elemento == 0:
           adiciona(novaLista, elemento)
        else:
           remove(novaLista)
    return novaLista



lista = [1,2,3,4,0]
insere_par_remove_impar(lista)
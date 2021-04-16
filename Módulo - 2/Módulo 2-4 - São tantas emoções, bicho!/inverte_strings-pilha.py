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

def inverte_texto(texto):
    novaLista = cria_pilha()
    for texto in novaLista:
        print(adiciona(novaLista, texto))
        novaLista = novaLista[::-1]

    remove(novaLista)
    
    return print(novaLista)


texto = ["a","l","i"]
# texto.reverse()
# print(texto)
teste = inverte_texto(texto)
print(teste)




def palindromo(s):
   novaLista = cria_pilha()
   for letra in texto:
        adiciona(novaLista, letra)
   
   OutraPilha = cria_pilha()
    
   for letra in range(0,tamanho(novaLista)):
        adiciona(OutraPilha,remove(novaLista))
        
    converterString = ""
    for string in OutraPilha:
      converterString = converterString + string
      
     if converterString == s or converterString == "":
        True
     else:
        False
#sum(dic. values())
def soma_valores(dicionario):
    # Implemente sua lógica aqui
    if dicionario == {}:
        return 0
    else:
        return sum(dicionario.values())

dic = {}
print(soma_valores(dic))
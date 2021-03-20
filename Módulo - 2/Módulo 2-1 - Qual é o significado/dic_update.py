def adiciona_chave_e_valor():
    dicionario = {"1+1": 2, "1+2": 3}
    # Adicione o novo par de chave e valor aqui
    adicionar_dic = {"1+3": 4}
    dicionario.update(adicionar_dic)
    print(dicionario)
    return dicionario

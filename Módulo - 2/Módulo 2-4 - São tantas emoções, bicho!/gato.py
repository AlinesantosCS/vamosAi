class Gato:
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor
    def miar(self,miou):
        self.miou= miou
        if miou == 'Sim':
            print('miaaaaaaw')
        else:
            print(False)

    def limpar(self,banhou):
        self.banhou = banhou   
        if banhou == True:
            print('Chorando')
        else:
            print('Correu')

gato = Gato('Chicão',"Marrom")
gato.miar('Sim')
gato.limpar(False)
class Relogio:
    def __init__(self,tamanho,cor):
        self.tamanho = tamanho
        self.cor = cor
    def funcionar(self,teste):
        self.teste =  teste
        if teste == "sim":
            print(True)
        else:
            print(False)


relogio = Relogio("Grande","Ouro")
relogio.funcionar("sim")

       
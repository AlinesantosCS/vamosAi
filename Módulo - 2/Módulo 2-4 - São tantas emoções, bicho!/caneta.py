class Caneta:
    def __init__(self,cor,marca):
        self.cor = cor
        self.marca = marca
    
    def rabiscar(self,rabiscou):
        self.rabiscou = rabiscou
        if rabiscou == "sim":
            print(True)
        else:
            print(False)

caneta = Caneta('Rosa',"Bic")
caneta.rabiscar('sim')
           
class Automovel:
      
    def informacoes(self,tipo,modelo,ano,quilometragem):
        self.tipo = tipo
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem

        return print(tipo,modelo,ano,quilometragem)

        

class Carro(Automovel):
    def __init__(self,nome):
        self.nome = nome
      

    def informacoes(self,tipo,modelo,ano,quilometragem):
        return tipo,modelo,ano,quilometragem


class Moto(Automovel):
    def __init__(self,nome):
        self.nome = nome
      

    def informacoes(self,tipo,modelo,ano,quilometragem):
        return tipo,modelo,ano,quilometragem
       
print(Automovel.informacoes)
automovel = Automovel()
automovel.informacoes("Esportivo","LXS","2010","10.000")
print(automovel)

car = Carro("Ferrari")
print(car.nome)
print(car.informacoes("esportiv","812","2017","0"))


moto = Moto('Honda')
print(moto.informacoes("Comum","CG 160","2008","20.000"))



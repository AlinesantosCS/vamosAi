class Automovel:
      
    def __init__(self,tipo,modelo,ano,quilometragem):
        self.tipo = tipo
        self.modelo = modelo
        self.ano = ano
        self.km_rodado = quilometragem


auto = Automovel("Esportivo","LXS","2010","10.000")   
print(auto.tipo)    
print(auto.modelo)
print(auto.ano)
print(auto.km_rodado)      
# Definir o nome da classe com a primeira letra maiuscula
#Pizza_da_gi
class Pizza:
    def __init__ (self,massa,recheio,molho):
        # instancia quando dar caracteristicas ao objeto
        # self referencia a classe Pizza, ou seja refeerencia a si mesmo
        self.massa = massa
        self.recheio = recheio
        self.molho = molho

    def comer(self, racao):
        #classe pizza vai ter a ração parâmetro e recebera o atributo
        self.racao = racao 
    
    def dormir(self,lugar):
        self.lugar = lugar
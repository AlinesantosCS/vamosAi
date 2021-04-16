'''
Polimorfismo você subscreve um método de uma classe que é feito a partir da herança, pois 
tenho herdar alguma coisa e modificar comportamento
'''

class Pizza:
    pedaços = 8

    @classmethod
    def mudar_tamanho(cls,pedaços):
        cls.pedaços = pedaços

    @staticmethod
    def ingredientes():
        return 'Ingredientes'

# HERANÇA PIZZA
class Mussarela(Pizza):

    @staticmethod
    #Subscreveu um método da classe Pizza
    def ingredientes():
        return ['Molho de tomate', 'queijo', 
        'cebola','óregano','azeitona']

print(Pizza.ingredientes)

print(Mussarela.ingredientes())

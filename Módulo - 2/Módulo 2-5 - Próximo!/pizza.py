'''
self -> Referência a instância, pegar um exemplo da classe. SELF É A INSTÂNCIA
cls -> Referência a classe, ou seja conteúdo da classe que são os elementos eternizados na classe. REFERÊNCIA A CLASSE EM SÍ
'''

'''
TIPOS DE MÉTODOS
Métodos de instância - self
Métodos de classe - @classmethod
Métodos estáticos - @staticmethod

'''
# Pizza é a forma 
class Pizza:
    pedaços = 8

    def __init__(self,sabor):
        self.sabor = sabor
    
    def pegar_pedaço(self):
        # MÉTODO DE INSTÂNCIA
        self.pedaços -= 1
    
    # Muda a classe em si
    @classmethod
    def mudar_tamanho(cls,pedaços):
        cls.pedaços = pedaços
    
    # Não recebe nenhum atributo, não interage com nada da classe
    @staticmethod
    def ingredientes():
        return 'Molho de tomate, queijo e cebola'

# instânca da Pizza
# mussarela = Pizza() precisa de um valor que é o sabor, pois essa classe é inicilizadora
mussarela = Pizza('mussarela')
print(mussarela.sabor) # mussarela
print(mussarela.pedaços) # 8
mussarela.pegar_pedaço() 
print(mussarela.pedaços) # 7

# Tem 8 pedaços porque é atributo de self copiou o atributo comum a toda a classe e aqui na classe Pizza o pedaços é um elemento comum de todos, por definição a pizza continua tendo 8 pedaços
print(Pizza.pedaços) # 8

mus = Pizza('mussarela')
print('PIZZA',mus.pedaços) # 8
Pizza.mudar_tamanho(12)
print('Nova PIZZA',mus.pedaços) # 12


mus= Pizza('mussarela') 
mus.pegar_pedaço() 
print(mus.pedaços) # 11

print(Pizza.pedaços) # 12 -  Pizza é a forma

# Chama a função sem precisar criar uma instância
print(Pizza.ingredientes())
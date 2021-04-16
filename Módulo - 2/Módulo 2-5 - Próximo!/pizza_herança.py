# SUPERCLASS
class Pizza:
    pedaços = 8

    @classmethod
    def mudar_tamanho(cls,pedaços):
        cls.pedaços = pedaços

# HERANÇA PIZZA
class Mussarela(Pizza):
    ...

# HERANÇA PIZZA
class Calabresa(Pizza):
    ...
# SUBCLASS DA SUBCLASS - HERANÇA MÚLTIPLA -  CLASS PIZZA ESTÁ POR ASSOCIAÇÃO, NÃO PRECISSANDO EXPLICITAR
class MeioAMeio(Mussarela,Calabresa):
    ... 

print(MeioAMeio.pedaços)
print(Calabresa.pedaços)

MeioAMeio.mudar_tamanho(10)
print(Calabresa.pedaços)
print(Mussarela.pedaços)
print(MeioAMeio.pedaços)
print(Pizza.pedaços)
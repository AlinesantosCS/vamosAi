# Boa prática colocar como subclasse o object
class Mamifero(object):
    def __init__(self, cor_pelo, genero, andar):
        self.cor = cor_pelo
        self.genero = genero
        self.num_pernas = andar

    def falar(self):
        print("Sou um mamífero!!De cor", self.cor)

    def andar(self):
        print("Estou andando sobre {} patas".format(self.num_pernas))

    def amamentar(self):
        if self.genero.lower()[0] == 'm':
            print("Machos não amamentam!!")
            return
        print("Estou amamentando meu filhote")


class Pessoa(Mamifero):
    def __init__(self, cor, genero, andar, cabelo):
        # Nome da classe, self(vem dos métodos).nome_método(métodos)
        # Acessa os métodos da classe pai 
        super(Pessoa, self).__init__(cor, genero, andar)
        self.cabelo = cabelo

    def falar(self):
        super(Pessoa,self).falar()
        print("Olá eu sou uma pessoa polimórfica")


rex = Mamifero("marrom", "macho", 4)
julia = Pessoa("preta", "fêmea", 2, "morena")
claudia = Pessoa("preta", "fêmea", 2, "loira")
julia.amamentar()
claudia.amamentar()


julia.andar()
julia.falar()












class NPC: #Classe Base, Pai ou Super
    def __init__(self,nome,time,forca,municao):
        # Variável do próprio elemento = parâmetro do método
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        # Não é parâmetro porque são valores fixos
        self.vivo = True
        self.energia = 100
    def info(self):
        print("Nome: "    + self.nome)
        print("Time: "    + str(self.time))
        print("Força: "   + str(self.forca))
        print("Munição: " + str(self.municao))
        # Operador ternário
        print("Vivo: "    + str("sim" if self.vivo else "não"))
        print("Energia: " + str(self.energia))
        print("-------------------------------------")

class Soldado(NPC):
    # Pega os parA^metros da classe pai
    def __init__(self,nome,time):
        # Variáveis da classe Pai
        self.forca = 200
        self.municao = 200
        #  Chama o contrutor da classe Pai, chamando todos os parâmetros
        super().__init__(nome,time,self.forca,self.municao)

class Guarda(NPC):
    def __init__(self,nome,time):
        self.forca = 100
        self.municao = 20
        super().__init__(nome,time,self.forca,self.municao)

class Elite(NPC):
    def __init__(self,nome,time):
        self.forca = 400
        self.municao = 500
        super().__init__(nome,time,self.forca,self.municao)

        # Chamando a classe info que está na classe Pai
    def info(self):
        # O super chama a classe que está no Pai
        super().info()



# Instanciar objeto
s1 = Guarda("Olho vivo",1)
s2 = Soldado("Bala na agulha",1)
s3 = Guarda("Olho Ninja",1)
s4 = Guarda("Super atento",2)
s5 = Guarda("Tiro certo",2)
s6 = Guarda("Samurai",2)

s1.vivo = False
s6.vivo = False 

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.info()
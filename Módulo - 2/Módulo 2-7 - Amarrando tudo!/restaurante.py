class Pessoa:
    def __init__(self,nome,cpf,telefone,rg):
        self.nome     = nome
        self.cpf      = cpf
        self.telefone = telefone
        self.rg       = rg
        
    def exibir(self):
        print("-------------------------------------")
        print("Nome: "    + self.nome)
        print("CPF - CNPJ: "    + str(self.cpf))
        print("Telefone: "   + str(self.telefone))
        print("RG: " + str(self.rg))
        print("-------------------------------------")

class Entregador(Pessoa):
    def __init__(self, nome, cpf, telefone, rg,veiculo):
        self.veiculo = veiculo
        super().__init__(nome, cpf, telefone, rg)

    def tempo(self,minutos):
        self.min = int(minutos)
        if self.min >= 60:
            return print("Dentro do esperado, parábens!\nBonificação - R$ 100,00\n\n\n")
        elif self.min > 120:
            return print("Entrega bastante demorada,  terá dimuição de entragas, acione o atendimento\n\n\n")
        elif self.min < 60:
           return print("\nEntrega muito rápida, bonificação será avaliada de acordo com a segurança da entrega e " 
           "do entragador, \nem torno de 15 dias terá a sua resposta.\n\n\n")
        

class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, rg,rua,cidade,numero,estado):
        self.rua = rua
        self.cidade = cidade
        self.casa = numero
        self.estado = estado
        super().__init__(nome, cpf, telefone, rg)


    

    def receber(self,entrada):
        self.recebeu = entrada
        if self.recebeu.lower()[0] == 's':
            return print("***Entrega concluída***")
        else:
            return print("***Problemas na entrega, iremos reembolsar.***")


class ProprietarioRestaurante(Pessoa):
    def __init__(self, nome,telefone,cnpj):
        self.nome = nome
        self.telefone = telefone
        self.cnpj = cnpj
    
    def exibir(self):
        # Sofre Polimorfismo
        self.cpf = self.cnpj
        self.rg  = None
        super().exibir()

    def cardapio(self):
        print("\n\n{0:^80}".format("CARDÁPIO"))
        print(90*'~')
        print("Tilápia à Meunière")
        print("400g de filet de tilápia grelhado com molho especial de alcaparras,\n champignon e arroz com brócolis e legumes.")
        print((90*'~') + "\n")

        print(90*'~')
        print("Tilápia Coco Bambu")
        print("Filé de Tilápia grelhado sobre camadas de batata inglesa, coberto com delicioso molho\n agridoce de mostarda, cebola, alcaparras, tomate, estragão e salsinha. \nMolho servido a temperatura ambiente. Acompanha arroz branco.")
        print((90*'~') + "\n")

        print(90*'~')
        print("Carne de Sol do Sertão")
        print("Arroz de leite coberto com carne de sol desfiada e refogada na \nmanteiga da terra com cebola roxa, nata e coentro. \nGratinada com queijo coalho. Acompanha macaxeira frita.")
        print((90*'~') + "\n")

        print(90*'~')
        print("Cachaça Coco Bambu")
        print("Feita em parceria com a Vale Verde,  a cachaça Coco Bambu tem um aroma e um sabor inconfundível.\n Envelhecida 3 anos em barril de carvalho, \nela é uma novidade que vai cair no gosto de quem aprecia uma bebida de qualidade")
        print((90*'~') + "\n")

        
        

primeiro = Entregador("Henrique Santos",'467-755-968.07','4748-5560','51.406-141.7','Carro')
primeiro.exibir()
primeiro.tempo(1)

segundo = Cliente("Adeneilson Pereira","56847158202",'45478890','5458798705','ruas da libras','Sorocaba','90',"São Paulo")
segundo.exibir()
segundo.receber("Sim,recebi")

terceiro = ProprietarioRestaurante("Alana Maurina","4145-590",'56998874561225')
terceiro.exibir()
terceiro.cardapio()
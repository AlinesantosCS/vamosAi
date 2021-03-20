class Cachorro:
    def __init__(self,nome,cor,raca,porte,qtd_patas, ):
        self.nome = nome
        self.cor = cor
        self.raca = raca
        self.porte = porte
        self.qtd_patas = qtd_patas
       

    def comer(self, racao):
        #classe pizza vai ter a ração parâmetro e recebera o atributo
        self.racao = racao 
    
    def dormir(self,lugar):
        self.lugar = lugar
    
    def latir(self):
        print("au au")
    
    def fazer_coco(self,onde_faz):
        self.onde_faz = onde_faz
    
    def xixi(self,fazer_xixi):
        self.fazer_xixi = fazer_xixi

joaninha = Cachorro("Joaninha", "Preto e branca", "Vira lata","pequeno", 4)

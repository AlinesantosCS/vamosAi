class Atendente(Pessoa):
    def __init__(self,nome):
        super().__init__(nome)
    
    def anotar_pedido(self,prato):
        self.prato = prato
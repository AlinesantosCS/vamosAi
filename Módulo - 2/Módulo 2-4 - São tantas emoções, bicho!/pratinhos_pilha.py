class Prato:
    def __init__(self):
        self.pratinhos = []
    def adicionar(self,louças):
        self.pratinhos.append(louças)
    def largura(self):
        return len(self.pratinhos)
    def tirar(self):
        if self.largura() == 0:
            return None
        else: 
            return self.pratinhos.pop()

chamando_pratos = Prato()
print(chamando_pratos.pratinhos)

chamando_pratos.adicionar("Prato sujo de macarrão")
chamando_pratos.adicionar("Prato sujo de camarão")
chamando_pratos.adicionar("Prato sujo de feijoada")

print(chamando_pratos.pratinhos)

chamando_pratos.tirar()

print(chamando_pratos.pratinhos)
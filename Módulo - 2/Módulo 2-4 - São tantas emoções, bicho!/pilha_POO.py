class Pilha:
    # Lista, pilha.. não precisa colocar como parâmetro, vou direto e criou dentro do def

    def __init__(self, livros_cabeceira):
        self.itens = livros_cabeceira
    
    def append(self, item):
        return self.itens.append(item)
    
    def tamanho(self):
        return len(self.itens)

    def pop(self):
        # referencia o método
        if self.tamanho() == 0:
            return None
        else:
            return self.itens.pop()
    

livros_cabeceira = Pilha(["Josué de Castro"])
print(livros_cabeceira.itens)

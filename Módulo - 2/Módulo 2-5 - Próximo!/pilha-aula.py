# LIFO
class Pilha:
    def __init__(self):
        self.itens = []
    def pop(self):
        return self.itens.pop()
    def push(self,item):
        return self.itens.append(item)
    def tamanho(self):
        return len(self.itens)
        
class Pilha:
    def __init__(self):
        self.queue = []
    def push(self,item):
        self.queue.append(item)
    def pop(self):
        if self.tamanho() == 0:
            return None
        else:
            return self.queue.pop(0)
    def tamanho(self):
        return len(self.queue)

Livros = Pilha()

print(Livros.queue)

Livros.push("Algoritmos para viver")
Livros.push("A Cabana")
Livros.push("A coragem de ser imperfeito")
Livros.push("Python fluente")
Livros.push("Algoritmos de destruição em massa")

print(Livros.queue)
print(Livros.tamanho())

Livros.pop()
print(Livros.tamanho())
print(Livros.queue)
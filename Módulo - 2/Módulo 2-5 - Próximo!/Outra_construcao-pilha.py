class Pilha:
    def __init__(self):
        self.stack = []
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if self.tamanho() == 0:
            return None
        else:
            return self.stack.pop()
    def tamanho(self):
        return len(self.stack)

Livros = Pilha()

print(Livros.stack)

Livros.push("Algoritmos para viver")
Livros.push("A Cabana")
Livros.push("A coragem de ser imperfeito")
Livros.push("Python fluente")
Livros.push("Algoritmos de destruição em massa")

print(Livros.stack)
print(Livros.tamanho())

Livros.pop()
print(Livros.tamanho())
print(Livros.stack)
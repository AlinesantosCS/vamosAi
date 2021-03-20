class Fila:
    def __init__(self):
        self.fila = []
        

    def entrar(self,nome):
      self.fila.append(nome)
      
     

    def sair(self):
       self.fila.pop(0)
       
    

supermercado = Fila()
supermercado.entrar('Eduardo')
supermercado.entrar('Maria')
supermercado.entrar('Luiz')

print(supermercado.fila)
supermercado.sair()
print(supermercado.fila)


supermercado =  Fila()
loterica = Fila()
banco = Fila()

banco.entrar('David')
loterica.entrar('Tiago')
supermercado.entrar('Marcelos')

print(supermercado.fila)
print(loterica.fila)
print(banco.fila)
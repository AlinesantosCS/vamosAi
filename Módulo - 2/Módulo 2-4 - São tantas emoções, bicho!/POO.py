# ABSTRAÇÃO

'''
É a identificação do que é um grupo, é uma generalização de uma classe. Na abstração não é necessário explicar as caracteristicas de ser, por exemplo de um passáro, podendo explicitar as caraceteristica específica, passáro de bico vermelho, sem necessidade de explicar o que é um passáro porque não faz sentido.
'''

# TIPOS
'''
Abstração de processos - 
Não importa como função ao fundo funciona e sim que a ação é executada, como sorted. Como o voar de um pássaro, não precisa saber como ele voa tecnicamente e sim saber que voa.

Abstração de dados -
é a representação de dados, ou seja é um tipo de dados como strings, int, listas...

Usuário pode criar um tipo de dados tendo que ter abstração de dados + abstração de processos

 2 + 2 <- é um tipo numérico()abstração de dados

'''

# CLASSES
'''
É uma estrutura de dados para fazer uma abstração de dados, assim craindo o próprio tipo, como abstração de pessoas, algo genérico.
'''



# ATRIBUTO
'''
São as características da classe, adjetivando.
"São as varáveis internas de uma abstração de dados"
'''

# MÉTODOS
'''
São as ações: divisão, subtração
É uma abstração de processos.
Método manipula o estado do atributo para isso é necessário relacionar a classe com o método com o "sel"
'''
# INSTÂNCIA
'''
É um exemplo de um passáro, ou seje uma abstração da classe,
Enquanto instância é um objeto especfico a classe é genérica
'''
# Classe
class Passaro:
    
    # Atributo
     estado = 'indefinido'
     # método é uma varável interna de uma classe
    def voar(self):
     self.voar = 'voando'
     print(self.estado)
    def pousar(self):
        self.pousar = 'Parado'
        print(self.estado)
        
#Instância
p1 =  Passaro()
p2 = Passaro()




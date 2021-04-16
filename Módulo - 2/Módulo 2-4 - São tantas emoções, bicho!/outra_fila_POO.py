# CONCEITO CLS E SELF
'''
self -> Referência a instância, pegar um exemplo da classe.
cls -> Referência a classe, ou seja conteúdo da classe que são os elementos eternizados na classe.
'''
class Fila:
    # ABSTRAÇÃO DE DADOS
    '''
    Abstração de qualquer tipo de Fila
    - Supermercado
    - Processos
    ...
    '''
    #  Global - Forma
    c_fila = [] # atributo - Pois é um característica  comum que será mantida em toda classe(objetos)

    @classmethod # Explicita que é um método classe
    #  escopo compartilhado
    def c_entrar(cls,obj): # Referência a própria classe -  Manipula a classe
        cls.c_fila.append(obj)
        print(cls.c_fila)
    
    #  MANIPULAÇÃO DO EXEMPLO, REPRESENTADA PELO TIPO DE DADO
    def __init__(self): # Inicia o exemplo ou instância
        self.s_fila = [] # Instância - único sendo que não vai ser compartilhado para orutros métodos
    def s_entrar(self,obj):
        self.s_fila.append(obj)
        print(self.s_fila)

# Acesso ao atributo - Instância
supermercado = Fila()
processos = Fila()
banco = Fila()

# Em todas as classes
supermercado.c_fila
supermercado.c_entrar('Aline') # c_entrar é escopo global(self)
print('SUPERMERCADO',supermercado.c_fila)
print('PROCESSOS',processos.c_fila)
print('BANCO',banco.c_fila,'\n\n')


# Especifica em cada módulo
supermercado.s_fila
# Entra na instância
supermercado.s_entrar('Eduardo')
banco.s_entrar('Maria')
processos.s_entrar('Rafael')

print('SUPERMERCADO',supermercado.s_fila)
print('PROCESSOS',processos.s_fila)
print('BANCO',banco.s_fila)



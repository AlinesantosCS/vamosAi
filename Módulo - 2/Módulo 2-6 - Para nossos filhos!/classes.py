# Atributos:
""" 
1 - Numerador
2 - Denomidador
"""
# Métodos
""" 
1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir
6 - Inverter
7 - Simplificar
8 - Negar
"""

class Fracao:
    #  Neste caso o objeto está sendo construído(self)
    def __init__(self,num,den):
        # Atributo do objeto + váriavel solta
        self.numerador = num
        self.denominador = den
        # Denomidador igual a 0 será considerado 1
        if den == 0:
            self.denominador = 1
        else:
            self.denominador = den
    # Self é referencia o próprio objeto que chamou o método
    def inverter(self):
        return Fracao(self.denominador, self.numerador)
    def negar(self):
        return Fracao(-self.numerador,self.denominador)
    def simplificar(self):
        pass
    def somar(self,outra):

        pass
    def subtrair(self,outra):
        return self.somar(outra.negar())

    def multiplificar(self,outra):
        # Fração que chamou esse método * e parâmetro da função
        numer = self.numerador*outra.numerador
        denom = self.denominador * outra.denomidador
        return Fracao(numer,denom)
    def dividir(self,outra):
        return self.multiplificar(outra.inverter())


 
# Novo objeto do tipo Fracao
a = Fracao(10,20)
b = Fracao(10,20)
print(type(a))
print(a.numerador)
print(a.denominador)

resultado = a.multiplificar(b)

# self referencia o objeto e seus métodos ~ den e num
# c = a.inverter()
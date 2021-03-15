print("Qual é a minha idade ?")
idade = [18,19,21,22,23,24,25,26]

contador = 0
while contador < len(idade):
    print(idade)
    break

escolha = int(input("Escolha a idade ? "))
if escolha == 23:
    print('ACERTOOOU')
else:
    print('ERROOOU')

numero_secreto = 23
numero_secreto = 0

for contador in range(0,3):

    numero_secreto = int(input("Digite um número: "))
    if numero_secreto == 23:
        print("ACERTOU MISERÁVI")
        break
    else:
        print("ERROOOU!!")
print("Qual é o desenho que é brasileiro ?")
desenho = ["\n[1] - Coragem, o cão covarde","\n[2] -Irmão do Jorel","\n[3] - Os setes monstrinhos"]

for escolha in desenho:
    print(escolha)

escolha = int(input("Escolha um número: "))
if escolha == '2':
    print('ACERTOU')
else:
    print('ERROU')
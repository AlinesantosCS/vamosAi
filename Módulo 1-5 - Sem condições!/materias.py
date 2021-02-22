nota_matematica = float(input('Qual é a sua nota em matemática ?'))
nota_biologia =  float(input('Qual é a sua nota em biologia ?'))
nota_portugues = float(input(' Qual é a sua nota em português ? '))

media = ((nota_matematica + nota_biologia + nota_portugues) / 3)

if media >= 6:
    print('Estude mais um pouco!')

else:
    print("Você precisa estudar mais")

   
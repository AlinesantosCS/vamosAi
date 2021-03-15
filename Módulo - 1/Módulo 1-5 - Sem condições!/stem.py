acertou = 0
print(' JOGO DE ADIVINHAÇÃO DA MARIE CURIE')
print('Digite qual alternativa é verdadeira A, B ou C.')

pergunta_1 = input(' Pergunta 1 - Qual área ela trabalhou ?\n A - Engenharia\n B - Ciência\n C - Tecnologia\n Escolha uma alternativa: ')
pergunta_2 = input(' Pergunta 1 - A causa da morte de Marie Currie está relacionado ao trabalho dela, qual foi a doença ?\n A - Aids\n B - Leucemia\n C - Pneumonia\n Escolha uma alternativa: ')
pergunta_3 = input(' Pergunta 1 - Quais dessas alternativas é verdadeira ?\n A - Ela não tinha nenhum admirador conhecido na área, inclusive Albert Einstein criticava Marie.\n B - Os cadernos dela não são  radioativos\n C - Ela foi educada em segredo\n Escolha uma alternativa: ')

if pergunta_1.upper() == 'B':
    print("Acertou! Ela foi uma cientista bem foda!")
    acertou+= 1
else:
    print("Errou! Ela foi uma cientista bem foda!")

if pergunta_2.upper() == 'B':
    print("Acertou! Ela morreu de leucemia em decorrência de contato constante com radiotividade.")
    acertou+= 1
else:
    print("Errou! Ela morreu de leucemia em decorrência de contato constante com radiotividade.")

if pergunta_3.upper() == 'C':
    print("Acertou! Isso ocorreu porque na época os russos consideravam educar mulheres uma atividade ilegal :/ ")
    acertou+= 1
else:
    print("Errou! Isso ocorreu porque na época os russos consideravam educar mulheres uma atividade ilegal :/ ")

print(f'Você acertou {acertou} questões!')
print('MARIE CURIE')
print('cientista responsável por descrever os elementos químicos Polônio e o Rádio e primeira mulher a ganhar um Prêmio Nobel — Física (1903) e Química (1911).')

            
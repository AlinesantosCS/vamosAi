def calcule_media(nota_1,nota_2,nota_3):

    media = (nota_1 + nota_2 + nota_3) / 3

    print('#'*30)
    print(f'Sua média é {media}')
    print('#'*30)

calcule_media(10,10,10)
calcule_media(5,6,6.6)
calcule_media(7,1,4)

# a = '1'
# print(a.center(50))#Válido somente para strings
# print("{:#^60}".format("Digite a sua nota: "))
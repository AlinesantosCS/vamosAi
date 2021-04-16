lista_de_pessoas = []

lista_de_pessoas.append({
    "nome": "Jefferson Felix",
    "idade": 22,
    "telefones": ["2221-2222", "98111-1111"]
})

lista_de_pessoas.append({
    "nome": "Nathan Cutrin",
    "idade": 23,
    "telefones": ["3333-2222"]
})

# Pega a posição da lista que são dicionários com espaços quebra a frase e pegar a segunda posição do nome
print(lista_de_pessoas[1]["nome"].split(" ")[1])

for pessoa in lista_de_pessoas:
    for tel in pessoa["telefones"]:
        print(tel)

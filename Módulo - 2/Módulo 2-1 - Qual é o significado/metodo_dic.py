musica = {}
musica['Fresno'] = 'Maré Viva'
musica['Música favorita'] = 'Maior que as muralhas'

frase = {"EMO": "DEMAIS HAHAH"}

musica.update(frase)
print(musica,'\n')

for chave in musica.keys():
    print(chave,'\n')

for valores in musica.values():
    print(valores,'\n')

print(musica.get('Fresno'))
nomes = ['aline','natália','karla','frida','frida','grace']
# repartir a lista
# aparece somente os primeiro três
print(nomes[:3]) 
print(nomes[0:3])
print(nomes[::2])
# precisa indicar o nome do elemento
nomes.remove('karla') 
# deixa o array em ordem alfabética, números também funciona
nomes.sort()
print(nomes)
# conta o nome está sendo repetidas
print(nomes.count('frida'))
print(nomes)
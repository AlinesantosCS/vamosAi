#  Github jobs retorna as vagas disponiveis no Github
from view import VagasView
# Chamando a nossa classe View
print("Insira um termo de pesquisa: ")
vagas = VagasView()
# Criando essa coleção de itens
vagas.set_termo(input())
# printando o vagas.resposta
print(vagas.resposta())


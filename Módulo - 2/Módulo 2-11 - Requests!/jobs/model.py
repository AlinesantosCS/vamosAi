# Importa uma biblioteca de requisições
#Permite requisições http
import requests
# import pandas as pd

class GithubModel():
  def __init__(self):
    # Chama a url Jobs - GET
    self.url = 'https://jobs.github.com/positions.json'

  def busca_json(self, termo, pagina):
    resposta = self.chamar(termo, pagina)
     # Retorna as informações em Json pq na documentação é position.json
    return resposta.json()

  def busca_csv(self, termo, pagina):
    resposta = self.chamar(termo, pagina)
    return self.transforma_em_json(resposta.content)

  def chamar(self, termo, pagina):  
    # https://jobs.github.com/positions.json?page=1&search=code
    return requests.get(f'{self.url}?pagina={pagina}&pesquisa={termo}') 

  def transforma_em_json(self,json):
    f = pd.read_json(json)
    return f.to_csv()
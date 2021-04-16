from model import GithubModel

class RequisicaoGithub():
  def __init__(self):
    self.pagina = 1
    self.model = GithubModel()

  def busca(self, termo, retorna_tipo):
    retorna_objeto = []

    if retorna_tipo == "csv":
      retorna_objeto = self.model.busca_csv(termo,self.pagina)
    elif retorna_tipo == "json":
      retorna_objeto = self.model.busca_json(termo,self.pagina)
    
    self.pagina += 1
    return retorna_objeto
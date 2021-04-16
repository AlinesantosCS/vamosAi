from controller import RequisicaoGithub

class VagasView:
  def __init__(self):
    self.controller = RequisicaoGithub()

  def set_termo(self, termo):
    self.termo = termo

  def resposta(self):
    return self.controller.busca(self.termo, "json")
# Uma professora deseja desenvolver um sistema para automatizar
#seu trabalho. Ela precisa criar uma solução onde seus alunos
#consigam inserir suas notas (seja a média geral de todas as
#matérias ou a média de uma única disciplina), receber a média, e
#saber sua situação (aprovação, reprovação ou recuperação).

def disciplina():
    disciplina = input("Qual é o nome da disciplina ")
    atividade_1 = float(input("Qual é a sua nota da sua primeira atividade "))
    atividade_2 = float(input("Qual é a sua nota da sua segunda atividade " ))
    atividade_3 = float(input("Qual é a sua nota da sua terceira atividade "))
    atividade_4 = float(input("Qual é a sua nota da sua quarta atividade "  ))

    media_disciplina = ((atividade_1 + atividade_2 + atividade_3 + atividade_4) / 4)
    if media_disciplina < 5:
      print("REPROVADO NESTA MATÉRIA")
    elif media_disciplina >= 5.0 and media_disciplina < 6.0:
      print("RECUPERAÇÃO NESTA MATÉRIA")
    elif media_disciplina >= 7 and media_disciplina <= 10:
      print("APROVAÇÃO NESTA MATÉRIA")
    else:
      print('ERRO MÉDIA')
    print(f" A sua média na matéria {disciplina} é de {media_disciplina}\n\n")

    return media_disciplina

def media_geral():

  print('NOTA 1')
  media_nome_materia_01 = disciplina() 

  print('NOTA 2')
  media_nome_materia_02 = disciplina() 

  print('MÉDIA GERAL DE TODAS AS MATÉRIAS')
  media_nome_materia = (media_nome_materia_01 + media_nome_materia_02)/2
  if media_nome_materia < 5:
    print("REPROVADO DISPLINAS GERAIS")
  elif media_nome_materia >=5 and media_nome_materia <= 6:
    print("RECUPERAÇÃO DISCIPLINAS GERAIS")
  elif media_nome_materia >=7 and media_nome_materia <= 10:
    print("APROVAÇÃO DISCIPLINAS GERAIS")
  else:
    print('ERRO MÉDIA')

  return media_nome_materia

media_geral_todas_materias = print("Média geral:{0:^20}".format(media_geral()))
print(40*"*")


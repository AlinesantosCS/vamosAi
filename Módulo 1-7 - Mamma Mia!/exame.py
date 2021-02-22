def paciente(resultado):
    titulo = 'PACIENTE - RESULTADOS'
    print(titulo.center(50))

    if resultado >= 7 and resultado <= 10:
       print("{:#^50}".format(" Continuar assim "))
    elif resultado >= 4 and resultado <= 6:
        print("{:#^60}".format(" Buscar se cuidar mais e fazer acompanhamento médico "))
    elif resultado >= 0 and resultado <= 3:
        print("{:#^50}".format(" Procurar a equipe médica "))
    else:
        print("{0:^50}".format("ERRO! Valor inválido"))

paciente(10)
paciente(4)
paciente(0)
paciente(50)

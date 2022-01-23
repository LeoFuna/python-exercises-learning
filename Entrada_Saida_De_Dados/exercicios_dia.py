def imprime_inverso(nome):
    for line in range(len(nome), 0, -1):
        nome_imprimir = ''
        for index in range(line):
            nome_imprimir += nome[index]
        print(nome_imprimir)


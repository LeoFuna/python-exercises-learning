from curses.ascii import isdigit


def imprime_na_vertical(nome):
    n = 0
    while n < len(nome):
        print(nome[n])
        n += 1


import sys


def soma_numeros():
    dados = input("Digite os números a serem somados: ")
    total = 0
    lista_de_numeros = dados.split()
    for numero in lista_de_numeros:
        if isdigit(numero):
            total += int(numero)
        else:
            print(
                f"Erro ao somar valores, '{numero}' é um valor inválido",
                file=sys.stderr,
            )
    return total


def anota_alunos_aprovados():
    notas = open("notas.txt", mode="r")
    file = open("file.txt", mode="w")
    for line in notas:
        aluno_com_nota = line.split()
        if int(aluno_com_nota[1]) >= 6:
            file.write(f"{aluno_com_nota[0]}\n")
    file.close()
    notas.close()

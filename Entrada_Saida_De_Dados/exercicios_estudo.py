from curses.ascii import isdigit


def imprime_na_vertical(nome):
    n = 0
    while n < len(nome):
        print(nome[n])
        n += 1


def soma_numeros():
    dados = input('Digite os números a serem somados: ')
    total = 0
    lista_de_numeros = dados.split()
    for numero in lista_de_numeros:
        if isdigit(numero):
            total += int(numero)
        else:
            print(f"Erro ao somar valores, '{numero}' é um valor inválido")
    return total


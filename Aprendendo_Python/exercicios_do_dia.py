# 1 - Crie uma função que receba dois números e retorne o maior deles.
def retorna_maior(num1, num2):
    if num1 < num2:
        return num2
    return num1


# 2 - Calcule a média aritmética dos valores contidos em uma lista.
def media_aritmetica(lista):
    total = 0
    for valor in lista:
        total += valor
    return total / len(lista)

# 3 - Faça um programa que, dado um valor n qualquer, tal que n > 1 , imprima na tela um quadrado feito de asteriscos de lado de tamanho n
def forma_retangulo(numero):
    for index in range(numero):
        print(numero * '*')

# 4 - Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres.
# Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"] , o retorno deve ser "Fernanda" 
def retorna_maior_nome(lista_nomes):
    maior_nome = lista_nomes[0]
    for nome in lista_nomes:
        if len(nome) > len(maior_nome):
            maior_nome = nome
    return maior_nome


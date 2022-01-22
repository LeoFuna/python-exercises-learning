# 1 - Crie uma função que receba dois números e retorne o maior deles.
import math


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

# 5 -  Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Crie uma função que retorne dois valores em uma tupla contendo a quantidade de latas de tinta a serem compradas e o preço total a partir do tamanho de uma parede(em m²).
def informa_tinta(tamanho_parede):
    preco_lata = 80
    litros_necessarios = math.ceil(tamanho_parede / 3)
    latas = math.ceil(litros_necessarios / 18)
    tupla = (latas, latas * preco_lata)
    return tupla

print(informa_tinta(55))

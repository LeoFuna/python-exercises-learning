from random import random


class Retangulo:
    def __init__(self, largura, altura):
        self.altura = altura
        self.largura = largura
        self.lados = 4
    
    def calcula_area(self):
        return self.altura * self.largura
    
    def calcula_perimetro(self):
        return 2 * self.altura + 2 * self.largura

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def calcula_area(self):
        return 3.14 * (self.raio ** 2)

# -----------------------------------------------------------

class Item:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco
    

class Pedido:
    def __init__(self, cliente, itens):
        self.cliente = cliente
        self.itens = itens
        self.numero = 0
        self.numero = self.gerar_numero()

    def gerar_numero(self):
        return random() * 10
    
    def calcula_total(self):
        total = 0
        for item in self.itens:
            total += item.preco
        return total

# ----------------------------------------------------

class Tv:
    def __init__(self, polegadas, marca):
        self._polegadas = polegadas
        self._marca = marca
        self.volume = 50
        self.canal = 1
        self.ligada = False

    def gerencia_liga_desliga(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_volume(self):
        if self.volume < 100 and self.ligada:
            self.volume += 1
    
    def diminui_volume(self):
        if self.volume > 1 and self.ligada:
            self.volume -= 1


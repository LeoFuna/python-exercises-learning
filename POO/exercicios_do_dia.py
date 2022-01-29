# Exercicio 1
class Tv:
    def __init__(self, tamanho):
        self.__volume = 50
        self.__canal = 1
        self.__ligada = False
        self.__tamanho = tamanho

    def aumentar_volume(self):
        if self.__volume < 99:
            self.__volume += 1

    def diminiuir_volume(self):
        if self.__volume > 0:
            self.__volume -= 1

    def modificar_canal(self, canal):
        if 0 < canal < 100:
            self.__canal = canal
        else:
            raise ValueError("Canal Indisponível")

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


# Exercicio 2
class Estatistica:
    @classmethod
    def media(cls, lista_numeros):
        return sum(lista_numeros) / len(lista_numeros)

    @classmethod
    def mediana(cls, lista_numeros):
        tamanho_lista = len(lista_numeros)
        numeros_ordenados = sorted(lista_numeros)
        if tamanho_lista % 2 == 0:
            return (
                numeros_ordenados[int((tamanho_lista / 2)) - 1]
                + numeros_ordenados[int(tamanho_lista / 2)]
            ) / 2

        return numeros_ordenados[tamanho_lista // 2]

    @classmethod
    def moda(cls, lista_numeros):
        dicionario = {}
        for numero in lista_numeros:
            if numero in dicionario.keys():
                dicionario[numero] += 1
            else:
                dicionario[numero] = 1
        return max(dicionario, key=dicionario.get)


# Exercicio 3
from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError

    @abstractmethod
    def perimetro(self):
        raise NotImplementedError


class Quadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return self.lado * 4


class Retangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.altura + self.base

    def perimetro(self):
        return self.altura * 2 + self.base * 2


class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * (self.raio ** 2)

    def perimetro(self):
        return 2 * 3.14 * self.raio


# Exercicio 4
# from abc import ABC
class ManipuladorDeLog(ABC):
    @classmethod
    @abstractmethod
    def log(cls, msg):
        raise NotImplementedError


class LogEmArquivo(ManipuladorDeLog):
    @classmethod
    def log(cls, msg):
        with open("log.txt", "a") as arquivo:
            print(msg, file=arquivo)


class LogEmTela(ManipuladorDeLog):
    @classmethod
    def log(cls, msg):
        print(msg)
        pass


class Log:
    def __init__(self, manipuladores):
        self.__manipuladores = set(manipuladores)

    def adicionar_manipulador(self, manipulador):
        self.__manipuladores.add(manipulador)

    def info(self, msg):
        self.__log("INFO", msg)

    def alerta(self, msg):
        self.__log("ALERTA", msg)

    def erro(self, msg):
        self.__log("ERRO", msg)

    def __log(self, nivel, msg):
        for manipulador in self.__manipuladores:
            manipulador.log(self.__formatar(nivel, msg))

    def __formatar(self, nivel, msg):
        return f"{nivel}: {msg}"


# Exercicio 5

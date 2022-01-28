# Exercicio 1
class Tv():
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
            self.__canal  = canal
        else:
            raise ValueError("Canal Indisponível")
    
    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True
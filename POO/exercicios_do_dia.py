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
            return (numeros_ordenados[int((tamanho_lista / 2)) - 1] + numeros_ordenados[int(tamanho_lista / 2)]) / 2
        
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


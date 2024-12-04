## Herencia Múltiple
"""
La herencia múltiple en Python permite que una clase herede características y comportamientos de
más de una clase base. Esto significa que un objeto puede tener atributos y métodos de varias
clases diferentes
"""

#ABC = ABSTRACT BASE CLASS
from abc import ABC, abstractmethod
class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto
    def __str__(self):
        return f'FiguraGeometrica[Ancho: {self._ancho}, Alto: {self._alto}]'

    ## Método abstracto
    # La creación de un metodo abstracto significa que las clases hijas deberán implementar dicho método
    @abstractmethod
    def calcularArea(self):
        pass
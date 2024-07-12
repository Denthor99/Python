from Color import Color
from FiguraGeometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):  # No se usa super para evitar problemas, ya que no sabriamos que metodo __init__ estamos usando
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
    def calcularArea(self):
        return self.ancho * self.ancho

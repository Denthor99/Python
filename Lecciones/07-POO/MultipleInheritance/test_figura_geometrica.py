from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from FiguraGeometrica import FiguraGeometrica

cuadrado1 = Cuadrado(5, 'Rojo')
print(cuadrado1.color)
print(cuadrado1.calcularArea())

## MRO - Method Resolution Order
# Nos permite conocer la jerearquía de clases
# Dentro de esta jerarquía, en caso de existir métodos con el mismo nombre en distintas clases, se ejecutará
# la que se encuentre primero en la jerarquía

# Imprimimimos la jerarquía de clases de la Clase Cuadrado. Modificado ya que hemos añadido una nueva clase padre
print(Cuadrado.mro())

"""
    Salida por consola:
    [<class 'Cuadrado.Cuadrado'>, <class 'FiguraGeometrica.FiguraGeometrica'>, <class 'Color.Color'>, <class 'object'>]
"""

# Si en la clase Cuadradro quisieramos cambiar la jerarquía, deberemos cambiar el orden de las clases padres
"""
    class Cuadrado(Color, FiguraGeometrica):
    
    Salida por consola:
    
"""

## Ejercicio propuesto
# Modifica las clases FiguraGeometrica y Color para encapsular sus atributos
# Crea una nueva clase llamada Rectangulo, donde se deberá calcular el area de un rectancgulo
cuadrado2 = Cuadrado(10, 'Amarillo')
rectangulo1 = Rectangulo(8,15, 'Verde')

# Imprimimos los resultados
print(cuadrado2)
print(cuadrado2.calcularArea())
print(rectangulo1)
print(rectangulo1.calcularArea())

# No se puede instanciar una clase abstracta
# figura = FiguraGeometrica()
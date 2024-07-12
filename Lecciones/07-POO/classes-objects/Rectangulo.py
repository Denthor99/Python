## Ejercicio propuesto
# Crear una clase llamada rectangulo, con dos atributos (base y altura), y un método con el calculo del area
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

# El usuario deberá introducir tanto la base comno la altura
base = float(input('Introduzca la base: '))
altura = float(input('Introduzca la altura: '))

# Creamos la instancia
resultado = Rectangulo(base, altura)

# Mostramos el resultado de la operación
print(f'El area del rectangulo es { resultado.calcularArea() }')
## Ejercicio propuesto
# Crea una clase llamada cubo, donde se le pasará el ancho, alto y profundidad como atributos, y un método
# que calcule el volumen de un cubo
class Cubo:
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcularVolumen(self):
        return self.ancho * self.alto * self.profundidad


# El usuario deberá introducir los 3 argumentos necesarios por teclado
ancho = int(input('Introduce al ancho: '))
alto = int(input('Introduce el alto: '))
profundidad = int(input('Introduce la profundidad: '))

# Creamos la instancia, y posteriormente realizamos el calculo del volumen
resultado = Cubo(ancho, alto, profundidad)
print(f'El vólumen del cubo es { resultado.calcularVolumen() }')
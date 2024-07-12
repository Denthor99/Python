## Ejercicio propuesto
## Clase aritmetica
# Crea una clase donde se le pasen por argumento dos valores
class Aritmetica:
    """
    Clase Aritmetica para realizar las operaciones de sumar, restar, etc
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sumar(self):
        return self.a + self.b

    def restar(self):
        return self.a - self.b

    def dividir(self):
        return self.a / self.b

    def multiplicar(self):
        return self.a * self.b

    def exponente(self):
        return self.a ** self.b


# Definimos un objeto de la clase, y posteriormente probamos todos los métodos creados
resultado = Aritmetica(19,3)

# Suma
print(f'Resultado de la suma: {resultado.sumar()}')

# Resta
print(f'Resultado de la resta: {resultado.restar()}')

# Dividir
print(f'Resultado de la división: {resultado.dividir():.2f}')

# Multiplicar
print(f'Resultado de la multiplicacion: {resultado.multiplicar()}')

# Exponente
print(f'Resultado de la potencia: {resultado.exponente()}')
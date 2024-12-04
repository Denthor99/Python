"""
    Ejercicio Propuesto
    Se deberá crear una clase Persona, que cada vez que se crea un objeto de persona incremente el contador, para usar
    ese valor como su id
"""
class Persona:
    contador = 0

    # Método de clase que incrementará el valor del contador
    @classmethod
    def contadorNew(cls):
        cls.contador += 1
        return cls.contador
    def __init__(self, nombre, edad):
        self.idPersona = Persona.contadorNew()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona[id: {self.idPersona}, nombre:{self.nombre}, edad:{self.edad}]'

# Definimos varias personas
persona1 = Persona("Mario",22)
persona2 = Persona('Carla',19)
persona3 = Persona('Alvaroo',22)

# Comprobamos los resultado
print(persona1)
print(persona2)
print(persona3)
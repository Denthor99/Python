## Herencia
# La herencia no es más que la propgación de atributos y métodos de una clase padre a las distintas clases hijas
class Persona(object):  # Definición de la clase Persona, que hereda de object, la clase base de todas las clases en Python.
    def __init__(self, nombre, edad):  # Constructor de la clase Persona. Inicializa los atributos nombre y edad.
        self.nombre = nombre  # Asigna el valor del parámetro nombre al atributo nombre de la instancia.
        self.edad = edad  # Asigna el valor del parámetro edad al atributo edad de la instancia.

    def __str__(self):  # Sobreescribe el método especial __str__ para definir una representación legible de la instancia como una cadena.
        return f'Persona[{self.nombre}, {self.edad}]'  # Retorna una cadena formateada que incluye el nombre y la edad de la persona.

class Empleado(Persona):  # Definición de la clase Empleado, que hereda de la clase Persona.
    def __init__(self, nombre, edad, sueldo):  # Constructor de la clase Empleado. Inicializa los atributos nombre, edad y sueldo.
        super().__init__(nombre, edad)  # Llama al constructor de la clase base Persona, pasando el nombre y la edad.
        self.sueldo = sueldo  # Asigna el valor del parámetro sueldo al atributo sueldo de la instancia.

    def __str__(self):  # Sobreescribe el método especial __str__ para definir una representación legible de la instancia de Empleado como una cadena.
        return f'Empleado[{super().__str__()}, {self.sueldo}€]'  # Utiliza super().__str__() para obtener la representación de cadena de la instancia de Persona y agrega el sueldo del empleado al final.

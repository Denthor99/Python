class Persona:
    def __init__(self, nombre, edad, apellido):
        self._nombre = nombre
        self._edad = edad
        self._apellido = apellido

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    def mostrarDetalles(self):
        print(f'Mi nombre es {self._nombre} {self._apellido}, y tengo actualmente {self._edad} años.')

    # Método destructor
    def __del__(self):
        print(f'La persona {self._nombre} ha sido eliminada de la base de datos')
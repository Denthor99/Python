## CLASES Y OBJETOS
# Una clase no es más que la plantilla para poder crear objetos
# Cada clase poseé una serie de atributos y métodos
# Un objeto no es más que la instacia de una clase

# Definición de una clase
class Persona:
    """
    Clase abstracta que representa a un individuo.

    Esta clase define los atributos básicos de una persona como nombre,
    edad y apellido. Se utiliza para crear objetos que representen a personas
    con estos datos específicos.
    """

    # Método inicializador (__init__)
    def __init__(self):
        """
        Inicializa una nueva instancia de la clase Persona.

        Este método establece los valores predeterminados para los atributos
        de nombre, edad y apellido. Si se desea personalizar estos valores al
        momento de crear un objeto, se debe pasarlos como argumentos al método.
        """
        self.nombre = 'Paco'  # Nombre por defecto
        self.edad = 19  # Edad por defecto
        self.apellido = 'Pepe'  # Apellido por defecto

# Creación de un objeto de la clase Persona
persona1 = Persona()

# Acceso a los atributos del objeto persona1
print('Clase con valores por defecto')
print(persona1.nombre)  # Imprime el nombre del objeto
print(persona1.edad)  # Imprime la edad del objeto
print(persona1.apellido)  # Imprime el apellido del objeto
print('\n')

## Creación de varios objetos pasando argumentos

class Persona:
    def __init__(self, nombre, edad, apellido):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido

# Creación de un nuevo objeto, al que se le pasarán parametros como argumentos
persona2 = Persona('Daniel', 67, 'Perales')

# Imprimimimos los atributos del objeto recién creado
print('Varios objetos creados, donde se le ha pasado por argumentos los valores de sus atributos')
print(persona2.nombre)
print(persona2.edad)
print(persona2.apellido)
print('\n')

# Crearemos nuevamevente otro objeto, pasandole como argumentos otros valores
persona3 = Persona('Jose María', 34, 'Pavía')
print(persona3.nombre)
print(persona3.edad)
print(persona3.apellido)
print('\n')


## Modificación de los atributos de un objeto
# Es muy sencillo, pues solo tendremos que asignaerle un valor nuevo
print('Modificación de los valores del objeto anterior')

persona3.nombre = 'Jose Carlos'
print(f'El nuevo nombre para el objeto es {persona3.nombre}')


## Métodos de instancia
# Son aquellos metodos que pueden usar los objetos
class Persona:
    def __init__(self, nombre, edad, apellido):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido

    # Definición de un metodo de instacia
    # Es obligatorio añadir self en la definición del método, pues es una referencia a la propia instacia del objeto
    def mostrarDetalles(self):
        print(f'\nMétodo de instancia: Mi nombre es {self.nombre} {self.apellido}, y tengo actualmente {self.edad} años')


# Creamos un nuevo objeto
persona4 = Persona('Jose', 59, 'Merced')

# Invocamos el método de la instancia
persona4.mostrarDetalles()

## self
# Es homologo de la palabra reservada 'this', usada en otros lenguajes
# self no es más que la referencia de una instancia en memoria, por lo que si queremos invocar un método de instancia,
# deberemos crear previamente un objeto o pasar directamente al método de esa clase un objeto en memoria, para que se pueda
# ejecutar sin problemas

# Podemos usar directamente la clase y el método propio de la clase, pero se le deberá pasar por argumento un objeto que
# se encuentre en memoria. No es el método habitual de hacerlo, pues solo se llaman así a los métodos estaticos
Persona.mostrarDetalles(persona1)

## Añadir atributos específicos a un objeto
# Se pueden añadir nuevos atributos a un objeto, pero no se propagará a la clase, por lo que se usará en contadas ocasiones

# Añadimos e imprimimos un nuevo atributo
persona4.whatsapp = 608452316
print(persona4.whatsapp)

# Si vemos los atributos de otros objetos, observamos que efectivamente el atributo anterior no existe
# print(persona1.whatsapp)

## Atributos especiales: tuplas y diccionarios
# El método __init__ puede tener tuplas y diccionarios como argumentos
class Persona:
    def __init__(self, nombre, edad, apellido, *otrosValores, **diccionario):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido
        self.otrosValores = otrosValores
        self.diccionario = diccionario

    def mostrarDetalles(self):
        print(f'\nMétodo de instancia: Mi nombre es {self.nombre} {self.apellido}, y tengo actualmente {self.edad} años. Valores: { self.otrosValores }')


persona5 = Persona('JJ',56, 'Abrahams', 4, 56, 'Gibraltar')
persona5.mostrarDetalles()

## Encapsulamiento
# Por motivos de la seguridad de las clases que hemos creado, en ocasiones no querremos que se accedan de forma pública a
# los distintos atributos y métodos de nuestra clase. Los atributos, por lo tanto deberán solo ser accesible por su clase
# solamente. Deberemos indicar con '_' en los atributos/métodos que queramos 'securizar'. Ahora bien, el guion bajo permite
# que se puedan modificar desde fuera, por lo que deberemos usar el decorador @property para modificar los atributos de una
# forma más elegante, siendo una buena práctica
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

    # Si queremos hacer un atributo que solo sea de modo lectura, deberemos borrar/comentar el setter
    # @edad.setter
    # def edad(self, edad):
    #     self._edad = edad

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    def mostrarDetalles(self):
        print(f'\nMétodo de instancia: Mi nombre es {self._nombre} {self._apellido}, y tengo actualmente {self._edad} años.')
# Definimos un nuevo objeto
persona6 = Persona('Matías', 37, 'Robledo')

# Usamos los getters para acceder a las propiedades protegidas
print(persona6.nombre)
print(persona6.edad)
print(persona6.apellido)

# Si quisieramos modificar la edad, saldría error pues no tenemos definido un setter
# persona6.edad = 15
# print(f'Edad modificada a traves de setter: {persona6.edad}')

# Esto se podría hacer, pero no es recomendado
# persona6._edad = 15

# Eliminamos todos los objetos anteriores:
del persona1
del persona2
del persona3
del persona4
del persona5
del persona6

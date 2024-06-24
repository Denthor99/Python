# Print
# Python nos facilita la tarea de imprimir por consola, usando la función print. Su contenido no debe tener espacios
# Mensaje "hola mundo"
print("Hola mundo")

# Saludos
print("Un saludo tanto a Python como a las personas que estén leyendo este código")

# Imprime del 1 al 10 (un número por línea)
print("1\n2\n3\n4\n5\n6\n7\n8\n9\n10")

# VARIABLES
# Python es un lenguaje no tipado, por lo que podemos asignar cualquier valor a una variable
miVar = "Primera variable"
dosVar = 365
tresVar = True
# cuatroVar = null;    Se debe importar el paquete null
print(miVar)
print(dosVar)
print(tresVar)

# Las variables, tal como dice el nombre, pueden modicar su valor en cualquier punto de la ejecución de un programa
miVar = "Variable modificada"
dosVar = 33
tresVar = False
print(miVar)
print(dosVar)
print(tresVar)

# OPERACIONES CON VARIABLES
# En caso de que las variables contengan valores númericos, se podrán realizar distintas operaciones matemáticas
x = 15
y = 10
# Multiplicacion
print(x * y)

# Division (resultado en decimal)
print(x / y)

# Resto
print(x % y)

# Potencia
print(x ** y)

# DIRECCIÓN DE MEMORIA
# Cada variable se almacena en una dirección de la memoria RAM, cuyo valor es llamado "literal"
# Comprobación de la dirección de memoria de las variables. Deberemos usar el print para visualizar el valor devuelto
# Las direcciones en memoria no son inmutables, ya que pueden ir cambiando cada vez que ejecutemos el programa, ya que
# la memoria RAM es una memoria de tipo volátil
print(id(x))
print(id(y))
print(id(tresVar))

# Prueba sencillita: añade parte de tus datos personales a variables
nombre = "Daniel Alfonso Rodríguez Santos"
telefono = 656423219
email = "darancuga@hotmail.com"
print("Mi nombre es", nombre, ", mi telefono es el", telefono, "y mi email es el", email)

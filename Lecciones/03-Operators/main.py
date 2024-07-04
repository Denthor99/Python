## Operadores aritmeticos

# suma (+)
a = 7
b = 5
print(f'Resultado de la suma: {a + b}')

# Resta (-)
print(f'Resultado de la resta: {a - b}')

# Multiplicación (*)
print(f'Resultado de la multiplicación: {a * b}')

# División, devolviendo un decimal (/)
print(f'Resultado de la division: {a / b}')

# División, devolviendo un entero (//)
print(f'Resultado de la división (int): {a // b}')

# Resto de la división (%)
print(f'Resultado del resto de la división (int): {a % b}')

# Potencia (**)
print(f'Resultado de la potencia: {a ** b}')

## Ejercicio propuesto
# Calcula el area y el perimetro de un rectángulo. El usuario deberá pasar por consola los parametros necesarios
# Definición de variables e inputs correspondientes
area = int(input("Introduce el alto del rectángulo: "))
perimetro = int(input("Introduce el ancho del rectángulo: "))

# Resultado, realizando el correspondiente formateo
print(f"El area del rectángulo es de {area * perimetro}")
print(f"El perimetro del rectángulo es de {(area + perimetro)*2}")


## Operadores de asignación

# Asignación de variables
var1 = 10
print(var1)

# Incremento y reasignación de variables
#var1 = var1 + 2
var1 += 2
print(var1)

# Decremento y reasignación de variables
#var1 = var1 - 2
var1 -= 2
print(var1)

# Multiplicación y reasignación de variables
#var1 = var1 * 2
var1 *= 2
print(var1)

# Division y reasignación de variables
#var1 = var1 / 2
var1 /= 2
print(var1)

## Operadores de comparación
c = 5
d = 3

# Operador "son iguales"
# Devuelve un valor boolean, es esta caso False
resultado = (c == d)
print(f'== {resultado}')

# Operador "es distinto"
# Devuelve True
resultado = (c != d)
print(f'!= {resultado}')

# Operador "mayor que"
# Devolverá True
resultado = (c > d)
print(f'> {resultado}')

# Operador "mayor igual que"
# Devolverá True
resultado = (c >= d)
print(f'>= {resultado}')

# Operador "menor que"
# Devolverá True
resultado = (c < d)
print(f'< {resultado}')

# Operador "menor igual que"
# Devolverá True
resultado = (c <= d)
print(f'<= {resultado}')

## Ejercicio propuesto
# Algoritmo par_impar
# Asignación de variables
num = int(input("Introduzca un número: "))
if (num % 2) == 0:
    print(f'{num} es un número par')
else:
    print(f'{num} es un número impar')

## Ejercicio propuesto
# Dependiendo de la edad que introduzca un usuario, mostrará si es o no mayor de edad
edad = int(input("Introduce tu edad: "))
if edad >= 18:
    print("Es usted una persona mayor de edad")
else:
    print("Usted sigue siendo menor de edad")


## Operadores Lógicos
# and-> Devuelve True si ambos operandos son verdaderos (True)
# or-> Devuelve True en caso de que uno de los operandos sea verdadero (True)
# not-> Devuelve True si el operando es False
# Creamos las variables para el ejemplo práctico
first = True
second = False

# and
resultado = first and second
print(f'and {resultado}')

# or
resultado = first or second
print(f'or {resultado}')

# not
resultado = not second
print(f'not {resultado}')

## Ejercicio propuesto
# Comprobar si un valor introducido por el usuario se encuentra en el rango establecido
# Definición de variables
valor = int(input("Introduce un valor: "))
min = 0
max = 10

# Almacenamos el resultado de los operadores
rango = (valor >= min) and (valor <= max)

# Realizamos la correspondiente sentencia de control
if rango:
    print("El número introducido se encuentra dentro de rango")
else:
    print("El número no se encuentra dentro del rango")

## Ejercicio propuesto
# ¿Podría ir al parque de atracciones?
diaDescuento = True
bonoFamilia = False
asistencia = diaDescuento or bonoFamilia
if asistencia:
    print("Si podría ir al parque de atraciones")
else:
    print("Tendré que esperar a la temporada baja")

## Ejercicio propuesto
# ¿Podría ir al parque de atracciones?
diaDescuento = False
bonoFamilia = False
asistencia = not (diaDescuento or bonoFamilia)
if asistencia:
    print("Tendré que esperar a la temporada baja")
else:
    print("Si podría ir al parque de atraciones")

## Ejercicio propuesto
# Edad de una persona en el rango de los 20 a los 30
edad = int(input("Introduce tu edad: "))
# veintes = edad >= 20 and edad <30
# treintas = edad >= 30 and edad <40

# if usando el operador or
# if veintes or treintas:
#    print("Se encuentra en el rango de los 20's y los 30's")
# else:
#    print("Es menor o mayor a dicho rango")

# if usando elif (else if)
# if veintes:
#    print("Se encuentra en el rango de los 20's")
# elif treintas:
#     print("Se encuentra en el rango de los 30's")
# else:
#     print("Es menor o mayor a dicho rango")

# Realmente, la forma normal de hacerlo es la siguiente
if (edad >= 20 and edad <30) or (edad >= 30 and edad <40):
    print("Se encuentra en el rango de los 20's y los 30's")
else:
    print("Es menor o mayor a dicho rango")

# Ahora especificando más el rango
if edad >= 20 and edad <30:
    print("Se encuentra en el rango de los 20\'s")
elif edad >= 30 and edad <40:
    print("Se encuentra en el rango de los 30\'s")
else:
    print("Edad fuera del rango establecido")

# Ahora vamos a simplificar el uso del operador "and"
if (20 <= edad <30) or (30 <= edad <40):
    print("Se encuentra en el rango de los 20's y los 30's")
else:
    print("Es menor o mayor a dicho rango")

## Ejercicio Propuesto
# El mayor de dos números. Controla si son valores iguales
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 > num2:
    print(f'El número mayor es {num1}')
elif num2 > num1:
    print(f'El número mayor es {num2}')
else:
    print(f'Los valores son iguales')

## Ejercicio Propuesto
# El usuario deberá introducir por teclado la información de un libro
print("Introduzca los siguieentes datos del libro: ")
titulo = input('Introduce el nombre del libro: ')
idLibro = int(input('Introduce el id del libro: '))
precio = float(input('Introduce el precio del libro: '))

# bool no se debe usar para realizar la conversión directamente, pues si introduces cualquier valor lo convierte a "True",
# y si es vacía devuelve "False"
envio = input("El envió es gratuito? (True/False): ")

# Deberemos por tanto realizar una comprobación
if envio == "True":
    envio = True
elif envio == "False":
    envio = False
else:
    envio = "Valor incorrecto"

# Con el siguiente formato de la función print podemos darle el formato de salida que queramos
print(f'''
    Nombre del libro: {titulo}
    Id del libro: {idLibro}
    Precio del libro: {precio}
    Envio gratuito: {envio}
''')
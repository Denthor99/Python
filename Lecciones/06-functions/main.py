## FUNCIONES

# Definición de una función
# Se deberá respetar la notación camelcase o usar guion bajo (_)
# Se debe respetar la indentación, pues de no respetarse no se estaría

# En python no podemos invocar a una funcion directamente, pues previamente deberemos de definir o importar una función
# miFuncion()
def miFuncion():
    print('Buenos días')


# Llamada a una funcion
miFuncion()


## Paso por parametros a una función
# Al ser Python un lenguaje de tipado debil, no es necesario indicar el tipo de valor que va a recibir la función
def paraFunction(nombre, apellidos):
    print(f'Hola mi nombre es {nombre} {apellidos}')


# Llamada a la función con parametros
paraFunction('Daniel Alfonso', 'Rodriguez Santos')


## Función return
# return nos permite devolver el resultado de una función, para poder operar con los resultados en otro apartado del código
def sumar(a, b):
    # Realizamos la operación de suma directamente en el return, devolviendo así el resultado
    return a + b


# Llamada a la función suma
resultado = sumar(4, 5)
print(f'El resultado de la suma es {resultado}')

# Esto también seria valido:
print(f'El resultado de la suma es {sumar(9, 12)}')


## Asignación de valores por defecto en los parametros de una función
# Se puede asignar un valor por defecto a un parametro, con esto no sería necesario inicializar un parametro
# IMPORTANTE: Podemos indicar el posible tipo de dato que puede devolver una función, aunque a veces sea redundante
# def sumDefault(a: int, b: int) -> int:
def sumDefault(a=0, b=0):
    return a + b


# Llamada a la función sin parametros (default)
resultado = sumDefault()
print(f'Resultado 2 params default: {resultado}')
# Llamada a la función con un parametro
resultado = sumDefault(2)
print(f'Resultado 1 params default: {resultado}')

# Llamada normal a la función
resultado = sumDefault(8, 6)
print(f'Resultado params normal: {resultado}')


## Argumentos variables en funciones
# Es posible que desconozcamos el número de argumentos totales que tiene una función
# A nivel interno, Python reconocerá esos argumentos variables como tuplas, por lo que no se podría modificar
def listaNombres(*nombres):  # en la documentación encontraremos como '*args'
    for nombre in nombres:
        print(nombre)


# Llamada a la función con argumentos variables
listaNombres('Daniel', 'José maría', 'Roberto Carlos', 'Pepe')
listaNombres('Francisco')


## Ejercicio Propuesto
# Se deberá crear una función que sume los valores númericos introducidos como argumentos.
# Se deberá devolver el resultado con la suma de todos los valores
def sumaVariable(*args):
    suma = 0
    for arg in args:
        suma += arg
    return suma


# Distintas invocaciones a la función propuesta
resultado = sumaVariable(2)
print(f'La suma de las operaciones es igual a {resultado}')

resultado = sumaVariable(2, 2, 8, 12)
print(f'La suma de las operaciones es igual a {resultado}')


## Ejercicio Propuesto
# Se deberá crear una función para multiplicar los valores intoducidos como argumentos
def multiplicaVariable(*args):
    multiplicacion = 1
    for arg in args:
        multiplicacion *= arg
    return multiplicacion


# Distintas invocaciones a la función propuesta
resultado = multiplicaVariable(3)
print(f'La multiplicación de los argumentos es igual a {resultado}')

resultado = multiplicaVariable(2, 2, 8, 12)
print(f'La multiplicación de los argumentos es igual a {resultado}')


## Argumentos variables de tipo clave - valor
# Se deberá añadir doble asteriscos en la funcion, siedo kwargs la palabra reservada
def listarDiccionarios(**kwargs):
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')


# Invocamos a la función, pasando por parametro la definición de un diccionario
listarDiccionarios(WK='WiKipedia', ORG='org', es='España')


## Distintos tipo de datos como argumentos
# Definimos una función que iterará lo que se le haya pasado como argumento
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

# En el caso de definir una lista, se mostrará su contenido
nombres = ['Carla', 'Alejandro']
desplegarNombres(nombres)

# En el caso de introducir una cadena, recorrerá la cadena carácter por caracter
desplegarNombres('Daniel')

# Si introducimos, por ejemplo un número, saldría error pues no se puede iterar
# desplegarNombres(15)

# Si queremos introducir valores númericos y que sean iterables, deberemos crear una lista o tupla
desplegarNombres((1, 2, 3))
desplegarNombres([1, 2, 3])


## Funciones Recursivas
# Esta funciones son aquellas que se mandan a llamar a si misma para realizar una tarea
# Un ejemplo típico de función recursiva sería la obtención del factorial de un número

# Definición de una función recursiva
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Invocación de la función recursiva
resultado = factorial(5)
print(f'El factorial de 5 es {resultado}')

## Ejercicio Propuesto
# Imprime números del x al 1 de forma descendente, usando una funcion recursiva

# Ejercicio hecho de forma rápida (Sin tener en cuenta los valores negativos e usando return)
# def descendNum(num):
#     if num >= 1:
#         print(num)
#         return
#     else:
#         print(num)
#         return descendNum(num - 1)
# descendNum(5)

# Ejercicio corregido (Teniendo en cuenta los valores negativos y simplificando el codigo)
def descendNum(num):
    if num >= 1:
        print(num)
        descendNum(num - 1)
    elif num == 0:
        return
    elif num <= 0:
        print('Valor negativo')
descendNum(30)

## Ejercicio Propuesto
# Crea una función que calcule el total de un pago incluyendo un impuesto aplicado
# La función tendrá que recoger dos argumentos: pago sin impuesto y el porcentaje del impuesto
def pagoImpuestos(pago, impuesto):
    return pago + pago * (impuesto/100)

# Inputs + Invocación a la función
pago = float(input('Introduce el pago sin impuestos: '))
impuesto = float(input('Introduce el porcentaje de impuesto a aplicar (x%): '))

resultado = pagoImpuestos(pago, impuesto)

# Mostramos el resultado
print(f'El pago total sería de {resultado} €')


## Ejercicio propuesto
# Crea dos funciones: una que convierta de grados celsius a fahrenheit y viceversa
def gradosCelsiusAFahrenheit(grados):
    return (grados * 9/5) + 32


def gradosFahrenheitACelsius(grados):
    return (grados - 32) * (5/9)


# Invocación de ambas funciones
celsius = gradosCelsiusAFahrenheit(35)
fahrenheit = gradosFahrenheitACelsius(109)

print(f'Celsius a Fahreint: {celsius}')
print(f'Fahrenheit a Celsius: {fahrenheit:.2f}')  # Con :.2f estamos formateando la salida de la variable

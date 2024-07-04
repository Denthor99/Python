## Listas
# Cada elemento de la lista cuenta con un indice. En esencia es un array

# Definición de una lista con elementos de tipo cadena
nombres = ['Alfonso', 'Daniel', 'Ricardo']

# Imprimimos la lista completa
print(nombres)

# Acceso a elementos de la lista en concreto
print(nombres[1])

# Acceso a los elementos de la lista de forma inversa
print(nombres[-2])

# Acceso a elementos de la lista según el rango. El valor del indice 2 no se muestra
print(nombres[0:2])

# Elementos desde el inicio de la lista hasta el indice indicado, sin incluirlo
print(nombres[:2])

# Desde el indice indicado hassta el final
print(nombres[1:])

# Cambiar el valor de un indice
nombres[2] = 'Ibai'
print(nombres)

# Iteración de la lista
for nombre in nombres:
    print(nombre)
else:
    print('Lista recorrida correctamente')

# Mostrar la cantidad de elementos de una lista
print(f'Nuestra lista contiene {len(nombres)} elementos')

# Añadir un nuevo elemento
nombres.append('Marta')
print(nombres)

# Añadir un elemento en un indice concreto, moviendo el contenido del arreglo a la derehca
nombres.insert(0,'Garry')
print(nombres)

# Borrar un elemento en concreto según su valor
nombres.remove('Garry')
print(nombres)

# Borrar el último valor agregado
nombres.pop()
print(nombres)

# Borrar un elemento según su indice
del nombres[2]
print(nombres)

# Borrar toda la lista
nombres.clear()
print(nombres)

# Borrar la lista por completo
# del nombres
# print(nombres)

## TUPLAS
# Las tuplas son de tipo inmutable, por lo que no se pueden modificar
# Si definieramos una tupla con un elemento, se deberá añadir al final una ','
# fruta = ('platano',)

# Definición de una tupla
frutas = ('Mandarina', 'Fresa', 'Manzana')
print(frutas)
# Cantidad de elementos de la tupla
print(len(frutas))

# Acceder a un elemento
print(frutas[1])

# Acceder a un elemento de forma inversa
print(frutas[-3])

# Acceder a un rango de valores
print(frutas[0:2])

# Mostrar el primer elemento de la tupla
print(frutas[:1])

# Recorrer una tupla. usamos "end" para modificar el muestreo de los elementos de la tupla
for fruta in frutas:
    print(fruta, end=' ')

# Conversion de tupla a lista
# No es una buena práctica, ya que es mejor tener claro desde un inicio si la colección va a ser inmutable o no
listaFrutas = list(frutas)

# Añadimos una fruta
listaFrutas.append('Kiwi')

# Realizamos de nuevo la conversión de la tupla
frutas = tuple(listaFrutas)
print(f'\n{frutas}')

## Ejercicio propuesto
# Dada la siguiente tupla, crea una lista que solo incluya los números menores a 5
tupla = (1, 3, 7, 9, 2, 4)
lista = []

for i in tupla:
    if i < 5:
        lista.append(i)
print(lista)

## SET
# Esta colección no mantiene ni orden ni permite elementos duplicados. Permite la inclusión y eliminación de elementos,
# pero no permite su modificación
# Definicion de set
planetas = {'Tierra', 'Jupiter', 'Urano', 'Marte'}
print(planetas)

# Largo de un set
print(len(planetas))

# Revisar si un elemento existe
print('Marte' in planetas)

# Agregar elemento a nuestro set
planetas.add('Saturno')
print(planetas)

# No soporta elementos duplicacdos
planetas.add('Tierra')
print(planetas)

# Eliminar un elemento, mostrando un error si no encuentra ese elemento
planetas.remove('Tierra')
print(planetas)

# Eliminar un elemento, sin mostrar un error si no encuentra ese elemento
planetas.discard('Tierra')
print(planetas)

## Diccionarios
# Colección de datos organizados en clave:valor
# Definición de un diccionario
diccionario = {
    '.WK':'WiKipedia',
    '.ORG':'org',
    '.es':'España'
}

# Imprimir diccionario
print(diccionario)

# Mostrar los elementos del diccionario
print(f'Los elementos del diccionario son {len(diccionario)}')

# Para acceder los elementos deberemos usar la llave(key)
print(diccionario['.es'])

# Podemos usar la función get para recuperar un elemento según su llave/key
print(diccionario.get('.WK'))

# Modificar un elemento del diccionario
diccionario['.ORG'] = 'Organismo Regional o del Gobierno'
print(diccionario)

# Recorrer los elementos de un diccionario, tanto sus llaves como valores
for termino, valor in diccionario.items():
    print(f'{termino} --> {valor}')

# Recuperar las claves del diccionario
for termino in diccionario.keys():
    print(termino, end=' ')

# Recuperar los valores del diccionario
for valores in diccionario.values():
    print(valores, end=' ')

# Comprobar si ya existe un elemento en el diccionario
print('\n')
print('.ORG' in diccionario)

# Agregar un nuevo elemento
diccionario['.uk'] = 'United Kingdom'
print(diccionario)

# Remover un elemento
diccionario.pop('.ORG')
print(diccionario)

# Limpiar el diccionario
diccionario.clear()
print(diccionario)

# Eliminar el diccionario
del diccionario
# print(diccionario)
## SENTENCIAS DE CONTROL

## IF/ELSE

# If simple
# condicion = False  # False
# condicion = 10  # True
# condicion = ''  # False
# if condicion:
#     print("Condición Verdadera")

# If/else
# if condicion:
#     print("Condición Verdadera")
# else:
#     print("Condición érronea")

# If/elif/else
# if condicion == True:
#     print("Condición Verdadera")
# elif condicion == False:
#     print("Condición Falsa")
# else:
#     print("No existe esa condición")

## Ejercicio propuesto
# Conversor de número a texto (5 valores)
numConver = input("Introduce un número del 1 al 5: ")

if numConver == '1':
    print("Número uno")
elif numConver == '2':
    print("Número dos")
elif numConver == '3':
    print("Número tres")
elif numConver == '4':
    print("Número cuatro")
elif numConver == '5':
    print("Número cinco")
else:
    print("Valor fuera de rango/no soportado")

# Operador ternario (Recomendable para códigos de pocas líneas)
# No se puede usar elif
newCondicion = False
print('Condición Verdadera') if newCondicion else print("Condición falsa")

## Ejercicio propuesto
# Según el mes introducido por consola, devuelve la estación
mes = int(input("Introduce un mes del año (1-12): "))
estacion = None

if mes == 12 or mes == 1 or mes == 2:
    estacion = "Invierno"
elif mes == 3 or mes == 4 or mes == 5:
    estacion = "Primavera"
elif mes == 6 or mes == 7 or mes == 8:
    estacion = "Verano"
elif mes == 9 or mes == 10 or mes == 11:
    estacion = "Otoño"
else:
    estacion = "No existe otra estación"

print(f'La estación del año correspondiente al mes {mes} sería {estacion}')

## Ejercicio propuesto
# Según la edad introducida, se indicará en que etapa de la vida se encuentra
edad = int(input("Intoduzca su edad: "))
etapa = None

# Asignar la etapa correspondiente a la variable 'etapa'
# Usaremos la sintaxis reducidad del operador 'and'
if 0 <= edad < 10:
    etapa = "La infancia"
elif 10 <= edad < 20:
    etapa = "La adolescencia"
elif 20 <= edad < 30:
    etapa = "La adultez"
else:
    etapa = "Etapa no válida, aún tienes camino por recorrer"

# Imprimir la etapa determinada
print(etapa)

## Ejercicio propuesto
# Según la nota de un alumno, se le asignará una calificación
nota = int(input("Nota del alumno (0-10): "))
califica = None

if 0 <= nota < 6:
    califica = 'F'
elif 6 <= nota < 7:
    califica = 'D'
elif 7 <= nota < 8:
    califica = 'C'
elif 8 <= nota < 9:
    califica = 'B'
elif 9 <= nota <= 10:
    califica = 'A'
else:
    califica = 'Valor no valido'

print(califica)

## BUCLES Y CICLOS

# While

# Bucle infinito
# condicion = True
# while condicion:
#     print(2)

# Bucle while. Se debe incrementar/decrementar el valor condicional para evitar bucles infinitos como el anterior
contador = 0
while contador < 3:
    print(contador)
    contador += 1
else:
    print('Fin ciclo')

## Ejercicio propuesto
# Muestra los números del 1 al 10
contador = 0
max = 10
while contador <= max:
    print(contador)
    contador += 1

## Ejercicio propuesto
# Muestra los números del 10 al 1
contador = 10
min = 1
while contador >= min:
    print(contador)
    contador -= 1

## BUCLE FOR
# Ideal para iterar cadenas y listas

# Iteracion de cadena. Una cadena/string no es más que un conjunto de caracteres
cadena = 'hola'
for c in cadena:
    print(c)
else:
    print('Cadena iterada correctamente')

## BUCLE FOR - BREAK
# En caso de encontrar el caracter 'ñ', sale del bucle
for letra in 'España':
    if letra == 'ñ':
        print(letra)
        break
else:
    print('No contiene la letra ñ')

## BUCLE FOR - CONTINUE
# Muestra los números que sean pares
# for i in range(6):
#     if i % 2 == 0:
#         print(f'valor: {i}')

# Usando continue saltamos el valor donde se cumpla x condición
for i in range (6):
    if i % 2 != 0:
        continue
    print(f'valor: {i}')

## Ejercicios propuestos
# Iterar un rango del 0 al 10, imprimiendo aquellos divisibles entre 3
for i in range(11):
    if i % 3 == 0:
        print(i)

# Iterar un rango del 2 al 6 e imprimelo
for i in range(2,7):
    print(i)

# Iterar un rango del 3 al 10, imprimiendo de dos en dos
for i in range(3,10,2):
    print(i)
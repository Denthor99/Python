# TIPOS DE DATOS
# Muchas veces trabajamos con múltiples variables, por lo que controlar el tipo de dato que almacena en su interior es
# fundamental para evitar posibles problemas en el código. Para comprobar el tipo de datos, usaremos la funcion type()
# Valor númerico
x = 10
# Valor de tipo string/cadena
y = "Barco"
print(type(x))
print(type(y))

# Podemos indicar el tipo de dato en la variable, pero el contenido de la variable es dinamico, es anotación más que nada
num: int = 15
fl: float = 8.9  # Valor decimal o float
car: str = False
print(type(car))

# Boolean
tr = True
notr = False

# MANEJO DE CADENAS
# Creamos una variable de tipo cadena
lenguajeFav = "PHP"

# Concatenamos la cadena anterior
lenguajeFav = lenguajeFav + ": el lenguaje para lado servidor"

# Concatenar cadena en la funcion print
print("Mi lenguaje favorito es " + lenguajeFav)

# Otra forma de concatenar con la función print
print("Mi lenguaje favorito es", lenguajeFav)

# Puede ocurrir que tengamos dos variables de tipo cadena con valor númerico
num1 = "5"
num2 = "3"

# Si realizamos una suma como tal, estaríamos concatenando, pues aunque sean valores númericos
print("Concatenación:", num1 + num2)

# Para sumar el contenido, tendriamos que convertirlo a un valor númerico ideal
print("Suma:", int(num1) + int(num2))

## TIPO BOOLEAN (bool)
miBool = True
print(miBool)

# Devolverá false o true, dependiendo del resultado
miBool = 1 < 2
print(miBool)

# Haremos otra comprobación
if miBool:
    print("Es verdadero")
else:
    print("Es falso")

# INPUT (entrada de usuario)
# Usaremos la función input() para procesar la entrada del usuario. Devuelve una cadena
# resultado = input("Introduce un valor:\n")
# print("Valor introducido:", resultado)
# print(type(resultado))

# Suma de dos números (INPUT)
# numero1 = int(input("Introduce un valor númerico: "))
# numero2 = int(input("Introduce otro valor númerico: "))
# resultado = numero1 + numero2
# print("La suma de los dos números introducidos es", resultado)

# Califica tu día (1 al 10)
# califcaDia = int(input("Del 1 al 10, ¿qué tal ha ido tu día? ^^: "))
# print("Mi día ha sido un", califcaDia)

# Titulo y autor de un libro
titulo = input("Proporciona el titulo del libro: ")
autor = input("Proporciona el autor del libro: ")
print(titulo, "fue escrito por", autor)
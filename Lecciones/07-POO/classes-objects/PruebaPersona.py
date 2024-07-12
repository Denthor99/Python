# Importamos la clase de Persona
from Persona import Persona


if __name__ == '__main__':
    print('Creación de una persona'.center(30, '*'))
    persona1 = Persona('Jose', 26, 'Marquesero')
    persona1.mostrarDetalles()

    print('Eliminar objeto'.center(30, '-'))
    del persona1

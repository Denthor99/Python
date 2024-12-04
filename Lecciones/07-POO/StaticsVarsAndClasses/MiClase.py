class MiClase:
    # Esta variable es una variable de clase, es decir, una variable que heredarán todas las instancias
    variableClase = "variable clase"

    # Definimos un atributo, que será la variable de instancia
    def __init__(self, variableInstancia):
        self.varInstancia = variableInstancia

    # Definición de un método estatico
    @staticmethod
    def metodoStatico(): # 'self' no se puede utilizar, pues es una variable de instancia y no una variable de clase
        print(f'Método de clase u estatico, y solo puede usar la variable de clase: {MiClase.variableClase}')

    # Definición de un método de clase. Este metodo puede recibir contexto de la clase, es decir atributos, etc
    @classmethod
    def metodoClase(cls):
        print(f'{cls.variableClase}')

    # Definición de un método de instancia
    def metodoInstancia(self):
        print('Método de instancia')

# Realizamos la prueba
objeto1 = MiClase("Valor de instancia")

# Valor de la instancia
print(objeto1.varInstancia)
# Valor de clase
print(objeto1.variableClase)

# Si desearamos añadir una nueva variable de clase, la podemos crear en cualquier momento
MiClase.variableClase2 = 'Otra variable de clase'

# Invocación de un método estatico
MiClase.metodoStatico()

# Invocación de un método de clase
objeto1.metodoClase()

# Invocación de un método de instancia
objeto1.metodoInstancia()


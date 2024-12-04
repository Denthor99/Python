class Producto:
    contador_productos = 0

    @classmethod
    def contadorNew(cls):
        cls.contador_productos += 1
        return cls.contador_productos
    def __init__(self, nombre, precio):
        self._idProducto = Producto.contadorNew()
        self._nombre = nombre
        self._precio = precio

    @property
    def idProducto(self):
        return self._idProducto
    @idProducto.setter
    def idProducto(self, id):
        self._idProducto = id
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio
    def __str__(self):
        return f'Producto[id: {self.idProducto}, Nombre:{self.nombre}, Precio:{self.precio}]'

if __name__ == '__main__':
    producto1 = Producto('Meta Quest 3', 580)
    print(producto1)
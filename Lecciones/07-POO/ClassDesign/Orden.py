from Producto import Producto
class Orden:
    contador_ordenes = 0

    @classmethod
    def contadorOrden(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes
    def __init__(self, productos):
        self._idOrden = Orden.contadorOrden()
        self._productos = list(productos)

    def agregarProducto(self, producto):
        self._productos.append(producto)

    def calculoTotal(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + ' | '

        return f'Orden: {self._idOrden},\nProductos: {productos_str}'

if __name__ == '__main__':
    producto1 = Producto('Meta Quest 3', 580)
    producto2 = Producto('Meta Quest 2', 180)
    producto3 = Producto('Oculus Quest', 120)
    producto4 = Producto('Valve Index', 820)


    productos1 = [producto1, producto2]
    productos2 = [producto3, producto4]

    orden1 = Orden(productos1)
    print(orden1)
    print(f'Total orden 1: {orden1.calculoTotal()}€')

    orden2 = Orden(productos2)
    print(orden2)
    print(f'Total orden 2: {orden2.calculoTotal()}€')
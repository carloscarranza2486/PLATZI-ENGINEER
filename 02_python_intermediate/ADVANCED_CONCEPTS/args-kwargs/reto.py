class Products():
    def __init__(self, name, *args, **kwargs):
        self.name = name 
        self.precio = args[0] if args else 0
        self.descuento = kwargs.get('descuento', 0)

    def recibir_producto(self):
        print(f'Producto {self.name} recibido')
        print(f'Precio del producto {self.name}: $ {self.precio}')
        print(f'Descuento aplicado: {self.descuento}%')

producto1 = Products('Jabón', 50000, descuento=10)

producto1.recibir_producto()
class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        self.__veces_prestado = 0

    def prestar(self):
        if self.disponible:
            self.disponible = False
            self.__veces_prestado = +1
            return f"{self.titulo}: prestado exitosamente. Total préstamos: {self.__veces_prestado}"
        return f"'{self.titulo}' no está disponible"

    def devolver(self):
        self.disponible = True
        return f"{self.titulo}: ha sido devuelto y disponible nuevamente."

    def es_popular(self):
        return self.__veces_prestado > 5

    def get_veces_prestado(self):
        return self.__veces_prestado

    def set_veces_prestado(self, veces_prestadas):
        self.__veces_prestado = veces_prestadas


mi_libro = Libro("100 años de soledad",
                 "Gabriel García Marquez", "9781644734728", True)
otro_libro = Libro("El Principito", "Saint-Exupéry", "9781644731234728", True)

mi_libro.set_veces_prestado(10)
print(mi_libro.get_veces_prestado())


catalogo = [mi_libro, otro_libro]

for libro in catalogo:
    print(libro)

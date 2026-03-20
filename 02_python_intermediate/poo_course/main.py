class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self_titulo = titulo
        self_autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def __str__(self):
        return f"{self.titulo} por {self.autor} disponible: {self.disponible}"

    def prestar(self):
        if self.disponible:
            self.disponible = False
        return f"'{self.titulo}' prestado exitosamente"


mi_libro = Libro("100 años de soledad", "Gabriel García Marquez")
otro_libro = Libro("El principito", "Saint-exupéry")

print(mi_libro.prestar())
print(mi_libro.devolver())

catalogo = [mi_libro, otro_libro]

for libro in catalogo:
    print(libro)

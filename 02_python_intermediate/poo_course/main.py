# Lista global o compartida que registre cada préstamo
historial_prestamos = []


class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            historial_prestamos.append(self)
            return f"{self.titulo}: prestado exitosamente."

    def devolver(self):
        self.disponible = True
        return f"{self.titulo}: ha sido devuelto y disponible nuevamente."

    def es_popular(self):
        return historial_prestamos.count(self) > 5


# Ejemplo de uso
libro1 = Libro("Cien años de soledad",
               "Gabriel García Márquez", "978-0-06-088328-7")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry",
               "978-0-15-601219-5")

catalogo = [libro1, libro2]
for libro in catalogo:
    # Se mejorará con __str__ más adelante
    print(libro.titulo, libro.autor, libro.isbn, libro.disponible)

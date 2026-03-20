class Libro:
    def __init__(self, titulo, autor):
        self_titulo = titulo
        self_autor = autor


mi_libro = Libro("100 años de soledad", "Gabriel García Marquez")
otro_libro = Libro("El principito", "Saint-exupéry")

print(f"mi_libro: {mi_libro.titulo} {mi_libro.autor}")
print(f"otro_libro: {otro_libro.titulo} {otro_libro.autor}")

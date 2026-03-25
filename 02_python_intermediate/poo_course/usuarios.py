class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados = []

    def solicitar_libro(self, titulo):
        return f"La solicitud de libro {titulo} relizada"


class Estudiante(Usuario):
    def __init__(self, nombre, cedula, carrera):
        super().__init__(nombre, cedula)
        self.carrera = carrera
        self.limite_libros = 3

    def solicitar_libro(self, titulo):
        if len(self.libros_prestados) < self.limite_libros:
            self.libros_prestados.append(titulo)
            return f"Préstamo del libro {titulo} autotizado"
        else:
            return f"No puedes prestar más libros, límite alcanzado {self.limite_libros}"

    def devolver_libro(self, titulo):
        for titulo in self.libros_prestados:
            self.libros_prestados.remove(titulo)
            return f"El libro {titulo} se ha devuelto a la biblioteca"


class Profesor(Usuario):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)
        self.limite_libros = None

    def solicitar_libro(self, titulo):
        self.libros_prestados.append(titulo)
        return f"Préstamo del libro {titulo} autotizado"


estudiante = Estudiante("Carlos", "123456789", "Sistemas")
profesor = Profesor("Felipe", "123123123")

print(profesor.solicitar_libro("Python Básico"))
print(profesor.solicitar_libro("Python intermedio"))
print(profesor.solicitar_libro("Python avanzado"))
print(profesor.solicitar_libro("Python / Django"))

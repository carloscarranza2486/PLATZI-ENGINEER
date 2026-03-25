from typing import Protocol

from main import Libro


class SolicitarProtocol(Protocol):
    def solicitar_libro(self, titulo: str) -> str:
        """Método que debe implementar cualquier solicitante"""
        ...


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
estudiante_1 = Estudiante("Jose", "56789123", "Salud")
profesor = Profesor("Felipe", "123123123")

libro = Libro("Titulo de prueba", "Autor de prueba", isbn="123123")

usuarios: list[SolicitarProtocol] = [estudiante, estudiante_1, profesor, libro]

for usuario in usuarios:
    print(usuario.solicitar_libro("Titulo de ejemplo"))

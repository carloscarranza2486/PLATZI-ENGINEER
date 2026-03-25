from biblioteca import Biblioteca
from exceptions import BibliotecaError, LibroNoDisponibleError, UsuarioNoEncontradoError
from libros import Libro, LibroFisico
from usuarios import Estudiante, Profesor, SolicitarProtocol
from exceptions import BibliotecaError

biblioteca = Biblioteca("Platzi Biblioteca")

estudiante = Estudiante("Carlos", "123456789", "Sistemas")
estudiante_1 = Estudiante("Jose", "56789123", "Salud")
profesor = Profesor("Felipe", "123123123")


mi_libro = LibroFisico("100 Años de Soledad", "Gabriel Garcia Marquez", "9781644734728")
otro_libro = LibroFisico("El Principito", "Saint-Exupéry", "9781644731234728")

biblioteca.usuarios = [estudiante, estudiante_1, profesor]
biblioteca.libros = [mi_libro, otro_libro]


print("Bienvenido a Platzi Biblioteca")

print("Libros disponibles: ")
for titulo in biblioteca.libros_disponibles():
    print(f"  - {titulo}")
print()

cedula = input("Digite el número de cédula: ")
try:
    usuario = biblioteca.buscar_usuario(cedula)
    print(usuario.cedula, usuario.nombre)
except UsuarioNoEncontradoError:
    print("El usuario que estás buscando no existe")

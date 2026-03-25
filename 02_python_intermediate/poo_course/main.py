from os import EX_CANTCREAT
from biblioteca import Biblioteca
from data import data_estudiantes, data_libros, libro1
from exceptions import UsuarioNoEncontradoError, LibroNoDisponibleError
from usuarios import Profesor

biblioteca = Biblioteca("Platzi Biblioteca")
profesor = Profesor("Felipe", "123123123")

biblioteca.usuarios = [profesor] + data_estudiantes
biblioteca.libros = data_libros


print("Bienvenido a Platzi Biblioteca")

print("Libros disponibles: ")
for titulo in biblioteca.libros_disponibles():
    print(f"  - {titulo}")
print()

cedula = input("Digite el número de cédula: ")
try:
    usuario = biblioteca.buscar_usuario(cedula)
    print(usuario.cedula, usuario.nombre)
except UsuarioNoEncontradoError as e:
    print(e)

titulo = input("Digite el título del libro: ")
try:
    libro = biblioteca.buscar_libro(titulo)
    print(f"El libro que seleccionaste es: {libro}")
except LibroNoDisponibleError as e:
    print(e)

resultado = usuario.solicitar_libro(libro.titulo)
print(f"\n{resultado}")

try:
    resultado_prestar = libro.prestar()
    print(f"\n{resultado_prestar}")
except LibroNoDisponibleError as e:
    print(e)

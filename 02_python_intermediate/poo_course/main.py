from biblioteca import Biblioteca
from data import data_estudiantes, data_libros
from exceptions import LibroNoDisponibleError, UsuarioNoEncontradoError
from libros import Libro
from usuarios import Profesor


biblioteca = Biblioteca("Platzi Biblioteca")
profesor = Profesor("Felipe", "123123123")


biblioteca.usuarios = [profesor] + data_estudiantes
biblioteca.libros = data_libros

# Ejemplo setter
# libro_de_prueba = data_libros[0]
# libro_de_prueba.veces_prestado = -1

# result = Biblioteca.validar_isbn("2345678900")
# print(f"El isbn es válido: {result}")
libro_no_disponible = Libro.crear_no_disponible(
    "Libro de prueba", "Autor de prueba", "1234567890"
)

print("libro disponible?:", libro_no_disponible.disponible)

print("Bienvenido a Platzi Biblioteca")

print("Libros disponibles:")
for libro in biblioteca.libros_disponibles:
    print(f"  - {libro.descripcion_completa}")
print()

cedula = input("Digite el numero cedula: ")
try:
    usuario = biblioteca.buscar_usuario(cedula)
    print(usuario.nombre_completo, usuario.nombre_completo)
except UsuarioNoEncontradoError as e:
    print(e)

titulo = input("Digite el titulo del libro: ")
try:
    libro = biblioteca.buscar_libro(titulo)
    print(f"El libro que selecionaste es: {libro}")
except LibroNoDisponibleError as e:
    print(e)

resultado = usuario.solicitar_libro(libro.titulo)
print(f"\n{resultado}")

try:
    resultado_prestar = libro.prestar()
    print(f"\n{resultado_prestar}")
except LibroNoDisponibleError as e:
    print(e)

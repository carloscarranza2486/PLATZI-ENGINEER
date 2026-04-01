from exceptions import LibroNoDisponibleError, UsuarioNoEncontradoError
from usuarios import Estudiante
from persistencia import Persistencia


persistencia = Persistencia()
biblioteca = persistencia.cargar_datos()

print("Bienvenido a Platzi Biblioteca")

print("Libros disponibles:")
for libro in biblioteca.libros_disponibles:
    print(f"  - {libro.descripcion_completa}")
print()

cedula = input("Digite el numero cedula: ")
try:
    usuario = biblioteca.buscar_usuario(cedula)
    print(usuario.nombre_completo, usuario.cedula)
except UsuarioNoEncontradoError as e:
    print(e)
    exit()

titulo = input("Digite el titulo del libro: ")
try:
    libro = biblioteca.buscar_libro(titulo)
    print(f"El libro que selecionaste es: {libro}")
except LibroNoDisponibleError as e:
    print(e)
    exit()

resultado = usuario.solicitar_libro(libro.titulo)
print(f"\n{resultado}")

try:
    resultado_prestar = libro.prestar()
    print(f"\n{resultado_prestar}")
except LibroNoDisponibleError as e:
    print(e)

usuario1 = Estudiante.crear_estudiante_ingenieria("Carlos", "1234567890")
print(f"Mi estudiante estudia: {usuario1.carrera}")

persistencia.guardar_datos(biblioteca)

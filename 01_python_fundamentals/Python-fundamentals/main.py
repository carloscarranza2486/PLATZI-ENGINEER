print('Hola Platzi live desde un archivo')


edad = 25


def bienvenida(nombre, edad):
    """Función para dar la bienvenida, valida si la edad es mayor a 18
    
    nombre: Nombre de la persona
    edad: Edad de la persona
    """
    if edad >= 18:
        print(f'Bienvenido {nombre} a la FIESTA!')
    elif edad >= 13:
        print(f'bienvenida {nombre} a la zona sin licor!')
    else:
        print("Menor de edad - Acceso denegado")


bienvenida('Carlos Carranza', 18)
bienvenida('Ana Buitrago', 15)
bienvenida('Maria Camila González', 12)

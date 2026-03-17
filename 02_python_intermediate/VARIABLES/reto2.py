# "Base de Datos"
empleados = [
    {'nombre': 'Carlos', 'edad': 32, 'sueldo': 5000},
    {'nombre': 'Ana', 'edad': 28, 'sueldo': 3000},
    {'nombre': 'Pedro', 'edad': 45, 'sueldo': 1500},
    {'nombre': 'Luisa', 'edad': 35, 'sueldo': 6000},
    {'nombre': 'Jorge', 'edad': 22, 'sueldo': 2000}
]


def mostrar_todos(nombre: str, edad: int, sueldo: float):
    print("--- Lista completa ---")
    for empleado in empleados:
        print(f'{empleado['nombre']} gana ${empleado['sueldo']}')

def filtro_empleados(lista_empleados, sueldo_minimo):
    empleados_vip =[]
    for empleado in empleados:
        if empleado > sueldo_minimo:
            empleados_vip.append(empleado)
    return empleados_vip


mostrar_todos(empleados)

ricos = filtro_empleados(empleados, 3500)

print("n\--- EMPLEADOS CON SUELDO ALTO (> 3500) ---")
mostrar_todos(ricos)
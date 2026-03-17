def check_access(func):
    def wrapper(employee):
        # Comprobar si el empleado tiene rol 'admin'
        if employee.get('rol') == 'admin':
            return func(employee)
        else:
            print('ACCESO DENEGADO: Solo los administradores pueden acceder')
    return wrapper

@check_access
def delete_employees(employee):
    print(f'El empleado {employee['name']} ha sido eliminado')

admin = {'name': 'Carlos', 'rol': 'admin'}
employee = {'name': 'Ana', 'rol': 'empleada'}

#delete_employees(admin)
delete_employees(employee)

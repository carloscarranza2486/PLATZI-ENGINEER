"""
Implementar un nuevo decorador que registre cualquier acción realizada por un empleado enn un
nuevo archivo de texto
Aumentar decoradores para poder reutilizarlos
"""
# the function will check if the format is in PDF
def log_action(func):
    def wrapper(file):
        with open('employee_actions.txt', 'a') as f:
            nombre = file['name']
            formato = file['format']
            f.write(f'Intento de subir archivo: {nombre} con formato {formato}\n')
        return func(file)
    return wrapper

def check_format(func):
    def wrapper(file):
        if file.get('format') == 'PDF':
            return func(file)
        else:
            print('Formato incorrecto, solo se permite PDF')
    return wrapper

@log_action
@check_format
def upload_files(file):
    print(f'The file {file['name']} has been uploaded')


file1 = {'name': 'reporte_final', 'format': 'PDF'}
file2 = {'name': 'base_de_datos', 'format': 'csv'}

print('---Intento 1 ---')
upload_files(file1)
print('---Intento 2 ---')
upload_files(file2)
# IDs de empleados
id1: int = 101
id2: int = 102

# Sumar los IDs

total_id: int = id1 + id2

# Mostrar resultado

print(f"La suma de los IDs es: {total_id}")

# uso de funciones
def add_employee_ids(id1: int, id2: int) -> int:
    return id1 + id2

print(add_employee_ids(201,202))

# Uso de clases

class Employee:
    name: str
    edad: int
    salary: float

    def __init__(self, name: str, edad: int, salary: float):
        self.name = name
        self.edad = edad
        self.salary = salary

    def introduce(self) -> str:
        return f"Hola, me llamo {self.name}, tengo {self.edad}"
    

employee1 = Employee("Carlos", 32, 3500.0)
print(employee1.introduce())

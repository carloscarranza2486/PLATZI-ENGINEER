"""
Code that filters employee names based on salary greater than 50000.
"""

employees_filtered = []


def get_employee(name, salary):
    for employee in employees:
        if employee["salary"] > 50000:
            employees_filtered.append(employee)
    return employees_filtered


employees = [
    {"name": "John", "salary": 60000},
    {"name": "Jane", "salary": 45000},
    {"name": "Doe", "salary": 70000},
    {"name": "Alice", "salary": 30000},
]

resultado = get_employee(employees, 50000)
print(resultado)

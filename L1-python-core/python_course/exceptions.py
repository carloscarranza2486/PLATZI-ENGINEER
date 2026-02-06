try:
    divisor = int(input("Ingresa el número divisor: "))
    result = 100 / divisor
    print(result)
except ZeroDivisionError as e:
    print("Error: El divisor no puede ser cero", e)
except ValueError as e:
    print("Error: Por favor ingresa un número válido", e)


def print_exception_hierarchy(exception_class, indent=0):
    print(" " * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)


print_exception_hierarchy(Exception)

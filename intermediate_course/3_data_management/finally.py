a = 0
b = 0

try:
    a = int(input("Digita un número: "))
    b = int(input("Digita otro número: "))
    resultado = a / b
    print(f"Resultado: {resultado}")
except ValueError:
    print("El valor digitado no es un número válido")
except ZeroDivisionError:
    print("No está permitido dividir por 0")
finally:
    print("Print desde finally")


print("Este es otro print")

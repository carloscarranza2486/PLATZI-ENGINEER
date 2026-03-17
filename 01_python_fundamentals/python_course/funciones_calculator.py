def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiplay(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculator():
    while True:
        print("Seleccione una operación")
        print("1. sumar")
        print("2. restar")
        print("3. multiplicar")
        print("4. dividir")
        print("5. salir")

        option = input("Ingrese su opción (1, 2, 3, 4, 5): ")

        if option == "5":
            print("Saliendo de la calculadora")
            break
        if option in ["1", "2", "3", "4"]:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            if option == "1":
                print("La suma es:", add(num1, num2))
            elif option == "2":
                print("la resta es:", substract(num1, num2))
            elif option == "3":
                print("la multiplicación es:", multiplay(num1, num2))
            elif option == "4":
                print("la división es:", divide(num1, num2))
        else:
            print("Opción no válida, por favor intenta de nuevo")


calculator()

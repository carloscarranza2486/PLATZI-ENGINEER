x = 100  # Variable de tipo global


def local_function():
    x = 10  # variable local
    print(f"Valor de x dentro de la función: {x}")


def show_global():
    print(f"El valor de la variable global es {x}")


# local_function()
print(x)

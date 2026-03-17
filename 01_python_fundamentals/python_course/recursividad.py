def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


factorial_5 = print(factorial(5))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number = 3
# print(fibonacci(number))


# ejercicio 1: Función para calcilar la sumatoria de números naturales
def sumatoria(n):
    if n == 0:
        return 0
    else:
        return n + sumatoria(n - 1)


print(sumatoria(5))

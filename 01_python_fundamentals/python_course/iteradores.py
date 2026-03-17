# ejemplo de iterador

# Se crea una lista

my_list = [1, 2, 3, 4]

# Se obtiene el iterador

my_iter = iter(my_list)


# usar el iterador
# next nos ayuda a ver los valores que se almacenan en la memoria
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


# Ejercicio 2: Iterar en cadenas

# creando la cadena
text = "Hola Mundo"
# Creando el iterador
iter_text = iter(text)
# iterar en la cadena
for char in iter_text:
    print(char)

# Ejercicio 3: Crear un iterador para númneros impares

# límite

limit = 10

odd_iter = iter(range(1, limit + 1, 2))

# usar el iterador

for num in odd_iter:
    print(num)

"""personal exercise

start separator separator

--------------------------------------------------------------------------------------------------
"""

fruits = ["manzana", "banana", "cereza"]

iter_fruits = iter(fruits)
for fruit in fruits:
    print(fruit)

""" end separator

--------------------------------------------------------------------------------------------------
"""
# Generadores: Una función que produce secuencia de números en los que podemos iterar


def my_generator():
    yield 1
    yield 2
    yield 3


for value in my_generator():
    print(value)

# Ejercicio 4: Fibonnacci
# 0 1 1 2 3 5 8 13 21 34 55 ...


def fibonnacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


for num in fibonnacci(10):
    print(num)

# Generador de números pares


def even_numbers(limit):
    num = 0
    while num < limit:
        yield num
        num += 2


for even in even_numbers(20):
    print(even)

# Generador de números pares


def odd_numbers(limit):
    num = 1
    while num < limit:
        yield num
        num += 2


for odd_number in odd_numbers(20):
    print(odd_number)

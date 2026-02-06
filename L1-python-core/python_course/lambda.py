# con lambda podemos crear funciones anónimas, es decir, sin nombre, que pueden ser utilizadas en el momento.
# Son útiles para operaciones simples y se pueden usar con funciones como map(), filter() y reduce().

add = lambda a, b: a + b
# print(add(10, 4))

multiply = lambda a, b: a * b
# print(multiply(80, 5))

# Obtener el cuadrado de un número
numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers))
# print("Cuadrados:", squared_numbers)


materials = [0.8, 3.5, 1.2, 4.0, 0.5, 2.1, 0.9, 3.0]
# Clasificar los materiales usando lambda
materiales_clasificados = list(map(lambda x: x**2, materials))
print("Materiales al cuadrado:", materiales_clasificados)


# pares
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Pares:", even_numbers)

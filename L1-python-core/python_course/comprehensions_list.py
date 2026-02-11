# squares = [x**2 for x in range(1, 11)]
# # print("Cuadrados:", squares)


# celsius = [0, 10, 20, 30, 40]
# farenheit = [(temp * 9 / 5) + 32 for temp in celsius]
# # print("Temperatura en grados Farenheit:", farenheit)

# # Hallar números pares

# evens = [x for x in range(1, 21) if x % 2 == 0]
# # print("Números pares:", evens)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# # print(matrix)
# # print(transposed)

# Sin comprensión de listas
# transposed = []
# for i in range(len(matrix[0])):
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)

# # print(transposed)

# # doble de los números

# numbers = [1, 2, 3, 4, 5]
# doubled = [x * 2 for x in numbers if x < 10]
# print(doubled)

# # Filtrar y transformar en un solo paso

# words = ["sol", "mar", "montaña", "rio", "estrella"]
# longest_words = [word.upper() for word in words if len(word) > 3]
# print(longest_words)

# # Crear un Diccionario con List Comprehension

# key = ["nombre", "edad", "ocupación"]
# value = ["Juan", 30, "Ingeniero"]
# dic = {key[i]: value[i] for i in range(len(key))}
# print(dic)

# # Anidación de List Comprehensions
# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# lista_transpuesta = [row[i] for i in range(len(matriz[0])) for row in matriz]
# print(lista_transpuesta)

# No pitónico

transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)


# Pytonico

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)

# # Leer un archivo línea por línea
# with open("caperucita.txt", "r") as file:
#     for lineas in file:
#         print(lineas.strip())

# # Leer todas las líneas en una lista
# with open("caperucita.txt", "r") as file:
#     lines = file.readlines()
#     print(lines)

# # Añadir texto
# with open("caperucita.txt", "a") as file:
#     file.write("\n\nBy:ChatGPT")

# # Sobreescribir el texto
# with open("caperucita.txt", "w") as file:
#     file.write("\n\nBy:ChatGPT")


# Leer todas las líneas en una lista
with open("caperucita.txt", "r") as file:
    cont = 0
    for lineas in file:
        cont += 1
        print(f"{cont}: {lineas.strip()}")

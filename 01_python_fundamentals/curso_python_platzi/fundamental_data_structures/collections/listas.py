# listas: las listas son ordenadas, modificables y permiten valores duplicados

# Indices_    0         1          2           3
# frutas = ["Manzana", "Naranja", "Mandarina","Naranja"]
# print(frutas)
# print(type(frutas))

# frutas[1] = "Banana"

# print(frutas[1])
# print(frutas)

# lista = ["Carlos Carranza", 5, True]
# print(lista)
# print(type(lista))

# print(len(lista))
# print(len(frutas))

# print(frutas[1:])

# if "Manzana" in frutas:
#     print("La manzana está dentro de frutas")

#Methods
# Append "Agregar un elemento al final de la lista"

# Index.      0.      1.     2

vehiculos =["Auto", "Moto","Avión"]
vehiculos.append("Barco")
print(vehiculos)

# Insert

vehiculos.insert(1,"Bicicleta")
print(vehiculos)

# remove

vehiculos.remove("Auto")
print(vehiculos)

# pop
vehiculos.pop(1)
print(vehiculos)

#sort
vehiculos.sort()
print(vehiculos)

# Reverse
vehiculos.reverse()
print(vehiculos)

# Unir listas
colection1 = [1,2,3]
colection2 = [4,5,6]


colection3 = colection1 + colection2
print(colection3) 

colection1.extend(colection2)
print(colection1)
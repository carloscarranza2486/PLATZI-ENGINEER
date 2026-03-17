# Tuplas: Colección ordenada e inmutable de elementos que permiten duplicados

# index           0.        1.         2.    3
tecnologías = ("Python", "Javascript","Go","Python")
print(tecnologías)
print(tecnologías[1])


print(len(tecnologías))

print(type(tecnologías))

fruta =("Manzana",)
print(type(fruta))


tupla = ("Python", 5, True)

print(tupla)
print(type(tupla))

x, y, z = (tupla)
print(x)
print(y)
print(z)

Tuple1 = (1,2,3)
Tuple2 = (3,4,5)
Tuple3 = Tuple1 + Tuple2

print(Tuple3)

tupla = ("Python", 5, True)

print(tupla * 2)

for item in tupla:
    print(item)

print("---------------")

tuplaAModificar = ("Python","Javascript","Go")
listaComodin = list(tuplaAModificar)
print(listaComodin)
listaComodin.append("ReactJS")
tuplaAModificar = tuple(listaComodin)
print(tuplaAModificar)
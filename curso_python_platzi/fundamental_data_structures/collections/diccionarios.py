# Colección de pares clave-valor (ordenado a partir de Python 3.7)

auto = {
    "marca": "Renault",
    "modelo": "clio",
    "año": 2025
}

print(auto)
print(auto["marca"])
print(auto.get("marca"))

print(auto.keys())
print(auto.values())

if "marca" in auto:
    print("Marca es una de las propiedades de este diccionario")
    
auto["año"] = 2020
print(auto)

auto["color"] = "verde"
print(auto)

auto.update({"año": 2022,"puertas": 4})
print(auto)

# auto.pop("puertas")
# print(auto)

# auto.popitem()
# print(auto)

# auto.clear()
# print(auto)

for k in auto: # Keys: claves
    print(k)
for v in auto.values(): # Values
    print(v)


# diccionarios anidados

familia = {
    "Hijo1" : {
        "nombre": "Pedro",
        "edad": 8
    },
    "Hijo2" : {
        "nombre": "Ana",
        "edad": 7
    },
    "Hijo3" : {
        "nombre": "Marcelo",
        "edad": 6
    }
}

print(familia["Hijo1"]["nombre"])
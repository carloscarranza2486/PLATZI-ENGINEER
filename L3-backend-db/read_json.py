import json

# lectura del archivo
with open("products.json", "r") as file:
    products = json.load(file)

# Mostrar el contenido

for product in products:
    # print(product)
    print(f"Product: {product['name']}, Price: {product['price']}")

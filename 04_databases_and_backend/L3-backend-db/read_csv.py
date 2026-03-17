import csv

# # leer un archivo
# with open("products_updated.csv", "r") as file:
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         print(row)

# Mostrar la información por columnas

# with open("products_updated.csv", mode="r") as file:
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         print(f"El producto {row['name']}, Precio: {row['price']}")

new_product = {
    "name": "Wireless charger",
    "price": "75",
    "quantity": 100,
    "brand": "ChargerMaster",
    "category": "Accessories",
    "entry_date": "2024-07-01",
}

with open("products_updated.csv", mode="a", newline="") as file:
    file.write("\n")
    csv_writer = csv.DictWriter(file, fieldnames=new_product.keys())
    csv_writer.writerow(new_product)

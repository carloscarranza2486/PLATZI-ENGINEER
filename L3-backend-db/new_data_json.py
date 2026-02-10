# import json

# file_path = "products.json"

# new_product = {
#     "name": "Wireless charger",
#     "price": "75",
#     "quantity": 100,
#     "brand": "ChargerMaster",
#     "category": "Accessories",
#     "entry_date": "2024-07-01",
# }

# with open(file_path, mode="r") as file:
#     products = json.load(file)

# products.append(new_product)

# with open(file_path, mode="w") as file:
#     json.dump(products, file, indent=4)


# convertir archivo csv en json

import csv
import json

with open("products.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    lista = list(csv_reader)

    with open("products_from_csv.json", mode="w") as json_file:
        json.dump(lista, json_file, indent=4)

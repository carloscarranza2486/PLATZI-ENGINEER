import random

# Generar un número entero aleatorio

random_number = random.randint(1, 100)
print(f"Número aleatorio generado: {random_number}")

# elegir colores aleatorios

colors = ["rojo", "verde", "azul", "amarillo", "naranja"]
random_color = random.choice(colors)
print(random_color)


# Barajar una lista de cartas

cards = ["As de corazones", "Rey de diamantes", "Reina de tréboles", "Jota de picas"]
random.shuffle(cards)
print(cards)

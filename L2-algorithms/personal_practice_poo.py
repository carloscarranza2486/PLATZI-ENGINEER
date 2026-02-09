"""
Este código busca poner en práctica los conceptos de POO para mi proyecto de upholstery AI

"""


# 1. Definimos la CLASE (El Molde)
class Mueble:
    # El CONSTRUCTOR (__init__): Es lo primero que pasa cuando fabricas el mueble.
    # Aquí definimos sus características básicas (Atributos).
    def __init__(self, nombre, tela, metros_tela):
        self.nombre = nombre  # Ej: "Sofá L"
        self.tela = tela  # Ej: "Lino"
        self.metros = metros_tela  # Ej: 15

    # Definimos un MÉTODO (Una acción que este mueble sabe hacer)
    def cotizar_trabajo(self, precio_metro):
        costo_total = self.metros * precio_metro
        return f"Retapizar el {self.nombre} con {self.tela} cuesta ${costo_total}"


# --- FIN DEL MOLDE ---

# 2. Ahora usemos el molde para crear OBJETOS reales (Instancias)

# Creamos el mueble de la Sala
mueble_sala = Mueble("Sofá Modular", "Terciopelo", 12)

# Creamos el mueble de la Oficina (usamos el MISMO molde, pero datos distintos)
mueble_oficina = Mueble("Silla Ejecutiva", "Cuero", 3)

# 3. Usamos sus métodos (Acciones)
print(mueble_sala.cotizar_trabajo(50))  # Precio del metro: 50
print(mueble_oficina.cotizar_trabajo(80))  # Precio del metro: 80

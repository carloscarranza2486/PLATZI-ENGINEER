import random


class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = 0
        self.hits = 0

    def place_ship(self, start_row, start_col, direction):
        if direction == "h":
            self.positions = [(start_row, start_col + i) for i in range(self.size)]
        else:
            self.positions = [(start_row + i, start_col) for i in range(self.size)]

    def hit(self):
        self.hits += 1
        return self.hits == self.size


class Destroyer(Ship):
    def __init__(self):
        super().__init__("Destroyer", 2)


class Submarine(Ship):
    def __init__(self):
        super().__init__("Submarine", 3)


class Battleship(Ship):
    def __init__(self):
        super().__init__("Battleship", 4)


class Player:
    def __init__(self, name):
        self.name = name
        self.board = [[" " for _ in range(10)] for _ in range(10)]
        self.ships = []
        self.hits = [[" " for _ in range(10)] for _ in range(10)]

    def add_ship(self, ship, row, col, direction):
        # 1. Calculamos posiciones teóricas
        ship.place_ship(row, col, direction)

        # --- VALIDACIÓN ---
        for r, c in ship.positions:
            # Chequeo 1: ¿Se sale del mapa?
            if not (0 <= r < 10 and 0 <= c < 10):
                print(f"❌ Error: El barco se sale del mapa.")
                return False  # ¡Falló! Devolvemos Falso

            # Chequeo 2: ¿Ya hay un barco ahí?
            if self.board[r][c] != " ":
                print(f"❌ Error: Ya hay un barco en ({r},{c}).")
                return False  # ¡Falló!

        # --- COLOCACIÓN (Si llegamos aquí, es seguro) ---
        self.ships.append(ship)
        for r, c in ship.positions:
            self.board[r][c] = "S"

        return True  # ¡Éxito!


jugador1 = Player("Jugador 1")
jugador2 = Player("Jugador 2")

destructor = Destroyer()
submarino = Submarine()
acorazado = Battleship()

# --- ZONA INTERACTIVA ---


def jugar_batalla_naval():
    print("\n⚓️ BIENVENIDO ALMIRANTE A BATALLA NAVAL ⚓️")
    nombre = input("Ingrese su nombre: ")
    jugador = Player(nombre)

    # Lista de barcos que debe colocar
    flota = [Destroyer(), Submarine(), Battleship()]

    print(f"\n{nombre}, es hora de posicionar tu flota.")

    # Recorremos cada barco de la flota
    for barco in flota:
        colocado = False
        while not colocado:  # Repetir hasta que lo logre poner bien
            print(f"\n--- Colocando {barco.name} (Tamaño: {barco.size}) ---")

            try:
                # Pedimos datos al usuario
                fila = int(input("Fila (0-9): "))
                col = int(input("Columna (0-9): "))
                orientacion = input(
                    "Orientación (h/v): "
                ).lower()  # Convertimos a minúscula

                # Intentamos colocarlo usando el método que modificamos
                if jugador.add_ship(barco, fila, col, orientacion):
                    print(f"✅ {barco.name} desplegado.")
                    colocado = (
                        True  # Rompemos el ciclo while para pasar al siguiente barco
                    )

                    # Mostramos el mapa actualizado
                    print("\n--- Tu Tablero Actual ---")
                    for f in jugador.board:
                        print(f)
                else:
                    print("⚠️ Intenta de nuevo en otra posición.")

            except ValueError:
                print("❌ Error: Por favor ingresa NÚMEROS para fila y columna.")

    print("\n🎉 ¡FLOTA LISTA PARA EL COMBATE! 🎉")


# Ejecutamos el juego
if __name__ == "__main__":
    jugar_batalla_naval()

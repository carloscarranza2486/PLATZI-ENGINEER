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
    def __init__(self, name, size):
        super().__init__(name, size)

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def __str__(self):
        return f"{self.brand} {self.model} (${self.price})"


class Buyer:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.owned_cars = []

    def buy_car(self, car, dealership):
        dealership.sell_car(self, car)


class Dealership:
    def __init__(self):
        self.inventory = []

    def add_car(self, car):
        self.inventory.append(car)
        print(f"El {car.brand} {car.model} ha sido añadido al inventario")

    def show_available_cars(self):
        print("\n--- Vehículos disponibles---")
        for car in self.inventory:
            if car.is_available:
                print(f"- {car}")

    def sell_car(self, user, car):
        if car in self.inventory and car.is_available:
            if user.money >= car.price:
                user.money -= car.price
                car.is_available = False
                user.owned_cars.append(car)
                print(
                    f"\n ¡Felicidades {user.name}! Has comprado el {car.brand}{car.model}"
                )
            else:
                print(f"\n {user.name}, no tienes saldo suficiente")
        else:
            print(f"{car.brand} no disponible en el inventario")


car1 = Car("Toyota", "Corolla", 20000)
car2 = Car("Honda", "Civic", 22000)
car3 = Car("Ford", "Mustang", 30000)

user1 = Buyer("Carlos", 25000)

dealership = Dealership()
dealership.add_car(car1)
dealership.add_car(car2)
dealership.add_car(car3)

dealership.show_available_cars()

user1.buy_car(car2, dealership)

dealership.show_available_cars()

user1.buy_car(car3, dealership)

dealership.show_available_cars()

class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print("El vehículo {self.brand} ha sifo vendido")
        else:
            print("El vehículo {self.brand} no está disponible para la venta")

    def check_available(self):
        return self.is_available

    def get_price(self):
        return self.price

    def start_engine(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def stop_engine(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")


class Car(Vehicle):
    def start_engine(self):
        if not self.check_available():
            print("El motor del {self.brand} está en marcha")
        else:
            return "El vehículo de marca {self.brand} no está disponible para arrancar"

    def stop_engine(self):
        if self.is_available:
            print("El motor del {self.brand} se ha detenido")
        else:
            print("El vehículo de marca {self.brand} no está disponible para detenerse")


class Bike(Vehicle):
    def start_engine(self):
        if not self.check_available():
            print("El motor de la {self.brand} está en marcha")
        else:
            return "El vehículo de marca {self.brand} no está disponible para arrancar"

    def stop_engine(self):
        if self.is_available:
            print("El motor de la {self.brand} se ha detenido")
        else:
            print("El vehículo de marca {self.brand} no está disponible para detenerse")


class Truck(Vehicle):
    def start_engine(self):
        if not self.check_available():
            print("El motor del camión {self.brand} está en marcha")
        else:
            return "El vehículo de marca {self.brand} no está disponible para arrancar"

    def stop_engine(self):
        if self.is_available:
            print("El motor del camión {self.brand} se ha detenido")
        else:
            print("El vehículo de marca {self.brand} no está disponible para detenerse")


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(
                f"Lo siento {self.name}, el vehículo {vehicle.brand} no está disponible para la venta"
            )

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availability = "Disponible"
        else:
            availability = "No disponible"
        print(
            f"El vehículo {vehicle.brand} está {availability} y cuesta ${vehicle.get_price()}"
        )


class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El vehículo {vehicle.brand} ha sido añadido al inventario")

    def register_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido registrado")

    def show_available_vehicles(self):
        print("\n--- Vehículos disponibles ---")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} {vehicle.model} (${vehicle.price})")


car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-09", 9000)
truck1 = Truck("Ford", "F-150", 35000)

customer1 = Customer("Carlos")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)
dealership.register_customer(customer1)

# Mostrar vehículos disponibles
dealership.show_available_vehicles()

# Cliente consulta un vehículo

customer1.inquire_vehicle(car1)

# Cliente compra un vehículo
customer1.buy_vehicle(car1)

# Mostrar vehículos disponibles después de la compra
dealership.show_available_vehicles()

import asyncio
from hotel_management.reservations import Reservation, ReservationSystem
from hotel_management.customers import Customer, CustomerManagement
from hotel_management.rooms import Room, RoomManagement
from hotel_management.payments import process_payment
from datetime import datetime

async def main():
    
    # Inicializar sistemas
    reservation_system = ReservationSystem()
    customer_mgmt = CustomerManagement()
    room_mgmt = RoomManagement()

    # Crear habitaciones
    room1 = Room(101, "Sencilla", 100)
    room2 = Room(102, "Doble", 150)
    room_mgmt.add_room(room1)
    room_mgmt.add_room(room2)

    # Agregar clientes
    customer1 = Customer(1, "Alice", "alice@example.com")
    customer_mgmt.add_customer(customer1)

    # Verificar disponibilidad de habitaciones
    if room_mgmt.check_availability(101):
        # Crear reserva
        reservation = Reservation(1, "Alice", 101, datetime.now(), datetime.now())
        reservation_system.add_reservation(reservation)

        # Procesar pago asincrónicamente
        await process_payment(customer1.name, room1.price * 4)  # Pago por 4 noches
    if room_mgmt.check_availability(102):
        # Crear reserva
        reservation = Reservation(2, "Bob", 102, datetime.now(), datetime.now())
        reservation_system.add_reservation(reservation)

        # Procesar pago asincrónicamente
        await process_payment("Bob", room2.price * 4)  # Pago por 4 noches

    # Procesar pago asincrónicamente
if __name__ == "__main__":
    asyncio.run(main())


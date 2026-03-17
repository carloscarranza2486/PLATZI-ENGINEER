from collections import defaultdict
from datetime import datetime

class Reservation:
    def __init__(self, reservation_id, guest_name, room_number, check_in_date, check_out_date):
        self.reservation_id = reservation_id
        self.guest_name = guest_name
        self.room_number = room_number
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

class ReservationSystem:
    def __init__(self):
        self.reservations = defaultdict(list)

    def add_reservation(self, reservation):
        """Agrega una nueva reserva al sistema."""
        self.reservations[reservation.room_number].append(reservation)
        print(f"Reserva creada para {reservation.guest_name} en la habitación {reservation.room_number}")
        

    def cancel_reservation(self, reservation_id):
        """Cancela una reserva existente por ID."""
        for room_number, reservations in self.reservations.items():
            for reservation in reservations:
                if reservation.reservation_id == reservation_id:
                    reservations.remove(reservation)
                    print(f"Reserva {reservation_id} cancelada.")
                    return
        print(f"Reserva {reservation_id} no encontrada.")



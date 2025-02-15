""" 
Módulo para la gestión de reservas de hoteles, clientes y datos relacionados. 
Permite la creación, modificación y eliminación de hoteles, clientes y reservas. 
"""
import json
import os

# pylint: disable=too-few-public-methods
class Hotel:
    """Clase que representa un hotel con su información y reservas."""

    def __init__(self, hotel_id: str, name: str, location: str, rooms: int):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms = rooms
        self.reservations = []

def to_dict(self):
    """Convierte el objeto en un diccionario."""

    return {
        "hotel_id": self.hotel_id,
        "name": self.name,
        "location": self.location,
        "rooms": self.rooms,
        "reservations": self.reservations,
    }


# pylint: disable=too-few-public-methods
class Customer:
    """Clase que representa un cliente con su información."""

    def __init__(self, customer_id: str, name: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        """Diccionario datos para json."""

        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
        }

# pylint: disable=too-few-public-methods
class Reservation:
    """Reservaciones datos para json."""

    def __init__(self, reservation_id: str, customer_id: str, hotel_id: str):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def to_dict(self):
        """Diccionario datos para json."""

        return {
            "reservation_id": self.reservation_id,
            "customer_id": self.customer_id,
            "hotel_id": self.hotel_id,
        }


class ReservationSystem:
    """Clase de Reservaciones con los datos para json."""

    def __init__(
        self, hotel_file="hotels.json", customer_file="customers.json",
        reservation_file="reservations.json"
    ):
        self.hotel_file = hotel_file
        self.customer_file = customer_file
        self.reservation_file = reservation_file
        self.hotels = self.load_data(hotel_file, Hotel)
        self.customers = self.load_data(customer_file, Customer)
        self.reservations = self.load_data(reservation_file, Reservation)
        self.ensure_files_exist()

    def ensure_files_exist(self):
        """Revisa si existe previamente informacin con datos para json."""

        for file_name in [
            self.hotel_file,
            self.customer_file,
            self.reservation_file
        ]:

            if not os.path.exists(file_name):
                with open(file_name, "w", encoding="utf-8") as file:
                    json.dump({}, file)

    def load_data(self, file_name, cls):
        """Carga datos en json."""

        if os.path.exists(file_name):
            try:
                with open(file_name, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    return {key: cls(**value) for key, value in data.items()}
            except (json.JSONDecodeError, IOError):
                print(f"Error reading {file_name}. Initializing empty.")
        return {}

    def save_data(self, file_name, data):
        """guarda datos."""

        try:
            with open(file_name, "w", encoding="utf-8") as file:
                json.dump(
                         {k: v.to_dict() for k, v in data.items()},
                         file, indent=4
                )
        except IOError:
            print(f"Error writing {file_name}.")

    def create_reservation(self, reservation_id, customer_id, hotel_id):
        """Genera reservacion con los datos del json."""

        if (
            reservation_id not in self.reservations
            and customer_id in self.customers
            and hotel_id in self.hotels
        ):
            self.reservations[reservation_id] = Reservation(
                reservation_id, customer_id, hotel_id
            )
            self.save_data(self.reservation_file, self.reservations)
        else:
            print("Invalid reservation, customer, or hotel ID.")

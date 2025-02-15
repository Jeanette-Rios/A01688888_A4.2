import unittest
import os
from hotel_reservation_system import ReservationSystem


class TestReservationSystem(unittest.TestCase):
    def setUp(self):
        """Inicializa el sistema con archivos de prueba antes de cada test"""
        self.system = ReservationSystem("test_hotels.json", "test_customers.json", "test_reservations.json")

    def test_create_hotel(self):
        """Prueba la creación de un hotel."""
        self.system.create_hotel("H1", "Grand Hotel", "NY", 100)
        self.assertIn("H1", self.system.hotels)

    def test_delete_hotel(self):
        """Prueba la eliminación de un hotel."""
        self.system.create_hotel("H2", "Budget Inn", "LA", 50)
        self.system.delete_hotel("H2")
        self.assertNotIn("H2", self.system.hotels)

    def test_create_customer(self):
        """Prueba la creación de un cliente."""
        self.system.create_customer("C1", "John Doe", "john@example.com")
        self.assertIn("C1", self.system.customers)

    def test_delete_customer(self):
        """Prueba la eliminación de un cliente."""
        self.system.create_customer("C2", "Jane Doe", "jane@example.com")
        self.system.delete_customer("C2")
        self.assertNotIn("C2", self.system.customers)

    def test_create_reservation(self):
        """Prueba la creación de una reservación válida."""
        self.system.create_hotel("H3", "Test Hotel", "Boston", 60)
        self.system.create_customer("C3", "Alice", "alice@example.com")
        self.system.create_reservation("R1", "C3", "H3")
        self.assertIn("R1", self.system.reservations)

    def test_cancel_reservation(self):
        """Prueba la cancelación de una reservación."""
        self.system.create_hotel("H4", "Reserve Hotel", "Chicago", 50)
        self.system.create_customer("C4", "Charlie", "charlie@example.com")
        self.system.create_reservation("R2", "C4", "H4")
        self.system.cancel_reservation("R2")
        self.assertNotIn("R2", self.system.reservations)

    def tearDown(self):
        """Limpia los archivos de prueba después de cada ejecución."""
        for file in ["test_hotels.json", "test_customers.json", "test_reservations.json"]:
            if os.path.exists(file):
                os.remove(file)


if __name__ == "__main__":
    unittest.main()

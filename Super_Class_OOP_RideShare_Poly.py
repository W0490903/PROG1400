class Person:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def create_trip(self, route):
        print(f"{self.first_name + " " + self.last_name} is making a trip along the route: {route}.")

class Driver(Person):
    def __init__(self, first_name, last_name, phone, email, vehicle_make, vehicle_model, vehicle_colour, vehicle_plate, vehicle_type):
        super().__init__(first_name, last_name, phone, email)
        self.vehicle_make = vehicle_make
        self.vehicle_model = vehicle_model
        self.vehicle_colour = vehicle_colour
        self.vehicle_type = vehicle_type
        self.vehicle_plate = vehicle_plate

    def create_trip(self, route):
        print(f"{self.first_name + " " + self.last_name} is driving a {self.vehicle_colour + " " + self.vehicle_make + " " + self.vehicle_model} and is making a trip along the route: {route}.")

class Rider(Person):
    def __init__(self, first_name, last_name, phone, email):
        super().__init__(first_name, last_name, phone, email)

    def create_trip(self, route):
        print(f"{self.first_name + " " + self.last_name} will pick you up along the route: {route}")

class Route:
    def __init__(self, stops):
        self.stops = stops

driver1 = Driver("Zachary", "Mason", 000, "NULL", "Dodge", "Charger", "Blue", "NULL", "Car")
rider1 = Rider("John", "Smith", "NULL", "NULL")

route = ["Antigonish", "Afton", "NSCC-Strait"]

driver1.create_trip(route[0])
rider1.create_trip(route[0])

# Define a superclass representing a vehicle
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        pass


# Define subclasses representing different types of vehicles
class Car(Vehicle):
    def __init__(self, brand, color):
        super().__init__(brand)
        self.color = color

    def move(self):
        return f"Driving a {self.color} car"

    def honk(self):
        return "Beep beep!"


class Truck(Vehicle):
    def __init__(self, brand, capacity):
        super().__init__(brand)
        self.capacity = capacity

    def move(self):
        return f"Driving a truck with {self.capacity} tons capacity"

    def load_cargo(self, cargo):
        return f"Loading {cargo} into the truck"


# Define a factory class to create instances of vehicles
class VehicleFactory:
    def create_vehicle(self, vehicle_type, **kwargs):
        if vehicle_type == "car":
            return Car(**kwargs)
        elif vehicle_type == "truck":
            return Truck(**kwargs)
        else:
            raise ValueError("Invalid vehicle type")


# Client code
if __name__ == "__main__":
    factory = VehicleFactory()

    car = factory.create_vehicle("car", brand="Toyota", color="blue")
    truck = factory.create_vehicle("truck", brand="Volvo", capacity=5)

    print(car.move())  # Output: Driving a blue car
    print(car.honk())  # Output: Beep beep!
    print(truck.move())  # Output: Driving a truck with 5 tons capacity
    print(truck.load_cargo("boxes"))  # Output: Loading boxes into the truck

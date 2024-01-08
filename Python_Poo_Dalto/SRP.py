# each class have a functionality just one and it can do something without another classes
class Vehicle:
    """This class represents a vehicle."""

    def __init__(self, tank):
        """Initializes a vehicle with a given tank."""
        self.locate = 0
        self.tank = tank

    def move(self, distance):
        """
        Moves the vehicle a certain distance if there is enough nafta.
        The vehicle can only move if there is at least 50% nafta left.
        """
        if self.tank.get_nafta() >= distance / 2:
            self.locate += distance
            self.tank.use_nafta(distance / 2)
            print("You move the car")
        else:
            print("There is no enough nafta")

    def get_position(self):
        """Returns the current position of the vehicle."""
        return self.locate

class Tank_Nafta:
    """This class represents a nafta tank."""

    def __init__(self):
        """Initializes a nafta tank with full capacity."""
        self.capacity = 100 # assume the full capacity of the tank is 100 units

    def get_nafta(self):
        """Returns the current amount of nafta in the tank."""
        return self.capacity

    def use_nafta(self, amount):
        """Uses a certain amount of nafta from the tank."""
        self.capacity -= amount

    def add_nafta(self, amount):
        """Adds a certain amount of nafta to the tank."""
        self.capacity += amount

tank = Tank_Nafta()
little_car = Vehicle(tank)
print(little_car.get_position())
print(little_car.move(10))
print(little_car.get_position())
print(little_car.move(20))
print(little_car.get_position())
print(little_car.move(60))
print(little_car.get_position())
print(little_car.move(100))
print(little_car.get_position())
print(little_car.move(100))
print(little_car.get_position())
print(little_car.move(100))
print(little_car.get_position())
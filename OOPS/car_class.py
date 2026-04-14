class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name


my_car = Car('audi', 'a4', 2019)
print(my_car.get_descriptive_name())

"""Setting a default for an attribute """
class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    def read_odometer(self):
        print(f"this car has {self.odometer} miles on it!")


my_car = Car('audi', 'a4', 2019)
print(my_car.get_descriptive_name())
my_car.read_odometer()

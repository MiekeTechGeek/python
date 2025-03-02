# class Dog:
#     """A simple attempt to model a dog."""

#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """Simulate a dog sitting in response to a command."""
#         print(f"{self.name} is now sitting.")

#     def roll_over(self):
#         """Simulate rolling over in response to a command."""
#         print(f"{self.name} rolled over!")

#     def bark(self):
#         print(f"{self.name} is barking really loud at a dog at the age of {self.age}!")

# my_dog = Dog('Bolt', 6)
# your_dog = Dog('Willie', 3)

# miekes_dog = Dog("Bolt", 2)
# miekes_dog.bark()

# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()

# print(f"\nYour dog's name is {your_dog.name}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.sit()

# class Restaurant:

#     def __init__(self, name, cuisine):
#         self.name = name.lower().title().strip()
#         self.cuisine = cuisine.lower().strip()

#     def describe_restaurant(self):
#         print(f"This restuarant's name is {self.name}, and it serves {self.cuisine} cuisine.")

#     def open_restaurant(self):
#         print(f"{self.name} is now open!")

# nomu = Restaurant("nomu", "asian fusion")

# nomu.describe_restaurant()
# nomu.open_restaurant()


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


# my_used_car = Car('subaru', 'outback', 2019)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

my_mazda_sting = Car("Mazda", "Sting", "1960voetsek")
my_mazda_sting.update_odometer(1)
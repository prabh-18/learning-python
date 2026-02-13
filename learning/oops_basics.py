# ==========================================================
# OBJECT ORIENTED PROGRAMMING (OOP) BASICS - CAR EXAMPLE
# ==========================================================


# A CLASS is a blueprint or template.
# It defines what a Car should HAVE (attributes/data)
# and what a Car should DO (methods/actions).
#
# Think of it like a car factory design.
# The class itself is NOT a real car.
# It is just the plan.


class Car:

    # ------------------------------------------------------
    # __init__ is called the CONSTRUCTOR.
    # It runs automatically when we create a new object.
    #
    # It is used to initialize (set up) the attributes.
    #
    # "self" represents the CURRENT object being created.
    # ------------------------------------------------------
    def __init__(self, make, model, year, color):

        # ATTRIBUTES (DATA)
        # These belong to EACH individual object.
        # Every car object will have its own copy.

        self.make = make
        self.model = model
        self.year = year
        self.color = color

        # Speed starts at 0 for every new car
        self.speed = 0


    # ------------------------------------------------------
    # METHODS (ACTIONS)
    # Methods are functions defined inside a class.
    # They describe what the object can DO.
    #
    # Difference:
    # - Attributes = Data (information stored)
    # - Methods = Behavior (actions performed)
    # ------------------------------------------------------


    def accelerate(self, amount):
        # Increase speed by the given amount
        self.speed += amount
        print(f"{self.make} accelerated. Speed is now {self.speed} km/h")


    def brake(self, amount):
        # Decrease speed but never go below 0
        self.speed -= amount

        if self.speed < 0:
            self.speed = 0

        print(f"{self.make} slowed down. Speed is now {self.speed} km/h")


    def honk(self):
        print(f"{self.make} says: Beep Beep!")


    def get_info(self):
        # Returns car details as a string
        return f"{self.year} {self.color} {self.make} {self.model} | Speed: {self.speed} km/h"



# ==========================================================
# CREATING OBJECTS (INSTANCES)
# ==========================================================

# An OBJECT is a real instance created from the class blueprint.
# Each object has its own independent data.

car1 = Car("BMW", "M3", 2022, "Black")
car2 = Car("Audi", "A4", 2021, "White")
car3 = Car("Toyota", "Supra", 2023, "Red")


# ==========================================================
# CALLING METHODS ON DIFFERENT OBJECTS
# ==========================================================

car1.accelerate(50)
car1.honk()

print("--------------------------------")

car2.accelerate(30)
car2.brake(10)

print("--------------------------------")

car3.accelerate(100)
car3.brake(40)
car3.honk()

print("--------------------------------")

# ==========================================================
# SHOWING THAT OBJECTS ARE INDEPENDENT
# ==========================================================

# Even though they come from the same class,
# each object has its own separate data.

print(car1.get_info())
print(car2.get_info())
print(car3.get_info())


# Notice:
# Changing car1's speed does NOT change car2 or car3.
# That proves objects are independent instances.

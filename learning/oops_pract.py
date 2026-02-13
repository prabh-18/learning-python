# This is a CLASS (blueprint)
class Student:

    # __init__ is the constructor
    # It runs automatically when we create an object
    def __init__(self, name, marks):
        # These are ATTRIBUTES (data stored inside object)
        self.name = name      # self.name belongs to THIS student
        self.marks = marks    # self.marks belongs to THIS student

    # This is a METHOD (function inside a class)
    def show_details(self):
        # self refers to the object calling this method
        print("Name:", self.name)
        print("Marks:", self.marks)

    # Another method
    def study(self):
        print(self.name, "is studying...")


# -------------------------------
# Creating OBJECTS (instances)
# -------------------------------

s1 = Student("Drip", 85)     # Object 1
s2 = Student("Rahul", 70)    # Object 2


# -------------------------------
# Calling METHODS
# -------------------------------

s1.show_details()   # self = s1
print("-------------")
s2.show_details()   # self = s2
print("-------------")

s1.study()          # self = s1
s2.study()          # self = s2

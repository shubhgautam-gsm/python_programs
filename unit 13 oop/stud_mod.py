# stud_mod.py

class Student:
    # Constructor to initialize the object with name, id, and age
    """This is a docstring for the MyClass."""
    def __init__(self, name, id, age):
        self.name = name  # Assigning name attribute
        self.id = id      # Assigning id attribute
        self.age = age    # Assigning age attribute

    # Method to display the details of the student
    def display_details(self):
        print("Name: %s, ID: %d, Age: %d" % (self.name, self.id, self.age))
        


class Person(Student):  # Student class inherits from Person
    print('person')

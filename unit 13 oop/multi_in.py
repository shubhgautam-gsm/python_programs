# stud_mod.py

class Bca_Student:
    # Constructor to initialize the object with name, id, age, and city
    def __init__(self, name, id, age):
        self.name = name  # Assigning name attribute
        self.id = id      # Assigning id attribute
        self.age = age    # Assigning age attribute

    # Method to display the details of the BCA student
    def display_details1(self):
        print("BCA Student - Name: %s, ID: %d, Age: %d" % (self.name, self.id, self.age))
        
class Bsc_Student:
    # Constructor to initialize the object with name, id, and age
    def __init__(self, name, id, age):
        self.name = name  # Assigning name attribute
        self.id = id      # Assigning id attribute
        self.age = age    # Assigning age attribute

    # Method to display the details of the BSC student
    def display_details2(self):
        print("BSC Student - Name: %s, ID: %d, Age: %d" % (self.name, self.id, self.age))

class Person(Bsc_Student, Bca_Student):
    def __init__(self, name, id, age):
        self.name = name  # Assigning name attribute
        self.id = id      # Assigning id attribute
        self.age = age    # Assigning age attribute

    def display_details3(self):
        print("PERSON - Name: %s, ID: %d, Age: %d" % (self.name, self.id, self.age))
    # Constructor to initialize the object with name, id, and age


# Creating instances of Person
p1 = Person("aj", 3401, 25)
p2 = Person("vj", 2301, 25)
p3 = Person("mj", 2321, 25)


# Displaying details of the students
p1.display_details1()
p2.display_details2()
p3.display_details3()


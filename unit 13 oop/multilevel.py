# Base class
class Animal:
    def __init__(self, species):
        self.species = species

    def show_species(self):
        print("Species:", self.species)


# Intermediate class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the constructor of the base class
        super().__init__("Dog")
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")


# Derived class inheriting from Dog
class WorkingDog(Dog):
    def __init__(self, name, breed, purpose):
        # Call the constructor of the intermediate class
        super().__init__(name, breed)
        self.purpose = purpose

    def display_info(self):
        print("Name:", self.name)
        print("Breed:", self.breed)
        print("Purpose:", self.purpose)


# Create an instance of the derived class
my_dog = WorkingDog("Max", "German Shepherd", "Police work")

# Accessing methods from the base classes
my_dog.show_species()  # Output: Species: Dog
my_dog.bark()          # Output: Woof!

# Accessing methods from the intermediate and derived classes
my_dog.display_info()  # Output: Name: Max, Breed: German Shepherd, Purpose: Police work

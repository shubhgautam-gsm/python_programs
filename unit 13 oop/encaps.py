class Person:
    def __init__(self, name):
        self._name = name  # Encapsulated attribute

    def get_name(self):
        return self._name  # Getter method to access encapsulated attribute

    def set_name(self, name):
        self._name = name  # Setter method to modify encapsulated attribute

# Usage
person = Person("Alice")
print("Name:", person.get_name())  # Accessing encapsulated data
person.set_name("Bob")  # Modifying encapsulated data
print("Updated Name:", person.get_name())  # Accessing encapsulated data

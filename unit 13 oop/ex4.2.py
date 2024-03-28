class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an instance of Person with __init__ method
person = Person("John", 30)

# Accessing attributes
print(person.name)  # Output: John
print(person.age)   # Output: 30

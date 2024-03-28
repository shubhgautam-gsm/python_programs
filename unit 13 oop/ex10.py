class Student:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

# Creating an instance of Student
s = Student("John", 101, 22)

# Getting attribute 'name' using getattr()
print(getattr(s, 'name'))  # Output: John

# Modifying attribute 'age' using setattr()
setattr(s, "age", 23)
print(getattr(s, 'age'))   # Output: 23

# Checking if attribute 'id' exists using hasattr()
print(hasattr(s, 'id'))    # Output: True

# Deleting attribute 'age' using delattr()
delattr(s, 'age')

# Trying to access 'age' after deletion
# This will raise an AttributeError
print(s.age)

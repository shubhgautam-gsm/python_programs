import stud_mod

# Creating an instance of the Student class
s = stud_mod.Student("John", 101, 22)

# Printing the docstring of the class (if any)
print(stud_mod.Student.__doc__)

# Printing the dictionary containing the attributes of the object
print(s.__dict__)

# Printing the name of the module in which the class is defined
print(s.__module__)

# Printing the name of the class
print(stud_mod.Student.__name__)

# Printing the base classes of the class
print(stud_mod.Person.__bases__)

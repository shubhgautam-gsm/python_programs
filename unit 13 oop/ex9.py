# Parameterized Constructor
class Employee1:
    def __init__(self, name, id):
        self.id = id
        self.name = name

# Creating instances with parameterized constructor
emp1 = Employee1("John", 101)
emp2 = Employee1("David", 102)

print("Parameterized Constructor Output:")
print("Employee 1 ID:", emp1.id, "Name:", emp1.name)  # Output: Employee 1 ID: 101 Name: John
print("Employee 2 ID:", emp2.id, "Name:", emp2.name)  # Output: Employee 2 ID: 102 Name: David

# Non-Parameterized Constructor
class Employee2:
    def __init__(self):
        self.id = id
        self.name = "Unknown"

# Creating instances with non-parameterized constructor
emp1 = Employee2()
emp1.id = 101
emp1.name = "John"

emp2 = Employee2()
emp2.id = 102
emp2.name = "David"

print("\nNon-Parameterized Constructor Output:")
print("Employee 1 ID:", emp1.id, "Name:", emp1.name)  # Output: Employee 1 ID: 101 Name: John
print("Employee 2 ID:", emp2.id, "Name:", emp2.name)  # Output: Employee 2 ID: 102 Name: David

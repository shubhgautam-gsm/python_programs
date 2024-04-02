class Employee:
    __count = 0  # Private class variable to __count the number of employees

    def __init__(self):
        Employee.__count += 1  # Increment the count each time an instance is created

    def display(self):
        print("The number of employees:", Employee.__count)

emp = Employee()  # Create an instance of Employee
emp2 = Employee()  # Create another instance of Employee

try:
    print(emp.__count)  # Try to access the private class variable directly (will raise an AttributeError)
finally:
    emp.display()  # Display the number of employees using the display method

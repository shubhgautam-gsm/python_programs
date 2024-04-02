class Calculation1:
    def Summation(self, a, b):
        """Returns the sum of two numbers."""
        return a + b

class Calculation2:
    def Multiplication(self, a, b):
        """Returns the product of two numbers."""
        return a * b

class Derived(Calculation1, Calculation2):
    def Divide(self, a, b):
        """Returns the division of two numbers."""
        return a / b

# Create an instance of Derived class
d = Derived()

# Check if Derived is a subclass of Calculation2
print(issubclass(Derived, Calculation2))  # Output: True

# Check if Calculation1 is a subclass of Calculation2
print(issubclass(Calculation1, Calculation2))  # Output: False

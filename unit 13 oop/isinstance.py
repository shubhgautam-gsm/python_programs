class Calculation1:
    def Summation(self, a, b):
        return a + b

class Calculation2:
    def Multiplication(self, a, b):
        return a * b

class Derived(Calculation1, Calculation2):
    def Divide(self, a, b):
        return a / b

# Create an instance of Derived class
d = Derived()

# Check if d is an instance of Derived class
print(isinstance(d, Derived))  # Output: True

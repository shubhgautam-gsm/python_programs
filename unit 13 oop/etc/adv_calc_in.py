class Calculator:
    def __init__(self):
        self.result = 0  # Attribute (instance)

    def add(x):  # Method without self parameter
     result1 = x + 1  # This won't modify any instance attribute
     result2 = x + 2
     result3 = x + 3


class AdvancedCalculator(Calculator):
    def subtract(self, x, y):
        self.result = x - y  # New method specific to AdvancedCalculator

# Creating an instance of the subclass
my_advanced_calculator = AdvancedCalculator()

# Using inherited method from parent class
print(my_advanced_calculator.add())  # This will result in an error

# Using method specific to the subclass
my_advanced_calculator.subtract(10, 3)
print("Result after subtraction:", my_advanced_calculator.result)

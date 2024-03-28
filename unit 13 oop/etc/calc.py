class Calculator:
    def __init__(self):
        self.result = 0  # Attribute (instance)

    def add(self, x, y):
        self.result = x + y  # Method modifying an attribute

    def subtract(self, x, y):
        self.result = x - y  # Method modifying an attribute


my_calculator = Calculator()

user=str(input('write name u want to perform add | sub write : '))
if(user=='add'):
 val1=int(input('enter val  : '))
 val2=int(input('enter val  : '))
 my_calculator.add(val1, val2)       # Calling a method to perform addition
 print(my_calculator.result)   # Accessing the result attribute

if(user=='sub'):
    
 val1=int(input('enter val  : '))
 val2=int(input('enter val  : '))
 my_calculator.subtract(val1, val2)  # Calling a method to perform subtraction
 print(my_calculator.result)   # Accessing the updated result attribute

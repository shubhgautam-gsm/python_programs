class MyClass:
    def my_method(self, a, b, c, d, e):
        self.c = a + b
        self.d = a * b
        self.e = a / b

# Creating an instance of MyClass
obj = MyClass()

user_input = input('Write c for add | d for mult | e for div: ')

if user_input in ['c', 'd', 'e']:
    # Calling my_method based on user input
    obj.my_method(10, 20, None, None, None)
    if user_input == 'c':
        print(obj.c)  # Output: Result of addition
    elif user_input == 'd':
        print(obj.d)  # Output: Result of multiplication
    elif user_input == 'e':
        print(obj.e)  # Output: Result of division
else:
    print("Invalid input")

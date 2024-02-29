# required to be passed at the time of
# function calling with the exact match of their positions in the function call and function
# definition. If either of the arguments is not provided in the function call, or the position
# of the arguments is changed, the Python interpreter will show the error.

def func(name):
 message = "Hi "+name
 return message

name = input("Enter the name:")
print(func(name))
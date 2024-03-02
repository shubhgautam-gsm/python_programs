# DEFAULT ARGUMENTS
# Python allows us to initialize the arguments at the function definition. If the value of
# any of the arguments is not provided at the time of function call, then that argument
# can be initialized with the value given in the definition even if the argument is not
# specified at the function call.

def printme(name,age=22):
 print("My name is",name,"and age is",age)
 
 

printme(name = "john")

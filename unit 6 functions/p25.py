# A python callable() function in Python is something that can be called. This built-in
# function checks and returns true if the object passed appears to be callable,
# otherwise false.
x = 8
print('IS CALLABLE x',callable(x))

def x():
 a=10
 b=20
 c=a+b
 return c
 
print('IS CALLABLE x()',callable(x))
# a is an argument and a+10 is an expression which got evaluated and returned.
x = lambda a:a+10
# Here we are printing the function object
print(x)
print("sum = ",x(20))
# The above lambda function is same as the normal function.
def x(a):
 return a+10
print('sum =', x(20))
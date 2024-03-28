import math

# Python 3 - PI
print("Python 3 - PI")
print("Value of PI:", math.pi)


# Python 4 - Euler's Number
print("\nPython 4 - Euler's Number")
print("Value of Euler's Number:", math.e)

# Python 5 - math.log()
print("\nPython 5 - math.log()")
number = 2e-7
print("Natural logarithm of |2e-7|:", math.log(math.fabs(number), 10))

# Python 6 - math.log10()
print("\nPython 6 - math.log10()")
x = 13
print("Base 10 logarithm of 13:", math.log10(x))

# Python 7 - math.exp()
print("\nPython 7 - math.exp()")
number = 5e-2
print("e raised to the power of 0.05:", math.exp(number))

# Python 8 - math.pow()
print("\nPython 8 - math.pow()")
number = math.pow(10, 2)
print("10 raised to the power of 2:", number)

# Python 9 - math.floor()
print("\nPython 9 - math.floor()")
number = math.floor(10.25201)
print("Floor value of 10.25201:", number)

# Python 10 - math.ceil()
print("\nPython 10 - math.ceil()")
number = math.ceil(10.25201)
print("Ceil value of 10.25201:", number)

# Python 11 - math.fabs()
print("\nPython 11 - math.fabs()")
number = math.fabs(-10.001)
print("Absolute value of -10.001:", number)

# Python 12 - math.factorial()
print("\nPython 12 - math.factorial()")
number = math.factorial(7)
print("Factorial of 7:", number)

# Python 13 - math.modf()
print("\nPython 13 - math.modf()")
number = math.modf(44.5)
print("Fractional and integer parts of 44.5:", number)

# Explanation:

# - **PI and Euler's Number**: These are mathematical constants representing π and Euler's number, respectively.
# - **math.log() and math.log10()**: These functions compute the natural logarithm and base 10 logarithm of the given number, respectively.
# - **math.exp()**: This function calculates the value of Euler's number raised to the power of the given number.
# - **math.pow()**: It returns the value of the first argument raised to the power of the second argument.
# - **math.floor() and math.ceil()**: These functions return the largest integer less than or equal to, and the smallest integer greater 
#    than or equal to, the given number, respectively.
# - **math.fabs()**: It returns the absolute value of the given number.
# - **math.factorial()**: This function returns the factorial of the given integer.
# - **math.modf()**: It returns the fractional and integer parts of the given number as a tuple.
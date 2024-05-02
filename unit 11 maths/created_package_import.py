import maths

x = 22
print("Base 10 logarithm of 13:", maths.log10(x))
print("Base 10 logarithm of 13:", maths.log20(x))


print('sqr of ', x, ' is ', maths.sqr(x))
print('sqrt of ', x, ' is ', maths.sqrt(x))
number = 0.05
print("exp raised to the power of 0.05:", maths.exp(number))

# Test other custom functions
print("\nTesting other custom functions:")
print("Custom power function:", maths.custom_pow(2, 3))
print("Custom floor function:", maths.custom_floor(-5.2))
print("Custom ceil function:", maths.custom_ceil(5.7))
print("Custom absolute function:", maths.custom_fabs(-7))
print("Custom factorial function:", maths.custom_factorial(5))
print("Custom modf function:", maths.custom_modf(3.5))


# This will print the results of all the custom functions defined in your `maths` module.
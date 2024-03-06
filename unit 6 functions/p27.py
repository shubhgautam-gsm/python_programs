# The python exec() function is used for the dynamic execution of Python program which
# can either be a string or object code and it accepts large blocks of code,

code = """
y = 20
print(x + y)
"""  # String containing the code

x = 10

exec(code)  # Execute the code

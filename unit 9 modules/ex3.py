# main.py

import calc as mo
import importlib

# Perform addition
result_addition = mo.add(5, 3)
print("Result of addition:", result_addition)

# Perform subtraction
result_subtraction = mo.subtract(8, 4)
print("Result of subtraction:", result_subtraction)

# Now, let's modify the math_operations.py module
with open("math_operations.py", "w") as f:
    f.write("""
def add(a, b):
    return a + b + 1

def subtract(a, b):
    return a - b - 1
""")

# Reload the module
mo = importlib.reload(mo)

# Perform addition again with the modified function
result_addition_modified = mo.add(5, 3)
print("Modified result of addition:", result_addition_modified)

# Perform subtraction again with the modified function
result_subtraction_modified = mo.subtract(8, 4)
print("Modified result of subtraction:", result_subtraction_modified)

import calc3 as cal
import importlib

def get_input():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    return a, b

# Initial input
a, b = get_input()

# Perform division
print("Initial Div= ", cal.div(a, b))

# Reload the module after the initial operation
cal = importlib.reload(cal)

# Perform square
x = int(input("Enter a number to square: "))
print("Square= ", cal.square(x))

# Reload the module again
cal = importlib.reload(cal)
5
# Perform division again
a, b = get_input()
print("Modified Div= ", cal.div(a, b))

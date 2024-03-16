# main.py
import calc2 as cal
import importlib

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("Div= ", cal.div(a, b))
# Reload the module
cal = importlib.reload(cal)

# Try using the function again after reloading
print("Modified Div= ", cal.div(a, b))

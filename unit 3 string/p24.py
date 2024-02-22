# Title case strings:
print("This Is A Title Case String".istitle())   # True
print("Python Is Awesome".istitle())             # True

# Non-title case strings:
print("this is not title case".istitle())       # False
print("This Is NOT Title Case Either".istitle()) # False
print("This is title case with numbers 123".istitle()) # False
print("99 Is A Number".istitle())                       # False
print("PYTHON".istitle())                            # False

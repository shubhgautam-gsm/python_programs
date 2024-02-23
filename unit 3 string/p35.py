# Python splitlines() method example
# Variable declaration
str = "Java is a programming language"
# Calling function
str2 = str.splitlines() # returns a list having single element
print(str)
print(str2)
str = "Java \n is programming \r language"
str2 = str.splitlines() # returns a list having splitted elements
print(str2)
print(str)
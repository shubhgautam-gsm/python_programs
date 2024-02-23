# Python splitlines() method example
# Variable declaration
str = "Java \n is a programming \r language for \r\n software development"
# Calling function
str2 = str.splitlines() # returns a list having splitted elements
# Displaying result
print(str2)
# getting back list to string
print("".join(str2)) # now it does not contain any line breaker character
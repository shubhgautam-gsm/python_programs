print(ord('n'))


# Python translate() method
# Declaring table and variables
table = { 97 : 103, 111 : 112, 117 : None }
str = "Hello javatpoint"
# Calling function
str2 = str.translate(table)
# Displaying result
print(str2)
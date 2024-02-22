# Python isidentifier() method example
# Variable declaration should be following python name declartion rules
# Start with a letter (a-z, A-Z) or an underscore (_).
# The isidentifier() method checks if a string meets these criteria.
# Strings that start with numbers or contain special characters are not valid identifiers.
str1 = "abc_123"
str2="12abc"

# Calling function
str3 = str1.isidentifier()
str4 = str2.isidentifier()
# Displaying result
print(str3)
print(str4)
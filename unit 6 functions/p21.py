# Non-zero numbers: 1, 2, -3.14, etc. (except 0)
# Non-empty strings: "hello", "world", etc. (except the empty string "")
# Most collections: Lists, tuples, dictionaries, sets (as long as they have at least one element)
# True
# Falsy:

# Zero: 0
# Empty string: ""
# None: Represents the absence of a value
# False: The boolean value False
# Empty collections: Empty lists, tuples, dictionaries, sets

# all values true 
k = [1, 2, 4, 6]
print(all(k)) # all values false
k = ['0',1,1]
print(all(k)) # one false value 
k = [1, 3, 7, 0]
print(all(k))
# one true value 
k = [0, False, 5]
print(all(k))

# empty iterable 
k = []
print(all(k))
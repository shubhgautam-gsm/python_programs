# The python bytes() in Python is used for returning a bytes object. It is an immutable
# version of the bytearray() function.
# It can create empty bytes object of the specified size.

string = "Hello World."
array = bytes(string, 'utf-8')
print(array)
# The python bytearray() returns a bytearray object and can convert objects into
# bytearray objects, or create an empty bytearray object of the specified size.
string = "python is a programming language."
# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8')
print(arr)
arr[0] = 80  # Change the first byte to 'P'
print(arr)  # Output: bytearray(b'Python is a programming language.')

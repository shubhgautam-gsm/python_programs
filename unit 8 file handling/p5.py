f = open("file.txt", 'r')
content = f.read()
print(content)


# Now attempting to perform file operations
try:
    content = f.read()
except ValueError:
    print("The file is closed.")
else:
    print("The file is still open.")

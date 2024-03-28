import os
fd = "python.txt"
# popen() is similar to open()

file = os.popen(fd, 'w')  
file.write("This is awesome")

file = open(fd, 'r')
text = file.read()
print(text)
# popen() provides
# File not closed, shown in next function.

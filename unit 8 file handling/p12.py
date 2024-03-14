#open the file.txt in read mode. causes error if no such file exists.
fileptr = open("file1.txt","r")
# If we use the following line, then it will print all content of the file.
content = fileptr.read()
print(type(content)) # prints the type of the data stored in the file
print(content) #prints the content of the file
fileptr.close() #closes the opened file
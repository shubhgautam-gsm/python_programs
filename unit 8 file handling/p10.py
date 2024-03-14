#open the file.txt in read mode. causes error if no such file exists.
fileptr = open("file2.txt","r")
#stores all the data of the file into the variable content
content = fileptr.read(10)
print(type(content)) # prints the type of the data stored in the file
print(content) #prints the content of the file
fileptr.close() #closes the opened file
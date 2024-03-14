# print single line
#open the file.txt in read mode. causes error if no such file exists.
fileptr = open("file1.txt","r")
#stores all the data of the file into the variable content
content = fileptr.readline()
content1 = fileptr.readline()
print(content) #prints the content of the file
print(content1)
fileptr.close() #closes the opened file
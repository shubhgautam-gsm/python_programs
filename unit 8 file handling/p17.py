# open the file file1.txt in read mode
fileptr = open("file1.txt","r")
print("The filepointer is at byte :",fileptr.tell())
content = fileptr.read()
print("After reading, the filepointer is at:",fileptr.tell())
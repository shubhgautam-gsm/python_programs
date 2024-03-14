# open the file file1.txt in read mode
fileptr = open("file1.txt","r")
print("The filepointer is at byte :",fileptr.tell())
fileptr.read(10)#-work same but read load uncessary data
fileptr.seek(10)#-work same but seek not load unccessary data but jump poniter to that part
print("After reading, the filepointer is at:",fileptr.tell())
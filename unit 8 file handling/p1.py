# Opens the file file.txt in read mode
fileptr = open("file.txt", "r")

if fileptr:
    print("file is opened successfully and content is ",fileptr.read())
    
    # Close the file
fileptr.close()

try:
    fileptr = open("file2.txt", "r")
    try:
        fileptr.write("Hi I am good")  # Attempting to write to a file opened in read mode will raise an error
    finally:
        fileptr.close()
        print("file closed")
except Exception as e:
    print("Error:", e)
    
    
    
    
#finally always run 
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = a / b
    print("a / b = %d" %c)
except ValueError:
    print("Please enter valid integers for 'a' and 'b'.")
except ZeroDivisionError:
    print("Can't divide by zero")
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("Hi, I am the else block")
    


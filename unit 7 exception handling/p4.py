try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = a / b
    print("a / b = %d" % c)
except ValueError:
    print("Please enter valid integers for 'a' and 'b'.")
except ZeroDivisionError:
    print("Can't divide by zero")
except Exception as e:
    print("An unexpected error occurred:", e)
else:
    print("Hi, I am the else block")

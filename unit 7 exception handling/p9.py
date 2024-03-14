try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    if b == 0:
        raise ArithmeticError
    else:
        print("a/b = ", a / b)
except ArithmeticError:
    print("The value of b can't be 0")

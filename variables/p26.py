end = int(input("Enter the number up to which you want to print the natural numbers?"))

if end<=10:
 for i in range(1, end + 1):  # Exit the loop if i exceeds 10
    print(i, end=' ')
    
else:
    print('number out of range')


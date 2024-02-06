my_list = []  # Use a more descriptive variable name
num_elements = int(input("Enter the number of elements in the list: "))

for i in range(0,num_elements):  # Iterate from 0 to num_elements - 1
    # item = input("Enter item {}: ".format(i + 1))  # Prompt for each item
    my_list.append(input("Enter item :" ))

print("\nPrinting the list items:")
for it in my_list:  # Iterate over the list elements directly
    print(it, end="A ")

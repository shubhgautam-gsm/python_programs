my_list = [0,1,2,3,4]  # Use a more descriptive variable name
print("print original list:")
for i in my_list:  # Iterate from 0 to num_elements - 1
     print(i)
my_list.remove(int(input("give value for remove it")))

print("\nprinting the list after the removal of first element...")
for i in my_list:
    print(i,end=" ")

# Creating a list
my_list = [3, 1, 4, 1, 5, 9]

# insert(index, obj) - inserting an object at a specified index
my_list.insert(2, 6)
print("After inserting 6 at index 2:", my_list)

# pop(obj) - removing and returning the last object from the list
last_element = my_list.pop()
print("Removed last element:", last_element)
print("List after pop:", my_list)

# remove(obj) - removing a specified object from the list
my_list.remove(1)
print("After removing 1:", my_list)

# reverse() - reversing the list
my_list.reverse()
print("Reversed list:", my_list)

# sort([func]) - sorting the list
my_list.sort()
print("Sorted list:", my_list)

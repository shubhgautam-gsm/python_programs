# Creating a list
my_list = [1, 2, 3, 4, 5, 2, 3]

# append(obj) - adding an element to the list
my_list.append(6)
print("After appending 6:", my_list)

# clear() - removing all elements from the list
my_list.clear()
print("After clearing the list:", my_list)

# copy() - creating a shallow copy of the list
original_list = [1, 2, 3]
copied_list = original_list.copy()
print("Copied list:", copied_list)

# count(obj) - counting occurrences of an object in the list
my_list = [1, 2, 3, 4, 5, 2, 3]
count_2 = my_list.count(2)
print("Number of occurrences of 2:", count_2)

# extend(seq) - extending the list with elements from another sequence
my_list.extend([6, 7, 8])
print("After extending with [6, 7, 8]:", my_list)

# index(obj) - finding the index of an object in the list
index_3 = my_list.index(3)
print("Index of 3:", index_3)

#defining the function
def change_list(list1):
 list1.append(20) #.append means call by refrence 
 return list1
 
#defining the list
list1 = [10,30,40,50] #orignal

#calling the function
change_list(list1)
print("list call by reference function = ",list1)
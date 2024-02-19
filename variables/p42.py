list =[1,2,3,4]
count = 1
for i in list:
 count = count + 1
 if i == 4: 
  print("item matched")

  break

print("found at",count,"location")
str= "python"
print('break stop at if condition match ')
for i in str:
 if i == 'o':
  break
 print(i)
 
print('continue skip at if condition match and loop continue')
 
str1= "python"
for i in str:
  if i == 'o':
   continue
  print(i)
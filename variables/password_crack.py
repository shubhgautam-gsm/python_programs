usr_password=int(input('user password which not know by us '))
crk_pass =[654,564,456,546]
for i in crk_pass:
 if i==usr_password:
  print("usr original  password is this :",i)
  break


if i!=usr_password:
  print("usr original  password is not match :")
  



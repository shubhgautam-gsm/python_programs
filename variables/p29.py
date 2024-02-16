n = int(input("Enter the number of rows you want to print?"))
i,j=0,0
for i in range(0,n):
 print()
 for j in range(0,i+1):
  print("*",end="")
  
  
m = int(input("Enter the number of rows you want to print?"))
for k in range(0,m):
 print()
 for l in range(0,k+1):
  print(l,end="") 
# n=0 ,n=1 ,n=2 ,n=3 ,n=4 ,n=5
#
#o 
#o 1
#o 1 2
#o 1 2 3
#o 1 2 3 4
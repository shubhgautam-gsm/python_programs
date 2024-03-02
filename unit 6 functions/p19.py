# local scope sum outside not change
def calculate(*args):
 sum=0
 for arg in args:
  sum = sum +arg
 print("The sum is",sum)

sum=0
calculate(10,20,30) #60 will be printed as the sum
print("Value of sum outside the function:",sum) # 0 will be printed Output:
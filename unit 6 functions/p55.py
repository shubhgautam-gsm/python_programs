# Python filter() function example
def filterdata(x):
 if x>5:
  return x
# Calling function
result= filter(filterdata,(1,2,6,7,8,9))
# Displaying result
print(list(result))

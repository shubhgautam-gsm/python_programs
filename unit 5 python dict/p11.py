# In the dictionary, we cannot store multiple values for the same keys. If we pass more
# than one value for a single key, then the value which is last assigned is considered as
# the value of the key.
Employee={"Name":"John","Age":29,"Salary":25000,"Company":"GOOGLE","Name":"John"}
for x,y in Employee.items():
 print(x,y)

# In python, the key cannot be any mutable object. We can use numbers, strings, or
# tuples as the key, but we cannot use any mutable object like the list as the key in the
# dictionary
# Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE",(100,201,301):"Department ID"}
# tup allow because immutable (unchangable)

Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE",[100,201,301]:"Department ID"}
for x,y in Employee.items():
 print(x,y)
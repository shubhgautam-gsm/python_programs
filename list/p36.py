# The difference of two sets can be calculated by using the subtraction (-) operator
# or intersection() method. Suppose there are two sets A and B, and the difference is
# A-B that denotes the resulting set will be obtained that element of A, which is not
# present in the set B.


Days1 = {"Monday", "Tuesday", "Wednesday", "Thursday"}
Days2 = {"Monday", "Tuesday", "Sunday"}
print(Days1-Days2) #{"Wednesday", "Thursday" will be printed}
print(Days2-Days1) #{"Sunday"}
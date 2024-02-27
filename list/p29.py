# the pop() method 
# will always remove the last item but the set is unordered, we can't determine which 
# element will be popped from set
Months = set(["January","February", "March", "April", "May", "June"])
print("\nprinting the original set ... ")
print(Months)
print("\nRemoving some months from the set...")
Months.pop()
Months.pop()
print("\nPrinting the modified set...")
print(Months)
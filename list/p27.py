# discard not throw error if value not exist and we want to remove

months = set(["January","February", "March", "April", "May", "June"])
print("\nprinting the original set ... ")
print(months)
print("\nRemoving some months from the set...")
months.discard("January")
months.discard("May")
print("\nPrinting the modified set...")
print(months)
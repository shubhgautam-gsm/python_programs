# remove throw error if value not exist and we want to remove
months = set(["January","February", "March", "April", "May", "June"])
print("\nprinting the original set ... ")
print(months)
print("\nRemoving some months from the set...")
months.remove("January")
months.remove("May")
print("\nPrinting the modified set...")
print(months)

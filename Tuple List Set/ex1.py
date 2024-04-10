data = ["Surat", "Baroda", "Bhuj", "Rajkot", "Jamnagar","Rajkot", "Ahamdabad", "Morbi", "Rajkot"]

# Find the index of the first occurrence of "Rajkot"
first_index = data.index("Rajkot")
print("Index of first 'Rajkot':", first_index)

# Find the index of the second occurrence of "Rajkot"
second_index = data.index("Rajkot", first_index + 1)
print("Index of second 'Rajkot':", second_index)

third_index = data.index("Rajkot", second_index + 1)
print("Index of third 'Rajkot':", third_index)

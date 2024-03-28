import os

# Create a file
with open("Pytho1.txt", "w") as file:
    file.write("This is a test file.")

# Change the permissions to deny read and write access
os.chmod("Pytho1.txt", 0o000)
# Check if the file is readable
if os.access("Pytho1.txt", os.R_OK):
    print("You have read permission for 'Pytho1.txt'.")
else:
    print("You do not have read permission for 'Pytho1.txt'.")

# Check if the file is writable
if os.access("Pytho1.txt", os.W_OK):
    print("You have write permission for 'Pytho1.txt'.")
else:
    print("You do not have write permission for 'Pytho1.txt'.")

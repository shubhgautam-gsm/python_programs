# We should use the following method to overcome such type of problem.
try:
 fileptr = open("file.txt")
# perform file operations
finally:
 fileptr.close()

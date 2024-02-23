# Example of rindex() method

# Original string
original_string = "This is a sample string, with some sample text."

# Finding the last occurrence of the word "sample" using rindex() it if not found  return error 
# Finding the first occurrence of the word "sample" using find() it if not found return -1
# Finding the first occurrence of the word "sample" using index() it if not found  return error

last_index = original_string.rindex("sas")

# Displaying the result
if last_index != -1:
    print("Last occurrence of 'sample' found at index:", last_index)
else:
    print("Substring 'sample' not found in the original string.",last_index)

def change_number(number):
  """This function attempts to modify a passed value (call by value)."""
  number=number+[14]   # =number means call by value
  return number

number =[15,22,33]# original 'number'
change_number(number)
# print(change_number(number))
# Print the original value (unchanged)
print(number)  # Output: 15

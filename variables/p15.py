#List contain items of different data types. Lists are mutable i.e., modifiable

# The values stored in List are separated by commas(,) and enclosed within a square
# brackets([]). We can store different type of data in a List.
# Value stored in a List can be retrieved using the slice operator([] and [:]).
# The plus sign (+) is the list concatenation and asterisk(*) is the repetition operator.
# PYTHON 3
list=['aman',678,20.4,'saurav']
print(list)
print(type(list))
print("20.4's data type is",type(list[2]),
"\naman's data type is",type(list[0]))
print('\n',list[1:3])
print('\n either concat same var 3 times',list+list+list)
print('\n or * using estric multiply by 3',list*3)
print('\n same result in both way')
# This type of arguments is useful when we do not know the number of arguments inadvance.
# It is similar as the *args but it stores the argument in the dictionary format.
def food(**kwargs):
 print(kwargs)
 
food(a="Apple")
food(fruits="Orange", Vagitables="Carrot")
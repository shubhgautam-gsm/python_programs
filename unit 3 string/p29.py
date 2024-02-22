# Python partition() method example
str = "Java is a programming language"
str2 = str.partition("is") # Calling function
print(str2)
str2 = str.partition("Java") # when seperate from the start
print(str2)
str2 = str.partition("language") # when seperate is the end
print(str2)
str2 = str.partition("av") # when seperater is a substring
print(str2)
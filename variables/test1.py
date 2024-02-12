# 'in' check value exist in list,tuple or dictonary
x = ["a","b","c"]
y = ["a","b","d"]
z = {"apple", "orange"}

youtube_search=str(input('search what you want to get from youtube'))

print('search existence is :',youtube_search in x)
print('using == search existence is :',y[0] == x[0],' == check both value same ')
print('using "in" search existence is :',y[0] in x[0],'in check value exist in it')

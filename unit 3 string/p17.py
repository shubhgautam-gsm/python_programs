a="12345".isdecimal() # True
b="9⁸".isdecimal() # True (superscript digit)


e="12345".isdigit()
f="9⁸".isdigit()


print('is digit e',e)
print('is decimal a',a)
print('is digit f',f)
print('is decimal b',b)

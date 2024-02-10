#OPERATORS IN PYTHON
a=int(input('give value of a:'))
b=int(input('give value of b:'))
addi=a+b
subi=a-b
divi=a/b
multi=a*b

add,sub,mult,div='add','sub','mult','div'
calc_chs=str(input('write one of task to perform add|sub|mult|div:'))


if add==calc_chs:
 print('additon is:',addi)

elif sub==calc_chs:
 print('subtraction is :',subi)
 
elif mult==calc_chs:
  print('multi is :',multi)
elif div==calc_chs:
  print('div is:',divi)

else:
  print('....')




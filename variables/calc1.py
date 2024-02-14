#USE OF 'and' AND 'or' OPERATORS IN PYTHON
a=int(input('give value of a:'))
b=int(input('give value of b:'))
addi=a+b
subi=a-b
divi=a/b
multi=a*b

add,sub,mult,div='add','sub','mult','div'
calc_chs1=int(input('you want to perform single or multi operation: give "1" for single "2 for multiple'))
calc_chs=str(input('write one of task to perform add|sub|mult|div:'))


if calc_chs1==1 or calc_chs1==0:
 if add==calc_chs:
  print('additon is:',addi)
 elif sub==calc_chs:
  print('subtraction is :',subi)
 elif mult==calc_chs:
  print('multi is :',multi)
 elif div==calc_chs:
  print('div is:',divi)    

else:
 calc_chs2=str(input('write any other of task to perform add|sub|mult|div:'))
 if div==calc_chs and add==calc_chs2:
  print('div and add is:',divi,' and ',addi)
 elif div==calc_chs and sub==calc_chs2:
  print('div and sub is:',divi,' and ',subi)
 elif div==calc_chs and mult==calc_chs2:
  print('div and mult is:',divi,' and ',multi)
 elif mult==calc_chs and add==calc_chs2:
  print('mult and add is:',multi,' and ',addi)
 elif mult==calc_chs and sub==calc_chs2:
  print('mult and sub is:',multi,' and ',subi)
 elif mult==calc_chs and div==calc_chs2:
  print('mult and div is:',divi,' and ',divi)
 elif add==calc_chs and add==calc_chs2:
  print('add and div is:',addi,' and ',divi)
 elif add==calc_chs and sub==calc_chs2:
  print('add and sub is:',addi,' and ',subi)
 elif add==calc_chs and mult==calc_chs2:
  print('add and mult is:',addi,' and ',multi)  
 elif sub==calc_chs and add==calc_chs2:
  print('sub and add is:',subi,' and ',addi)
 elif sub==calc_chs and sub==calc_chs2:
  print('sub and div is:',subi,' and ',divi)
 elif sub==calc_chs and mult==calc_chs2:
  print('sub and mult is:',subi,' and ',multi)  
 



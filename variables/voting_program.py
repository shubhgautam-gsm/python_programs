#WE LEARN COMPARISION OPERATORS AND IF-ELSE STATEMENT and NESTED IF-ELSE
require_age=18
r_nationality='indian'
your_age=int(input('give your age:'))


if require_age<=your_age:
 y_nationality=str(input('your r_nationality:'))
 if r_nationality==y_nationality:
  print('eligle for vote because your age is :',your_age,'and your y_nationality is:',y_nationality)
 else:
  print('yourage is :',your_age,' proper but your nationality is:',y_nationality,' that why u are not eligble')

else:
 print('not eligle for vote because your age is  :',your_age)


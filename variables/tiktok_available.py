#WE LEARN COMPARISION OPERATORS AND IF-ELSE STATEMENT and NESTED IF-ELSE
r_nationality='india'
y_nationality=str(input('your live in which country:'))

have_vpn=1


if r_nationality!=y_nationality:
  print('you can play TIKTOK APP because you live in is:',y_nationality)

elif have_vpn==1:
  vpn=int(input('if you have vpn write 1 if you not have vpn  0: -->'))
  print(' you can play TIKTOK APP because you have vpn:')
else:
  print(' you cannot play TIKTOK APP because you live in :',y_nationality,' it is band in' ,y_nationality)




from datetime import datetime as dt
#Compares the time. If the time is in between 8AM and 4PM, then it prints working hours otherwise it prints fun hours
if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt(dt.now().year,dt.now().month,dt.now().day,16):
 print("Working hours....")
else:
 print("fun hours")
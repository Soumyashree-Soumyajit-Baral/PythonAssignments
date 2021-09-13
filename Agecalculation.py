from datetime import date

dd=int(input('Enter your Birth Date :'))
mm=int(input('Enter your Birth Month :'))
yy=int(input('Enter your Birth Year :'))        
dob=date(yy,mm,dd)
cd=date.today()
normalmonths=[31,28,31,30,31,30,31,31,30,31,30,31]
leapmonths=[31,29,31,30,31,30,31,31,30,31,30,31]
isleap=not dob.year%4
if isleap:
    months= leapmonths[mm-2]
else:
    months= normalmonths[mm-2]
y=cd.year-dob.year-((cd.month,cd.day) < (dob.month,dob.day))
m=(((cd.month-1)+12)-dob.month if(dob.day>cd.day and dob.month>=cd.month)else(cd.month-1)-dob.month if((cd.month>dob.month)and(dob.day>cd.day))
   else(cd.month+12)-dob.month if ((cd.month<dob.month) and (dob.day<cd.day)) else (cd.month-dob.month))
d=((cd.day+months)-dob.day if (dob.day>cd.day and dob.month>=cd.month)else (cd.day+months)-dob.day if((cd.month>dob.month)and(dob.day>cd.day))
   else cd.day-dob.day if ((cd.month<dob.month) and (dob.day<cd.day)) else cd.day-dob.day)
print(f'Your Age is : {y}years, {m}months, {d}days')
print('Thank You ! Please Come again whenever you forget your Age.')




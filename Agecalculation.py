from datetime import date

yy=int(input('Enter your Birth Year :'))
mm=int(input('Enter your Birth Month :'))
dd=int(input('Enter your Birth Date :'))        
dob=date(yy,mm,dd)
cd=date.today()
bd=date(yy,2,28)
l=[]
if dob>bd:
    for i in range(dob.year+1,cd.year):
        if not i%4:
            l.append(i)
else:
    for i in range(dob.year,cd.year):
        if not i%4:
            l.append(i)
d1=(cd-dob).days
y=int(d1/365)
m=int((d1%365)/30)
d=int(((d1%365)%30.416666666666668)-len(l))
print(f'Your Age is : {y}years, {m}months, {d}days')
print('Thank You ! Please Come again whenever you forget your Age.')

'''
#yy=int(input('Enter your Birth Year :'))
#mm=int(input('Enter your Birth Month :'))
#dd=int(input('Enter your Birth Date :'))        
#dob=date(yy,mm,dd)
dob=date(2000,4,13)
cd=date.today()
d1=(cd-dob)
print(d1)
d2=d1.days
y=int(d2/365)
m=int((d2%365)/30)
d=int((d2%365)%30.4167)
print(f'Your Age is : {y}years, {m}months, {d}days')
print('Thank You ! Please Come again whenever you forget your Age.')

'''


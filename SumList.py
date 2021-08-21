'''
from functools import reduce

list1=[10,20,306,130,580,80,97,650,450,304,50,67]
l2=reduce(lambda a,b :a+b,list1)
print('Sum of all numbers in the list is :',l2)


list1=[10,20,306,130,580,80,97,650,450,304,50,67]
sum=0
for i in range(0,len(list1)):
    sum+=list1[i]
print('Sum of all the element in the given list :',sum)


   
'''  

list1=[10,20,306,130,580,80,97,650,450,304,50,67]
total=sum(list1)
print('Sum of all the element in the given list :',total)

'''
from functools import reduce

l1=[10,22,63,98,56,24,14,17,25,35,2,3,8,5,100,150,256]
l2=reduce(lambda a,b : a if a>b else b,l1)
l3=reduce(lambda a,b : a if a<b else b,l1)
print('Greatest number in the list is :',l2)
print('Smallest number in the list is :',l3)
        
'''

l1=[10,22,63,98,56,24,14,17,25,35,2,3,8,5,100,150,256]
l1.sort()
print('Greatest number in the list is :',l1[(len(l1)-1)])
print('Smallest number in the list is :',l1[0])

'''
l1=[10,22,63,98,56,24,14,17,25,35,2,3,8,5,100,150,256]
l2=tuple(filter(lambda a :not a%2,l1))
l3=list(filter(lambda a : a%2,l1))
print(f'List of all even numbers in the list is : {l2}')
print(f'List of all odd numbers in the list is : {l3}')
'''




def even(a):
    if not a%2:
        return True
    else:
        return False

def odd(a):
    if a%2:
        return True
    else:
        return False


l1=[10,22,63,98,56,24,14,17,25,35,2,3,8,5,100,150,256]
l2=list(filter(even,l1))
l3=list(filter(odd,l1))
print(f'List of all even numbers in the list is : {l2}')
print(f'List of all odd numbers in the list is : {l3}')

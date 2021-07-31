'''
n=int(input('Enter no. of tickets'))
n1=int(input('Enter no. of person'))
age=int(input('Enter the age'))
p=int(input('Enter the price of the ticket'))                                   #d=00
print('Total price of tickets is :',n1*p)
if n1<=n:
    if age>=65:
        d=20
        print('You are senior citizen so, you will get 20% discount.')        #print('Discount price is :',p*d/100)
        print('final price of tickets is :',n1*(p-(p*d/100)))
    elif age<5:
        d=100
        print('You are child so, you will get 100% discount.')               #print('Discount price is :',p*d/100)
        print('final price of tickets is :',n1*(p-(p*d/100)))
    elif 5<age<=18:
        d=50
        print('You are kid so, you will get 50% discount.')                  #print('Discount price is :',p*d/100)
        print('final price of tickets is :',n1*(p-(p*d/100)))
    else:
        d=0
        print('You are adult so, you will not get any discount.')            #print('Discount price is :',p*d/100)
        print('final price of tickets is :',n1*(p-(p*d/100)))
else:
    print('invalid entry')
print('No of availabe ticket is :',n-n1)



n=int(input('Enter no. of tickets'))
n1=int(input('Enter no. of senior citizens'))
n2=int(input('Enter no. of childs'))
n3=int(input('Enter no. of minors'))
n4=int(input('Enter no. of adults'))
age1=int(input('Enter the age of senior citizen'))
age2=int(input('Enter the age of child'))
age3=int(input('Enter the age of minor'))
age4=int(input('Enter the age adult'))
p=int(input('Enter the price of single ticket'))                                   
print('Total price of tickets is :',p*(n1+n2+n3+n4))
if n1<=n and age1>=65:
    d=20
    fp1=n1*(p-(p*d/100))
    print('senior citizen will get 20% discount.')      
    print('the price of tickets after discount is :',fp1)
    if n2<=(n-n1) and age2<5:
        d=100
        fp2=n2*(p-(p*d/100))
        print('child will get 100% discount.')  
        print('the price of tickets after discount is :',fp2)
        if n3<=(n-(n1+n2)) and 5<age3<=18:
            d=50
            fp3=n3*(p-(p*d/100))
            print('minors will get 50% discount.')     
            print('the price of tickets after discount is :',fp3)
            if n4<=(n-(n1+n2+n3)) and 18<age4<65:
                d=0
                fp4=n4*(p-(p*d/100))
                print('adults will not get any discount.')           
                print('the price of tickets after discount is :',fp4)
else:
    print('invalid entry')                                
print('Final price of all the tickets is :',(fp1+fp2+fp3+fp4))
print('No of availabe ticket is :',n-(n1+n2+n3+n4))










n=int(input('Enter no. of tickets'))
n1=int(input('Enter no. of senior citizens'))
n2=int(input('Enter no. of childs'))
n3=int(input('Enter no. of minors'))
n4=n-(n1+n2+n3)                                                                 #int(input('Enter no. of adults'))
p=int(input('Enter the price of single ticket'))                                   
print('Total price of tickets is :',p*n)
if n1<=n :
    d=20
    fp1=n1*(p-(p*d/100))
    print('senior citizen will get 20% discount.')      
    print('the price of tickets after discount is :',fp1)
    if n2<=(n-n1) :
        d=100
        fp2=n2*(p-(p*d/100))
        print('child will get 100% discount.')  
        print('the price of tickets after discount is :',fp2)
        if n3<=(n-(n1+n2)) :
            d=50
            fp3=n3*(p-(p*d/100))
            print('minors will get 50% discount.')     
            print('the price of tickets after discount is :',fp3)
            if n4!=0:                                                             #<=(n-(n1+n2+n3)) :
                d=0
                fp4=n4*(p-(p*d/100))
                print('adults will not get any discount.')           
                print('the price of tickets after discount is :',fp4)
                print('Final price of all the tickets is :',(fp1+fp2+fp3+fp4))
else: print('invalid entry')                                

                                                                                  #print('No of availabe ticket is :',n-(n1+n2+n3+n4))

'''


n=int(input('Enter no. of tickets'))
p=int(input('Enter the price of single ticket'))
print('Price of tickets is :',p*n)
y=input('Do you have that much balance(y/n) :')
if y.lower()=='yes' or y.lower()=='y' :
    n1=int(input('Enter no. of senior citizens'))
    n2=int(input('Enter no. of childs'))
    n3=int(input('Enter no. of minors'))
    n4=n-(n1+n2+n3)                                                                 
    if n1<=n :
        d1=20
        print('senior citizen will get 20% discount.')      
        print('the price of tickets after discount is :',n1*(p-(p*d1/100)))
        if n2<=(n-n1) :
            d2=100
            print('child will get 100% discount.')  
            print('the price of tickets after discount is :',n2*(p-(p*d2/100)))
            if n3<=(n-(n1+n2)) :
                d3=50
                print('minors will get 50% discount.')     
                print('the price of tickets after discount is :',n3*(p-(p*d3/100)))
                if n4!=0:                                                             #<=(n-(n1+n2+n3)) :
                    d4=0
                    sum=n1*(p-(p*d1/100))+n2*(p-(p*d2/100))+n3*(p-(p*d3/100))+n4*(p-(p*d4/100))
                    print('adults will not get any discount.')           
                    print('the price of tickets after discount is :',n4*(p-(p*d4/100)))
                    print('Final price of all the tickets is :',sum)
                else: print('invalid entry')
            else: print('invalid entry')
        else: print('invalid entry')                                                         
    else: print('invalid entry')                                
else: print('kripeyaa aap ghar wapes jaye,, Mummy se paise lekar aaye,, fer milega ticket..samjhe!')




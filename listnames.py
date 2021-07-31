
southheros=['Naga Arjun','Chiranjiv','Mahesh Babu','Junior NTR','Ram Charan','Allu Arjun','Naga Chaitanya','Gopi Chand','Pavan Kalyan','Yash','Ravi Teja','Ram Pothenin']
n=input('Enter the name of your favorite south hero :')
if n in southheros:
    print('It was there in the list')
    southheros.remove(n)
    print('You removed the name of your favorite south hero and the final list is given below-')
    for i in southheros:
        print(i)
else:
    print('It is not there in the list')
    southheros.append(n)
    print('You have added the name of your favorite south hero and the final list is given below-')
    for i in southheros: 
        print(i)

'''











WWESuperstars=['Undertaker','Batista','Kane','Tripple H','Shawn Michaels','Randy Orton','Roman Reigns','John Cena','Brock Lesner','Seth Rollins','Edge']
n=input('Enter the name of your favorite WWE Superstar :')
if n in WWESuperstars:
    print('It is there in the list')
    WWESuperstars.remove(n)
    print('You removed the name of your favorite WWE Superstar and the final list is given below-')
    for i in WWESuperstars:
        print(i)
else:
    print('It is not there in the list')
    WWESuperstars.append(n)
    print('You have added the name of your favorite south hero and the final list is given below-')
    for i in WWESuperstars:
        print(i)
        
'''

s=input('Enter your string')
nonvowels=['b','c','d','f','g','h','j','k'',l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','E','X','Y','Z']
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in s:
    if i in vowels:  
        continue
    print(i)
    











'''
while s[::]!=0:
    s[::1]
    if s[::] not in nonvowels:
        continue
    print(s[::])




count=0
for j in s:
    print(j)
    if s[::] not in nonvowels:
        continue
    print(j)
    count+=1
'''

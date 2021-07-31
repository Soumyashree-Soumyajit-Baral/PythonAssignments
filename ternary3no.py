n1,n2,n3=int(input('Enter your first number')),int(input('Enter your second number')),int(input('Enter your third number'))
smaller=('first number is smaller'if n2>n1<n3 else'second number is smaller'if n1>n2<n3 else'third number is smaller'if n1>n3<n2 else
         'all are equal'if n1==n2==n3 else'first and second are equal and smaller'if n1==n2<n3 else
         'second and third are equal and smaller'if n2==n3<n1 else'first and third are equal and smaller')
print(smaller)
                                                                                          

                                                                                          

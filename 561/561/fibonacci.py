n = int(input("Enter limit"))
a = 0
b = 1
if n <= 2:
    print(a,"\n",b)
else:
    print(a)
    print(b)    
    for i in range(2,n+1):
        c = a+b
        a = b
        b = c
        print(c)




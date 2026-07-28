a = int(input("Enter a number"))
prime = False
if a / 1 == a and a / a == 1:
    for i in range(1,a):
        if a == i or a == 1:
            prime = True
        else:
            if a % i == 0:
                prime = False
            else:
                prime = True
print(prime)

n = int(input("Enter No of items"))
l1 = list(range(n))
for i in range(n):
    l1[i] = int(input("Enter no "))
for i in l1:
    if i == 0:
        print(i , " is Zero")
    elif i < 0:
        print(i , " is Negative")
    elif i > 0:
        print(i , " is Positive")

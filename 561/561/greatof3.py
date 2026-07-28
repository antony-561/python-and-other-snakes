a = int(input("Enter a no"))
b = int(input("enter 2nd no"))
c = int(input("Enter 3rd no"))
if a > b:
    if a>c:
        print("A is greatest")
    else:
        print("C is greatest")
elif b > a:
    if b>c:
        print("B is greatest")
    else:
        print("C is greatest")
elif c > a:
    if c > b:
        print("C is greatest")
    else:
        print("B is greatest")

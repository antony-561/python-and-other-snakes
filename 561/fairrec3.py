n = int(input("Enter Number n : "))
for i in range (n+1):
    num = i
    temp = num
    rev = 0
    while temp != 0:
        rem = temp % 10
        temp = int(temp / 10)
        rev = (10*rev) + rem
        if rev == num:
            print("Number ", num, "  is Palindrome")

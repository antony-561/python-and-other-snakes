qlist = """\n 1.Find the factorial of a number
\n 2.Check whether a number is prime or not
\n 3.Check whether a number is a palindrome or not
\n 4.Check whether Armstrong or not
\n 5.Reverse a number
\n 6.Find the square of a number
\n 7.Find the cube of a number
\n 0.Exit
"""
def findFact():
    print("Factorial of a number")
    n = int(input("enter no"))
    res = 1
    for i in range(1,n+1):
        res = res * i
    print(res)

def findPrime():
    print("Check Whether Prime")
    flag = True
    n = int(input("Enter No"))
    if n > 2:
        for i in range(2,n):
            if n%i ==0:
                flag = False
    if flag:
        print("It is a Prime Number")
    else:
        print("It is not a Prime Number")

def findPalindrome():
    print("Check Whether Palindrome")
    n = int(input("Enter No"))
    tnum = n
    rev = 0
    while tnum!=0:
        rem = tnum%10
        tnum = tnum//10
        rev = (rev*10) + rem
    if rev==n:
        print("It is a Palindrome")
    else:
        print("It is not a Palindrome")

def findArmstrong():
    print("Check whether armstrong")
    n = int(input("Enter No"))
    cnt = 0
    res = 0
    tnum = n
    while tnum != 0:
        tnum = tnum // 10
        cnt=cnt+1
    tnum = n
    while tnum!=0:
        rem = tnum%10
        tnum = tnum // 10
        res = res + (rem**cnt)
    if res == n:
        print("It is Armstrong")
    else:
        print("It is not Armstrong")
        
def findReverse():
    print("Check Whether Reverse")
    n = int(input("Enter No"))
    tnum = n
    rev = 0
    while tnum!=0:
        rem = tnum%10
        tnum = tnum//10
        rev = (rev*10) + rem
    print("Reverse of the number is : " , rev)

def findSquare():
    print("Find Square")
    n = int(input("Enter No"))
    res = n**2
    print("Square of ", n ," is ",res)
    
def findCube():
    print("Find Cube")
    n = int(input("Enter No"))
    res = n**3
    print("Cube of ", n ," is ",res)
    
ch = 1

while ch!= 0:
    ch = int(input(qlist))
    match(ch):
        case 1:
            findFact()
        case 2:
            findPrime();
        case 3:
            findPalindrome()
        case 4:
            findArmstrong()
        case 5:
            findReverse()
        case 6:
            findSquare()
        case 7:
            findCube()
        case 0:
            print("Exiting...")







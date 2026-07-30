qlist = """
\n1. Find the length of a string
\n2. Convert to uppercase
\n3. Convert to lowercase
\n4. Reverse the string
\n5. Check whether the string is a palindrome
\n6. Count vowels
\n7. Replace a substring
\n8. Search for a substring
\n9. Count the occurrence of a character
\n0. Exit
"""

ch = 1

def getStr():
    return input("Enter String")

def showLen():
    a = getStr()
    print("Length of given string is : ", len(a))

def conUp():
    a = getStr()
    b = a.upper()
    print("In Uppercase is : ", b)

def conDwn():
    a = getStr()
    b = a.lower()
    print("In Lowercase is : ", b)

def revStr():
    a = getStr()
    b = a[::-1]
    print("In Reversed is : ", b)

def palStr():
    a = getStr()
    b = a[::-1]
    if a == b:
        print("The string is a palindrome : ",a)
    else:
        print("The string is not a palindrome : ",a)

def vowStr():
    a = getStr()
    cnt = 0
    for i in a:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            cnt += 1
    print("No of vowels = ", cnt)

def repStr():
    a = getStr()
    b = input("enter word to replace")
    c = input("Enter new word")
    res = a.replace(b,c)
    print("Result String : ",res)

def serStr():
    a = getStr()
    b = input("Enter word to search")
    if b in a:
        print(b," found at location ," ,a.index(b), " of ", a)

def occChr():
    a = getStr()
    b = input("Enter letter to count")
    cnt = 0
    for i in a:
        if i == b:
            cnt += 1
    print("Found ",b,cnt," no of times...")
        
while ch!=0:
    print(qlist)
    ch = int(input("Enter Choice"))
    match ch:
        case 1:
            showLen()
        case 2:
            conUp()
        case 3:
            conDwn()
        case 4:
            revStr()
        case 5:
            palStr()
        case 6:
            vowStr()
        case 7:
            repStr()
        case 8:
            serStr()
        case 9:
            occChr()

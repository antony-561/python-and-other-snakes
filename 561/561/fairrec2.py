ch = 0

while ch != 5:
    ch = int(input("Enter Choice :\n 1: Find Sum\n 2: Find Reverse\n 3: Check Palindrome\n 4: Check Armstrong\n 5: Exit: \n"))
    match ch:
        case 1:
            num = int(input("Enter number"))
            temp = num
            rev = 0
            s1 = 0
            while temp != 0:
                rem = temp % 10
                temp = int(temp / 10)
                s1 = s1 + rem
            print("Sum = ", s1)
        case 2:
            num = int(input("Enter number"))
            temp = num
            rev = 0
            while temp != 0:
                rem = temp % 10
                temp = int(temp / 10)
                rev = (10*rev) + rem
            print("Reversed = ", int(rev))
        case 3:
            num = int(input("Enter number"))
            temp = num
            rev = 0
            while temp != 0:
                rem = temp % 10
                temp = int(temp / 10)
                rev = (10*rev) + rem
            if rev == num:
                print("Number is Palindrome")
            else:
                print("Number is not Palindrome")
        case 4:
            num = int(input("Enter number"))
            temp = num
            rev = 0
            cnt = 0
            arm = 0
            while temp != 0:
                temp = int(temp / 10)
                cnt = cnt + 1
            temp = num
            while temp != 0:
                rem = temp % 10
                arm = arm + (rem**cnt)
                temp = int(temp / 10)
            if arm == num:
                print("It is an armstrong number")
            else:
                print("It is not an armstrong number")
        case 5:
            print("Exiting.....")
                
                
                
    
            

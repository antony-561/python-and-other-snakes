ch = 0
while ch != 9:
    ch = int(input("Enter Choice"))
    match ch :
        case 1:
            print("Right Traingle")
            for i in range(10):
                print("*" * i)
        case 2:
            print("Inverted Right Triangle")
            for i in range(10,0,-1):
                print("*" * i)
        case 3:
            print("Number Triangle")
            for i in range(1,10+1):
                print()
                for k in range(1,i+1):
                        print(k ," ",end = "")
            print()
        case 4:
            print("Repeated number pattern")
            for i in range(10):
                print(str(i) * i)
        case 5:
            print("Floyds Triangle")
            a = 1
            for i in range(1,10+1):
                for k in range(1,i):
                    print(a,end = "")
                    a = a+1
                print()
            
        

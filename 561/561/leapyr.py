yr = int(input("Enter year"))
if yr%4 == 0:
    if yr%100 == 0:
        print("Not Leap year")
    else:
        print("Leap year")
elif yr % 400 == 0:
        print("Leap year")
    

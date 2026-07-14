#fairrec 5
ch = 1

while ch !=0:
    print("Enter Choice : \n 1: Create List;\n 2: Display all elements;\n 3: Append Item;\n 4: Insert an item;\n 5: Remove an item;\n 6: Delete using index;\n 7: Search for item;\n 8: Count no of occurence;\n 9: Sort in ascending order;\n 10: Reverse list order;\n 11: Extend with another list;\n 12: Display length of list;\n 0:Exit")
    ch = int(input())
    match ch:
        case 1:
            n = int(input("Enter no of elements in list"))
            l1 = list(range(n))
            print("Enter elements to list")
            for i in l1:
                i = input()
        case 2:
            print("The list is...")
            if l1:
                for i in l1:
                    print(i)
            else:
                print("List not created")
                
                

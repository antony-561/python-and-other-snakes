#fairrec 5
ch = 1
l1 = []
while ch !=0:
    print("Enter Choice : \n 1: Create List;\n 2: Display all elements;\n 3: Append Item;\n 4: Insert an item;\n 5: Remove an item;\n 6: Delete using index;\n 7: Search for item;\n 8: Count no of occurence;\n 9: Sort in ascending order;\n 10: Reverse list order;\n 11: Extend with another list;\n 12: Display length of list;\n 0:Exit")
    ch = int(input())
    match ch:
        case 1:
            n = int(input("Enter no of elements in list"))
            print("Enter elements to list")
            for i in range(n):
                l1.append(input())
        case 2:
            if l1:
                print("The list is...")
                for i in l1:
                    print(i)
            else:
                print("List not created")
        case 3:
            if l1:
                inp = input("enter element to append")
                l1.append(inp)
            else:
                print("List not created")
        case 4:
            if l1:
                inp = input("Enter Item to insert")
                pos = int(input("Enter position to insert"))
                l1.insert(pos, inp);
            else:
                print("List not created")
        case 5:
            if l1:
                item = input("enter items to delete")
                l1.remove()
            else:
                print("List not created")
        case 6:
            if l1:
                pos = int(input("Enter Items index to delete"))
                l1.pop()
            else:
                print("List not created")
        case 7:
            if l1:
                item = input("Enter element to search")
                if item in l1:
                    print(item, "Found! at ", l1.index(item))
                else:
                    print(item, "not Found")
            else:
                print("List not created")
        case 8:
            if l1:
                item = input("Enter element to count")
                if item in l1:
                    print("No of occurence = ", l1.count(item))
                else:
                    print("Item not found")
            else:
                print("List not created")
        case 9:
            if l1:
                l1.sort()
                print("List is sorted")
            else:
                print("List not created")
        case 10:
            if l1:
                l1.reverse()
                print("List is reveresed")
            else:
                print("List not Created")
        case 11:
            if l1:
                l2 = []
                n2 = int(input("Enter no of elements in new list"))
                for i in range(n2):
                    l2.append(input())
                l1.extend(l2)
                print("L1 is updated")
            else:
                print("List not created")
        case 12:
            if l1:
                print("Length of list = ",len(l1))
            else:
                print("List not created")
        
                

            

                
                

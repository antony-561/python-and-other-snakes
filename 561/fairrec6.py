qlist = """\n 1.Create a tuple using user input.
\n 2.Display all elements of the tuple.
\n 3.Search for an element in the tuple.
\n 4.Count the occurrences of a given element.
\n 5.Find the index of a given element.
\n 6.Display the largest and smallest elements.
\n 7.Calculate the sum and average of the tuple elements.
\n 8.Reverse the tuple.
\n 9.Sort the tuple in ascending order.
\n 0.Exit the program
\n Enter Choice
"""

ch = 1
tlist = []
tup = ()
while ch!=0:
    ch = int(input(qlist))
    match(ch):
        case 1:
            noElem = int(input("Enter No of elements in tuple"))
            for i in range(noElem):
                tlist.append(input("Enter Item: "))
            tup = tuple(tlist)
            print("\nTuple Created! \n",tup)
        case 2:
            if tup:
                print("The Tuple is...")
                for i in tup:
                    print(i)
            else:
                print("Tuple not created")
        case 3:
            if tup:
                item = input("Enter element to search")
                if item in tup:
                    print(item, "Found!")
                else:
                    print(item, "not Found")
            else:
                print("Tuple not created")
        case 4:
            if tup:
                item = input("Enter element to count")
                if item in tup:
                    print("No of occurence = ", tup.count(item))
                else:
                    print("Item not found")
            else:
                print("Tuple not created")
        case 5:
            if tup:
                item = input("Enter element to find index")
                if item in tup:
                    print(item, "Found at index ", tup.index(item))
                else:
                    print(item, "not Found")
            else:
                print("Tuple not created")
        case 6:
            
            
            
            
    

stak = []

def ins():
    item = input("Enter Element to insert")
    stak.insert(0,item)
            

    
def delete():
    item = stak.pop(0)
    print("deleted item = ", item)

def peek():
    print(stak[0])

def isEmpty():
    if stak:
        return
    else:
        print("Stack is empty")

ch = 1

while(ch!=5):
    ch = int(input("enter ch:"))
    

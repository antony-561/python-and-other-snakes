#Student Mark Management System

sname = input("enter Student name:")
sroll = int(input("Enter Roll no:"))
marks = []


def getMarks():
    try:
        for i in range(5):
            mk = int(input("Enter mark : "))
            if mk>100 or mk<0:
                raise ValueError("Invalid Mark Given (Below 100 and positive)")
            marks.append(mk)
    except ValueError as e:
        print(e)
        marks.clear()
        print("Enter marks Again!")
        getMarks()

def printMarks():
    for i in range(5):
        print(marks[i])
        
getMarks()
printMarks()


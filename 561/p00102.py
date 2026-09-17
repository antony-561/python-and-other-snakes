class shape:
    area = 0
    def printArea(self):
        print("Area = ",self.area)

class rect(shape):
    def __init__(self):
        l = int(input("Enter Length"))
        b = int(input("Enter Breadth"))
        self.area = l*b

class triangle(shape):
    def __init__(self):
        h = int(input("enter height"))
        b = int(input("enter base"))
        self.area = (0.5 * h * b)

class circle(shape):
    def __init__(self):
        r = int(input("enter radius"))
        self.area = (3.14 * r * r)

r1 = rect()
r1.printArea()
t1 = triangle()
t1.printArea()
c1 = circle()
c1.printArea()

l1 = ["Don","Shon","Venu","Davd"]
print(l1)
print(len(l1))
l1[2] = "Don 2"
print(l1)
for i in l1:
    print(i, " 0_0 ")
l1.append(5)
for i in l1:
    print(i, " 0_0 ")
for i in l1[2:4]:
    print(i)

l2 = [5,24,633,45,3,423]

#write a prgm to print each item with index
#

print(" *********Program 1*********")
l1 = ["Don","Shon","Venu","Davd"]
for i in range(len(l1)):
    print(i, " : " , l1[i])

#write a program to find sum of elements in the list
#

print(" *********Program 2*********")
s1 = 0
print("List = ")
for i in l2:
    print(i)
    s1 = s1+i
print("Sum = " , s1)
    

#write a program to find largest element in a list
#

print(" ********* Program 3 ********")
large = l2[0]
for i in l2:
    if i > large:
        print(i)
        large = i
print("Largest = ", large)


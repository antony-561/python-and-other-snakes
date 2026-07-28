n = int(input("Enter len of list"))
l1 = {}
print("Enter list items")
for i in range(n):
    l1[i] = int(input())

mni = l1[0]
for i in l1:
    if l1[i] < mni:
        mni = l1[i]

print("Min = ",mni)
    
            

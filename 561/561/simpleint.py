amt = int(input("Enter Principle Amount"))
irate = int(input("Enter Int Rate"))
time = int(input("Enter time"))
si = (amt*irate*time)/100
print("Simple Interest = ", si)
tot = amt + si
print("Total Amount = ",tot)


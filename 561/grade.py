mk1 = int(input("Enter mark1"))
mk2 = int(input("Enter mark2"))
mk3 = int(input("Enter mark3"))
mk4 = int(input("Enter mark4"))
mk5 = int(input("Enter mark5"))
tot = mk1+mk2+mk3+mk4+mk5
perc = (tot / 500) * 100
if perc > 98:
    gr = 'S'
elif perc > 90:
    gr = 'A'
elif perc > 80:
    gr = 'B'
elif perc > 70:
    gr = 'C'
elif perc > 60:
    gr = 'D'
elif perc > 50:
    gr = 'E'
else:
    gr = 'F'
print("Grade = " , gr)

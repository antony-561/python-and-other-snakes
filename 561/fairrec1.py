#Program 1
print("Student Grade Program")
name = input("Enter Name of Student")
mk1 = int(input("Enter mark 1"))
mk2 = int(input("Enter mark 2"))
mk3 = int(input("Enter mark 3"))
mk4 = int(input("Enter mark 4"))
mk5 = int(input("Enter mark 5"))
total = mk1+mk2+mk3+mk4+mk5
avg = total / 500
perc = avg * 100
if perc > 95:
    grade = "S"
elif perc > 90:
    grade = "A"
elif perc > 80:
    grade = "B"
elif perc > 70:
    grade = "C"
elif perc > 60:
    grade = "D"
elif perc > 50:
    grade = "E"
else:
    grade = "F"

print("Name : " , name)
print("Percentage : ", perc)
print("Grade : " , grade)

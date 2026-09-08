import pymysql

mydb = pymysql.connect (
    host = "localhost",
    user = "root",
    password = "windows",
    database = "imca561"
    )
curs = mydb.cursor()
roll = int(input("Enter roll"))
name = input("Enter name")

sqlq = "insert into student1 values(%s,%s);"

curs.execute(sqlq, (roll,name))
mydb.commit()


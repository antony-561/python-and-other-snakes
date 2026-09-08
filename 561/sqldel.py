import pymysql

mydb = pymysql.connect (
    host = "localhost",
    user = "root",
    password = "windows",
    database = "imca561"
    )
curs = mydb.cursor()
roll = int(input("Enter roll"))

sqlq = "delete from student1 where roll = %s;"

curs.execute(sqlq, (roll))
mydb.commit()


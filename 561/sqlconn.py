import pymysql

mydb = pymysql.connect (
    host = "localhost",
    user = "root",
    password = "windows",
    database = "imca561"
    )
curs = mydb.cursor()

sqlq = "create table student1(roll int, name varchar(20));"

curs.execute(sqlq)
mydb.commit()


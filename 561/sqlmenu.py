import pymysql

mydb = pymysql.connect (
    host = "localhost",
    user = "root",
    password = "windows",
    database = "imca561"
    )
c1 = mydb.cursor()
tflg = False
ch = 1
while ch != 6:
    ch = int(input("""
    Enter Choice \n
    1:Create Table \n
    2:Insert \n
    3:Delete Roll no \n
    4:Update Roll no \n
    5:View Table \n
    6:Exit Program: \n
"""))
    match ch:
        case 1:
            sqlq = """
                    Create table std1(
                        roll int,
                        name varchar(20),
                        dept varchar(6)
                    )
                    
                    """
            c1.execute(sqlq)
            print("table created")
            tflg = True
            mydb.commit()
        case 2:
            if tflg:
                roll = int(input("Enter Roll no"))
                name = input("Enter name")
                dept = input("Enter dept")
                sqlq = "insert into std1 values(%s,%s,%s)"
                c1.execute(sqlq, (roll,name,dept))
                print("Query Successfull")
                mydb.commit()
            else:
                print("Table not created")
        case 3:
            if tflg:
                roll = int(input("Enter Roll no to delete"))
                sqlq = "delete from std1 where roll = %s"
                c1.execute(sqlq, (roll))
                print("Query Successfull")
                mydb.commit()
            else:
                print("Table not created")
        case 4:
            if tflg:
                roll = int(input("Enter Roll no to update"))
                name = input("Enter name")
                sqlq = "update std1 set name = %s where roll = %s "
                c1.execute(sqlq, (name,roll))
                print("Query Successfull")
                mydb.commit()
            else:
                print("Table not created")
            

c1.execute("drop table std1")
mydb.commit()

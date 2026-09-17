import pymysql

empDb = pymysql.connect (
    host = "localhost",
    user = "root",
    password = "windows",
    database = "employee"
    )

c1 = empDb.cursor()

ch = 1

while(ch != 6):
    ch = int(input("""
Enter Choice
1:Create Table;
2:Insert into Table;
3:View Table;
4:Delete Record;
5:Update Record;
6:Exit;
"""))
    match(ch):
        case 1:
            sqlq = """
                create table emp1(
                    empid int,
                    ename varchar(20),
                    dept varchar(10));
                """
            c1.execute(sqlq)
            empDb.commit()
            print("Table Emp1 successfully created")
        case 2:
            eid = int(input("Enter emp id"))
            ename = input("Enter Name")
            dpt = input("Enter dept")
            sqlq = "insert into emp1 values(%s,%s,%s)"
            c1.execute(sqlq, (eid,ename,dpt))
            empDb.commit()
        case 3:
            sqlq = "select * from emp1"
            c1.execute(sqlq)
            records = c1.fetchall()
            print("EID  ENAME EDEPT")
            for r in records:
                print(r[0],r[1],r[2])
            empDb.commit()
        case 4:
            sqlq = "delete from emp1 where empid = %s;"
            eid = int(input("Enter emp id to delete"))
            c1.execute(sqlq, (eid))
            print("Emp id deleted")
            empDb.commit()
        case 5:
            sqlq = "update emp1 set ename = %s, dept = %s where empid = %s"
            eid = int(input("Enter emp id to update"))
            name = input("Enter updated name")
            dpt = input("Enter updated dept")
            c1.execute(sqlq, (name,dpt,eid))
            print("Record updated")
            empDb.commit()
        case 6:
            print("Exiting")
            c1.execute("drop table emp1")

import pymysql

hosp = pymysql.Connect(
    host = "localhost",
    user = "root",
    password = "windows",
    database = "imca561"
    )

c1 = hosp.cursor()

ch = 1
chStr = """
1: Insert To table
2: View Table
3: Update Table
4: Delete From Table
5: Exit
Enter Choice :
    """
table = """
    create table hospital(
        pid int primary key,
        pname varchar(20),
        age int,
        disease varchar(20)
        );
        """

#c1.execute(table)

while ch!=5:
    ch = int(input(chStr))
    match ch:
        case 1:
            print("Insert Record")
            sql = "insert into hospital values(%s,%s,%s,%s)"
            pid = int(input("Enter Patient Id"))
            pname = input("Enter Patient Name")
            age = int(input("Enter Patient Age"))
            disease = input("Enter Disease")
            c1.execute(sql,(pid,pname,age,disease))
            print("Record Inserted")
            hosp.commit()
        case 2:
            print("View Table")
            sql = "select * from hospital"
            c1.execute(sql)
            records = c1.fetchall()
            for r in records:
                print(r)
            hosp.commit()
        case 3:
            print("Update Table")
            sql = "update hospital set pname = %s, age = %s, disease = %s where pid = %s"
            pid = int(input("Enter patient id to update record"))
            pname = input("Enter updated name")
            age = int(input("Enter updated age"))
            disease = input("Enter updated disease")
            c1.execute(sql,(pname,age,disease,pid))
            print("Record Updated")
            hosp.commit()
        case 4:
            print("Delete from Table")
            sql = "delete from hospital where pid = %s;"
            pid = int(input("Enter id to delete record"))
            c1.execute(sql,(pid))
            print("record deleted")
            hosp.commit()
        case 5:
            print("Exiting")

                                      



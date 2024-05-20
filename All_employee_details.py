import mysql.connector as m
def view_all_records():
    try:
        con=m.connect(host="localhost", user="root", passwd="charan", database="employee_info")
        cur=con.cursor()
        cur.execute("select * from employee_info")
        #get all the record using fetchall()
        records=cur.fetchall()
        for record in records:
            for val in record:
                print("{}".format(val),end="\t")
                print()

    except m.DatabaseError as d:
        print("something went wrong:",d)
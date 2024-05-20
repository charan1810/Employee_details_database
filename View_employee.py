import mysql.connector as m
def view_Employee():
    while True:
        try:
            con=m.connect(host="localhost", user="root", passwd="charan",database="employee_info")
            cur=con.cursor()
            query="select * from employee_info where emp_id=%d"
            cur.execute(query %(int(input("Enter the id of the employee to view the record:"))))
            record=cur.fetchone()
            if record==None :
                print("You must have entered wrong employee Id, check once")
            else:
                for val in record:
                    print("{}".format(val),end="\t")
                    print()

        except m.DatabaseError as d:
            print("Something went wrong:",d)
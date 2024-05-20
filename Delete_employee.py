import mysql.connector as m
def del_emp():
    while True:
        try:
            con=m.connect(host="localhost", user="root", passwd="charan",database="employee_info")
            cur=con.cursor()
            query="delete from employee_info where emp_id=%d"
            cur.execute(query %(int(input("Enter the employee id that you want to delete"))))
            con.commit()
            if(cur.rowcount>0):
                print(cur.rowcount,"employee record deleted")
            else:
                print("Employee record doesn't exist")

            ch=input("If you want to delete record of another employee enter (yes/no): ")
            if ch=="no" or ch=="No" or ch=="NO":
                print("Thanks for using the program")
                break

        except m.DatabaseError as d:
            print("Something went wrong:",d)

        except ValueError:
            print("Don't Enter alnums,strs and symbols for Employee Number")



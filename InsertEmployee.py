import mysql.connector as m


def insert_employee():
    try:
        con = m.connect(host="localhost", user="root", passwd="charan")
        cur = con.cursor()

        cur.execute("CREATE DATABASE IF NOT EXISTS employee_info")
        cur.execute("USE employee_info")

        cur.execute("""CREATE TABLE IF NOT EXISTS employee_info (
                        emp_id INT PRIMARY KEY,
                        emp_name VARCHAR(255),
                        emp_contact VARCHAR(255),
                        emp_add VARCHAR(255),
                        emp_desgn VARCHAR(255),
                        emp_sal INT
                      )""")
        con.commit()
        print("Employee_info table is created")

        while True:
            try:
                emp_id = int(input("Enter employee id: "))
                emp_name = input("Enter employee name: ")
                emp_contact = input("Enter the contact of employee (Ph.No/E-mail): ")
                emp_add = input("Enter the employee address: ")
                emp_desgn = input("Enter the designation of the employee: ")
                emp_sal = int(input("Enter the salary of the employee (in terms of k) (like 400 for 400k): "))

                query = "INSERT INTO employee_info (emp_id, emp_name, emp_contact, emp_add, emp_desgn, emp_sal) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (emp_id, emp_name, emp_contact, emp_add, emp_desgn, emp_sal)
                cur.execute(query, values)
                con.commit()
                print("Record inserted successfully")
            except m.Error as e:
                print("Error while inserting data: ", e)

            ch = input("Do you want to insert another record (yes/no): ").strip().lower()
            if ch == "no":
                print("Thank you for using this program")
                break
    except m.Error as e:
        print("Sorry, the connection is unsuccessful due to:", e)
    finally:
        if con.is_connected():
            cur.close()
            con.close()
            print("MySQL connection is closed")




import mysql.connector as m


def update_employee():
    while True:
        try:
            con = m.connect(host="localhost", user="root", passwd="charan", database="employee_info")
            cur = con.cursor()
            print("The values need to be updated:")
            print(" 1. Employee Name\n 2. Employee Contact\n 3. Employee Address\n 4. Employee Designation & Salary")

            ch = int(input("Enter an option: "))

            if ch == 1:
                new_name = input("Enter the new name that needs to be updated: ")
                empl_id = int(input("Enter the employee ID: "))
                query = "UPDATE employee_info SET emp_name=%s WHERE emp_id=%s"
                cur.execute(query, (new_name, empl_id))

            elif ch == 2:
                new_contact = input("Enter the new contact: ")
                empl_id = int(input("Enter the employee ID: "))
                query = "UPDATE employee_info SET emp_contact=%s WHERE emp_id=%s"
                cur.execute(query, (new_contact, empl_id))

            elif ch == 3:
                new_add = input("Enter the new address: ")
                empl_id = int(input("Enter the employee ID: "))
                query = "UPDATE employee_info SET emp_add=%s WHERE emp_id=%s"
                cur.execute(query, (new_add, empl_id))

            elif ch == 4:
                new_desgn = input("Enter the new designation: ")
                new_salary = float(input("Enter the new salary: "))
                empl_id = int(input("Enter the employee ID: "))
                query = "UPDATE employee_info SET emp_desgn=%s, emp_sal=%s WHERE emp_id=%s"
                cur.execute(query, (new_desgn, new_salary, empl_id))

            else:
                print("Invalid option. Please choose a valid option.")
                continue

            con.commit()

            if cur.rowcount > 0:
                print(f"{cur.rowcount} Employee Record Updated")
            else:
                print("Employee Record does not exist")

        except m.Error as db_error:
            print("Problem in MySQL DB: ", db_error)
        except ValueError as ve:
            print("Invalid input: ", ve)
        finally:
            cur.close()
            con.close()

        ch = input("Do you want to update another record (yes/no): ")
        if ch.lower() == "no":
            print("Thanks for using this program.")
            break




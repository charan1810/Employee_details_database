#Employee_ProjectDemo.py
from menu_employee_details import menu
from InsertEmployee import insert_employee
from Delete_employee import del_emp
from Update_employee import update_employee
from View_employee import view_Employee
from All_employee_details import view_all_records
while(True):
    menu()
    ch=int(input("Enter Ur Choice:"))
    try:
            match(ch):
                case 1:
                    insert_employee()
                case 2:
                    del_emp()
                case 3:
                    update_employee()
                case 4:
                    view_Employee()
                case 5:
                    view_all_records()

                case 6:
                    print("Thanks for using Program")
                    break
                case _:
                    print("Your Selection of Operation is wrong-try again")
    except ValueError:
            print("Don't Enter Alphanumericals,str,symbols for Choice of Operation")
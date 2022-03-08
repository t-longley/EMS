"""
an Employee Management System. Allows user to add, update, remove, and list employee info. U/I in terminal with 
basic menu. Employee has first name, last name, employee id(unique), Date of 
employement, salary, and department as "string"/or a class. Employees stored as a list
Exceptions implemented in reasonable places. 1 custom exception needed.
1 List Comprehension needed
"""
class existError(Exception): pass
class inputException(Exception): pass

def menu(employees:list):

    print("MAIN MENU")
    print("1) Add Employees")
    print("2) Update Employees")
    print("3) Remove a Employee")
    print("4) List Employee information")
    print("5) Exit")

    #employees.sort()

    try:
        choice = int(input("Enter number of your option: "))
        if (choice < 1) or (choice > 5): raise inputException
    except ValueError:
        print("Option is not in proper format. Please use a numeric value. Eg. 1, 2, 3...\n")
        menu(employees)
    except inputException:
        print("Not a valid option. Choose an option from the list.\n")
        menu(employees)
    else:
        if choice == 1:
            addEmp(employees)
        elif choice == 2:
            updateEmp(employees)
        elif  choice == 3:
            removeEmp(employees)
        elif choice == 4:
            listEmp(employees)
        else:
            print("Exiting")
            exit(1)
    

def addEmp(employees: list):
    """Adds an employee"""
    print("\nAdding a new employee!")
    first = input("Please enter the first name: ").capitalize()
    last = input("Please enter the last name: ").capitalize()

    while True:
        try:
            id = int(input("Please enter a unique ID: "))
            if(uniqueID(id, employees)):
                break
            else:
                print(f"ID: {id} is already in use. Please enter a new ID number\n")
        except ValueError:
            print("Non-integer Input. Please enter a number")

    while True:
        try:
            salary = int(input("Please enter a numerical value for the salary: "))
        except ValueError:
            print("Invalid input. Please enter numbers: '12345...'")
        else:
            salary = "${:,.2f}".format(salary)
            break

    dept = input("Please enter the department: ")

    newEmp = [first, last, id, salary, dept]
    print("\nNew Employee Created!")
    print(f"{first} {last} ID: {id} Salary: {salary} Department: {dept}")
    employees.append(newEmp)
    menu(employees)

def updateEmp(emps: list):
    """Allows for employee updating"""
    print("\nUpdating an employee")

    while True:
        try:
            id = int(input("Please enter the ID number of the employee to update: "))
            if idExists(id, emps) == False:
                raise existError
        except ValueError:
            print("Invalid input. Please enter integers.")
        except existError:
            print(f"Error! ID number {id} does not exist!")
        else:
            break
    
    nFirst = input("Enter updated first name: ")
    nLast = input("Enter updated last name: ")
    nDate = input("Enter updated hire date: ")
    nSal = input("Enter updated salary: ")
    nDept = input("Enter updated department: ")

    newEmp = [nFirst, nLast, id, nDate, nSal, nDept]

    for employee in emps:
        if employee[2] == id:
            employee = newEmp
            break

    print(f"Updated Employee #{id}")
    print(f"First Name: {nFirst}")
    print(f"Last Name: {nLast}")
    print(f"Hire Date: {nDate}")
    print(f"Salary: {nSal}")
    print(f"Department: {nDept}")

    menu(emps)

def removeEmp(emps:list):
    """Removes an Employee"""
    print("\nRemove an employee")
    while True:
        try:
            num = int(input("Enter employee ID to remove: "))
            if(idExists(num, emps) == False):
                raise existError
        except ValueError:
            print("Invalid input. Please enter an integer.")
        except existError:
            print("Invalid ID. ID does not exist")
        else:
            break

    #removeEmp = [emp for emp in emps if int(emp[2]) == num]
    #print(removeEmp)
    #print(emps)
    for employee in emps:
        print(employee)
        if employee[2] == num:
            emps.remove(employee)

    
    
    #print(emps)
    #print(f"Removed Employee:\n{removeEmp}\n")
    menu(emps)

def listEmp(emps:list):
    """Lists an employee's info"""
    print("\nList Employee's info")
    #for emp in emps:
    #    sal = "${:,.2f}".format(int(emp[4]))
    #    print(f"{emp[0]} {emp[1]} ID: {emp[2]} Date Hired: {emp[3]} Salary: {sal} Department: {emp[5]}")

    empList = [emp for emp in emps if len(emps) > -1]
    print(empList)
    print("\nReturning to main menu\n")
    menu(emps)    

def uniqueID(idNum:int, emps:list):
    """Checks if ID passed is unique"""
    for employees in emps:
        if employees[2] == idNum:
            return False
    return True

def idExists(idNum:int, emps:list):
    """confirms an id number exists in the employees list"""
    for employees in emps:
        if employees[2] == idNum:
            return True
    return False

if __name__ == "__main__":
    #employees list with test data
    employees = [
        ['Timothy', 'Longley', 1, '3/1/2022', 90000, "IT"],
        ['John', 'Smith', 2, '12/09/2021', 50000, 'HR'],
        ['Sally', 'Sue', 3, '11/16/2020', 60000, 'Sales']
    ]
    
    menu(employees)
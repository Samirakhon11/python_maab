import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"
    
    @staticmethod
    def add_employee():
        employee_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        
        with open(EmployeeManager.FILE_NAME, "a") as file:
            file.write(f"{employee_id},{name},{position},{salary}\n")
        print("Employee added successfully!\n")
    
    @staticmethod
    def view_employees():
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.\n")
            return
        
        print("Employee Records:")
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                print(line.strip())
        print()
    
    @staticmethod
    def search_employee():
        employee_id = input("Enter Employee ID to search: ")
        found = False
        
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(employee_id + ","):
                    print("Employee Found:")
                    print(line.strip())
                    found = True
                    break
        
        if not found:
            print("Employee not found.\n")
    
    @staticmethod
    def update_employee():
        employee_id = input("Enter Employee ID to update: ")
        updated_records = []
        found = False
        
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(employee_id + ","):
                    print("Current Record:", line.strip())
                    name = input("Enter New Name: ")
                    position = input("Enter New Position: ")
                    salary = input("Enter New Salary: ")
                    updated_records.append(f"{employee_id},{name},{position},{salary}\n")
                    found = True
                else:
                    updated_records.append(line)
        
        if found:
            with open(EmployeeManager.FILE_NAME, "w") as file:
                file.writelines(updated_records)
            print("Employee record updated successfully!\n")
        else:
            print("Employee not found.\n")
    
    @staticmethod
    def delete_employee():
        employee_id = input("Enter Employee ID to delete: ")
        updated_records = []
        found = False
        
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                if not line.startswith(employee_id + ","):
                    updated_records.append(line)
                else:
                    found = True
        
        if found:
            with open(EmployeeManager.FILE_NAME, "w") as file:
                file.writelines(updated_records)
            print("Employee record deleted successfully!\n")
        else:
            print("Employee not found.\n")

    @staticmethod
    def menu():
        while True:
            print("Welcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            
            choice = input("Enter your choice: ")
            print()
            
            if choice == "1":
                EmployeeManager.add_employee()
            elif choice == "2":
                EmployeeManager.view_employees()
            elif choice == "3":
                EmployeeManager.search_employee()
            elif choice == "4":
                EmployeeManager.update_employee()
            elif choice == "5":
                EmployeeManager.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.\n")

EmployeeManager.menu()

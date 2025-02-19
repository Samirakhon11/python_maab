import os

employees_ID = []
employees_name = []
employees_position = []
employees_salary = []

if os.path.exists('employee.txt'):
    with open('employee.txt', "r") as file:
        for line in file:
            if line.strip():
                id, name, position, salary = line.strip().split(',')
                employees_ID.append(int(id))
                employees_name.append(name)
                employees_position.append(position)
                employees_salary.append(int(salary))
else:
    print("employee.txt not found. Starting with an empty record.")

while True:
    print("1. Add new employee record")
    print("2. View all employee records")
    print("3. Search for an employee by Employee ID")
    print("4. Update an employee's information")
    print("5. Delete an employee record")
    print("6. Exit")
    
    while True:
        try:
            option = int(input("What do you want to do: "))
            print('* '*30)
            break
        except ValueError:
            print("Enter number only: ")

    if option == 1:
        while True:
            try:
                id = int(input("Enter an ID for the employee: "))
                employees_ID.append(id)
                break
            except ValueError:
                print("Employee ID can be written with only numbers: ")

        name = input("Enter name of the employee: ")
        employees_name.append(name)

        position = input("Enter the position of the employee: ")
        employees_position.append(position)

        while True:
            try:
                salary = int(input("Enter the salary of the employee: "))
                employees_salary.append(salary)
                break
            except ValueError:
                print("Salary must be written with numbers only: ")

        print('* '*30)

    elif option == 2:
        with open('employee.txt', mode='a') as file_handler:
            print("List of all employees: ")
            for i in range(0, len(employees_ID)):
                print(f"{i + 1}. ID: {employees_ID[i]},   name: {employees_name[i]},   position: {employees_position[i]},   salary: {employees_salary[i]}")

        print('* '*30)

    elif option == 3:
        while True:
            try:
                find_id = int(input("Enter an ID to search: "))
                break
            except ValueError:
                print("Employee ID has only numbers: ")

        if find_id in employees_ID:
            index = employees_ID.index(find_id)
            print(f"ID: {employees_ID[index]},   name: {employees_name[index]},   position: {employees_position[index]},   salary: {employees_salary[index]}")
        else:
            print("This employee doesn't exist.")

        print('* '*30)

    elif option == 4:
        print("1. Name")
        print("2. Position")
        print("3. Salary")
        
        while True:
            try:
                find_id = int(input("Enter an ID to search: "))
                break
            except ValueError:
                print("Employee ID has only numbers: ")

        if find_id in employees_ID:
            index = employees_ID.index(find_id)
        else:
            print("This employee doesn't exist.")

        while True:
            try:
                option_change = int(input("What do you want to update? "))
                break
            except ValueError:
                print("Enter a number between 1 - 3: ")

        print("1. Name")
        print("2. Position")
        print("3. Salary")

        if  option_change == 1:
            new_name = input("Enter a new name: ")
            employees_name[index] = new_name

        elif option_change == 2:
            new_position = input("Enter a new position: ")
            employees_position[index] = new_position

        elif option_change == 3:
            while True:
                try:
                    new_salary = int(input("Enter a new amount of salary: "))
                    break
                except ValueError:
                    print("Salary must be written with numbers only")

        employees_salary[index] = new_salary

        print('* '*30)

    elif option == 5:
        while True:
            try:
                find_id = int(input("Enter an ID to search: "))
                break
            except ValueError:
                print("Employee ID has only numbers: ")

        if find_id in employees_ID:
            index = employees_ID.index(find_id)
            employees_ID.pop(index)
            employees_name.pop(index)
            employees_position.pop(index)
            employees_salary.pop(index)
        else:
            print("This employee doesn't exist.")

    elif option == 6:
        break

print("Program has finished working!")
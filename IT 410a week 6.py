import re

def get_valid_input(prompt, pattern, error_message):
    valid_input = False
    while not valid_input:
        user_input = input(prompt)
        if not re.match(pattern, user_input):
            print(error_message)
        else:
            valid_input = True
    return user_input

def get_employee_information(employee_number):
    print(f"Please enter information for employee {employee_number}:")
    
    employee_id = get_valid_input("Enter employee ID (7 digits or less): ",                              
                                  "Invalid employee ID. Please try again.")
    
    employee_name = get_valid_input("Enter employee name: ", 
                                    "Invalid employee name. Please try again.")
    
    employee_email = get_valid_input("Enter employee email address: ",
                                     "Invalid email address. Please try again.")
    
    employee_dict = {
        "ID": employee_id,
        "Name": employee_name,
        "Email": employee_email,
    }
    return employee_dict

def print_employee_info(employee):
    if not employee["Address"]:
        print(f"Hello, {employee['Name']}. Your Employee ID is {employee['ID']}, "
              f"and your email address is {employee['Email']}. You did not provide an address.")
    else:
        print(f"Hello, {employee['Name']}. Your Employee ID is {employee['ID']}, "
              f"and your email address is {employee['Email']}. Your address is {employee['Address']}.")

employees = []
num_employees = 0

while num_employees < 5:
    employee = get_employee_information(num_employees + 1)
    employees.append(employee)
    num_employees += 1

# Print list of employees
print("Employee information:")
for employee in employees:
    print_employee_info(employee)

# Payroll System
class Employee:
    def __init__(self, emp_id, name, hours, hourly_rate):
        self.emp_id = emp_id
        self.name = name
        self.hours = hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        self.sal=self.hours* self.hourly_rate
        if self.sal>=35000 and self.sal<50000:
            self.sal-=(self.sal*(5/100))
        elif self.sal>=50000: 
            self.sal-=(self.sal*(10/100))
        return self.sal
def add_employee(employee_list):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    hours= float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))
    employee = Employee(emp_id, name, hours, hourly_rate)
    employee_list.append(employee)
    print(f"Employee {name} added successfully.\n")

def display_payroll(employee_list):
    if not employee_list:
        print("\nNo employee data available.\n")
        return

    print("\n--- Payroll Details ---")
    for emp in employee_list:
        print(f"ID: {emp.emp_id} | Name: {emp.name} | Hours Worked: {emp.hours} | Hourly Rate: {emp.hourly_rate} | Salary: {emp.calculate_salary()}")

def delete_employee(employee_list):
    emp_id = input("Enter Employee ID to delete: ")
    for emp in employee_list:
        if emp.emp_id == emp_id:
            employee_list.remove(emp)
            print(f"Employee {emp.name} (ID: {emp.emp_id}) deleted successfully.\n")
            return
    print(f"No employee found with ID: {emp_id}\n")

def save_to_file(employee_list, filename='payroll.txt'):
    with open(filename, 'w') as f:
        for emp in employee_list:
            f.write(f"{emp.emp_id}, {emp.name}, {emp.hours}, {emp.hourly_rate}, {emp.calculate_salary()}\n")
    print("Data saved to payroll.txt\n")

def load_from_file(filename='payroll.txt'):
    employee_list = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                emp_id, name, hours, hourly_rate, salary = line.strip().split(', ')
                employee = Employee(emp_id, name, float(hours), float(hourly_rate))
                employee_list.append(employee)
        print("Data loaded from file.\n")
    except FileNotFoundError:
        print("No previous data found, starting fresh.\n")
    return employee_list

employee_list = load_from_file()

while True:
    print("\nPayroll System Menu:")
    print("1. Add Employee")
    print("2. Display Payroll")
    print("3. Delete Employee")
    print("4. Save ")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '1':
        add_employee(employee_list)
    elif choice == '2':
        display_payroll(employee_list)
    elif choice == '3':
        delete_employee(employee_list)
    elif choice == '4':
        save_to_file(employee_list)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")



employees = {
    101: {
        "name": "Rahul",
        "salary": 65000
    },
    102: {
        "name": "Anu",
        "salary": 55000
    }
}

# Find employee by ID
emp_id = int(input("Enter employee ID to search: "))
if emp_id in employees:
    print(employees[emp_id])
else:
    print("Employee not found")

# Add a new employee
new_id = int(input("Enter new employee ID: "))
name = input("Enter name: ")
salary = int(input("Enter salary: "))

employees[new_id] = {
    "name": name,
    "salary": salary
}

# Update salary
update_id = int(input("Enter employee ID to update salary: "))
if update_id in employees:
    new_salary = int(input("Enter new salary: "))
    employees[update_id]["salary"] = new_salary
    print("Salary updated")
else:
    print("Employee not found")

# Delete an employee
delete_id = int(input("Enter employee ID to delete: "))
if delete_id in employees:
    del employees[delete_id]
    print("Employee deleted")
else:
    print("Employee not found")

# Display all employees
print("Employee Details")
for emp_id, details in employees.items():
    print("ID:", emp_id)
    print("Name:", details["name"])
    print("Salary:", details["salary"])
    print()
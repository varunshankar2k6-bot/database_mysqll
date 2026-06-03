employees = {
    101: {"name": "Rahul", "salary": 65000, "department": "IT"},
    102: {"name": "Anu", "salary": 55000, "department": "HR"},
    103: {"name": "John", "salary": 85000, "department": "IT"}
}

#Question 1: Group employees by department
dept_groups = {}
for emp_id, details in employees.items():
    department = details["department"]
    if department not in dept_groups:
        dept_groups[department] = []
    dept_groups[department].append(details["name"])
print(dept_groups)

#Question 2: Count employees in each department
for department, employees in dept_groups.items():
    print(department, ":", len(employees))

#Question 3: Calculate average salary by department
salary = {}
for details in employees.values():
    department = details["department"]
    if department not in salary:
        salary[department] = []
    salary[department].append(details["salary"])
for department, salaries in salary.items():
    avg = sum(salaries) / len(salaries)
    print(department, "Average Salary =", avg)

#Question 4: Find the highest paid employee in each department
for department, salaries in salary.items():
    highest_salary = max(salaries)
    for details in employees.values():
        if details["department"] == department and details["salary"] == highest_salary:
            print(department, ":", details["name"], "-", highest_salary)

#Question 5:Sort employees by salary
sorted_employees = sorted(
    employees.items(),
    key=lambda x: x[1]["salary"]
)
for emp_id, details in sorted_employees:
    print(emp_id, details["name"], details["salary"])

#Question 6: Search for employees in a specific department
search=input("Enter department to search: ")
for emp_id, details in employees.items():
    if details["department"] == search:
        print(details["name"])

#Question 7: Calculate total and average salary by department
for department in salary:
    total = sum(salary[department])
    avg = total / len(salary[department])
    print("Department:", department)
    print("Total Salary:", total)
    print("Average Salary:", avg)
    print("Employees:", len(salary[department]))
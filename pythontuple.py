#Question 1: Create a tuple with student details
student = (2, "Varun", 211, "ECE")
print("Student Details:")
#For loop to print elements
for i in student:
    print(i)

#Question 2: Create marks tuple and print marks
marks=(25,90,89,71,40,55)
#splicing first three marks
marksfirst=marks[:3]
print("Marks of first three subjects: ", marksfirst)
#Splicing last two marks
markslast=marks[-2:]
print("Marks of last two subjects: ", markslast)
#Splicing middle two marks
marksmiddle=marks[3:len(marks)-2]
print("Marks of middle two subjects: ", marksmiddle)

#Question 3: Tuple name count
student_name=("Varun", "Ravi", "Sita", "Varun","Varun")
#Count function to count specific name in tuple
count=student_name.count("Varun")
print("Count of name in tuple: ", count)

#Question 4: Tuple unpacking
employee = (101, "Arun", 50000,"ECE")
#Giving seperate varuables according to index
emp_id=employee[0]
emp_name=employee[1]
emp_salary=employee[2]
emp_department=employee[3]
print("Employee ID:", emp_id)
print("Employee Name:", emp_name)
print("Employee Salary:", emp_salary)
print("Employee Department:", emp_department)

#Question 5:
employees = (
    (101, "Rahul", "Developer", 65000),
    (102, "Anu", "Tester", 55000),
    (103, "John", "Manager", 85000)
)

#Searching using id
id=int(input("Enter employee ID: "))
#For loop to search employee details using id
for i in range(len(employees)):
    if employees[i][0]==id:
        print("Employee Details:")
        print("ID:", employees[i][0])
        print("Name:", employees[i][1])
        print("Role:", employees[i][2])
        print("Salary:", employees[i][3])
designation=input("Enter employee designation: ")

#To count number of employees with specific designation
count=0
for i in range(len(employees)):
    if employees[i][2]==designation:
        count=count+1
print("Number of employees with designation", designation, "is:", count)

#To find max, min and average salary by taking salary list
salary=[]
for i in range(len(employees)):
    salary.append(employees[i][3])
salary.sort()
print("Max salary is ",salary[-1])
print("Min salary is ",salary[0])
#Average salary calculation
avg=sum(salary)/len(salary)
print("Average salary is ",avg)

#Searching employee details using name
name=input("Enter employee name: ")
for i in range(len(employees)):
    if employees[i][1]==name:
        print("Employee Details:")
        print("ID:", employees[i][0])
        print("Name:", employees[i][1])
        print("Role:", employees[i][2])
        print("Salary:", employees[i][3])
    else:
        print("Employee not found.")

#To find employees with salary greater than 60000
for i in range(len(employees)):
    if employees[i][3]>60000:
        print("Employee Details:")
        print("ID:", employees[i][0])
        print("Name:", employees[i][1])
        print("Role:", employees[i][2])
        print("Salary:", employees[i][3])

#To covert tuple to list and sort by salary
employeelist=list(employees)
employeelist.sort(key=lambda x: x[3])
print("Employees sorted by salary:")
print(employeelist)

#To print employee details using tuple unpacking
for emp_id, name, designation, salary in employees:
    print("ID:", emp_id)
    print("Name:", name)
    print("Designation:", designation)
    print("Salary:", salary)
    print()


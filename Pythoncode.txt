name=input("enter name  ")
age=int(input("enter age    "))
course=input("enter course  ")
marks=float(input("enter marks out of 100   "))
print("-----Student Details-----")
print("Name: ",name)
print("Age: ",age)
print("Course: ",course)
print("Marks: ",marks)
if marks>=40:
    print("Pass")
else:
    print("Fail")

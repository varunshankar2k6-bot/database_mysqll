#Defining a function to generate a student report
def student_report(*args, **kwargs):
    #Lambda function to calculate average marks
    avg = lambda marks:sum(marks)/len(marks)
    print("Student Name:",kwargs.get("name"))
    print("Roll Number:",kwargs.get("roll_no"))
    print("Total Marks:",sum(args))
    print("Average Marks:", avg(args))
#Giving student details
student_report(
    80, 90, 100,40,
    name="Varun",
    roll_no=21
)
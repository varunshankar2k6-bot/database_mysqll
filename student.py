#Defining function to evaluate student results
def student_performance(*marks, passing_mark=40, **student):
    print("Student Name:", student["name"])
    print("Student ID:", student["id"])
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)
    passed = 0
    failed = 0
#For loop to count passed and failed subjects
    for mark in marks:
        if mark >= passing_mark:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        result = "Pass"
    else:
        result = "Fail"
    print("Total Marks:", total)
    print("Average Marks:", average)
    print("Highest Mark:", highest)
    print("Lowest Mark:", lowest)
    print("Subjects Passed:", passed)
    print("Subjects Failed:", failed)
    print("Final Result:", result)
student_performance(
    41, 65, 92, 35, 80,
    name="Varun",
    id=21
)
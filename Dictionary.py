#Initializing quiz questions with answers
quiz = {
    "What language is used for websites?": {
        "A": "Python",
        "B": "JavaScript",
        "C": "Java",
        "D": "C++",
        "answer": "B"
    },
    "Which language is used for Python programming?": {
        "A": "Python",
        "B": "Java",
        "C": "C++",
        "D": "HTML",
        "answer": "A"
    },
    "How many bits are there in a byte?": {
        "A": "4",
        "B": "16",
        "C": "8",
        "D": "32",
        "answer": "C"
    }
}
score = 0
#For loop to get elements in quiz
for question,option in quiz.items():
    print(question)
    print("A", option["A"])
    print("B", option["B"])
    print("C", option["C"])
    print("D", option["D"])
    print("S Skip Question")
    print("Q Quit Quiz")
    choice = input("Enter your choice: ").upper()

    if choice == "Q":
        print("Quiz Ended Thank you.")
        break
    elif choice == "S":
        print("Question skipped moving to next.")
        continue
    elif choice == option["answer"]:
        print("Correct Answer")
        score += 1
    else:
        print("Wrong Answer")
        score -= 1
print("Final Score:", score)
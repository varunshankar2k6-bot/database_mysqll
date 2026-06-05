#Class Employee defined
class Employee:
    #Function to calculate bonus based on salary and performance
    def calculate_bonus(self, *args):
        if len(args) == 1:
            salary = args[0]
            bonus = salary * 0.10
        elif len(args) == 2:
            salary = args[0]
            performance = args[1]
            if performance == "Excellent":
                bonus = salary * 0.20
            elif performance == "Good":
                bonus = salary * 0.15
            else:
                bonus = salary * 0.05
        return bonus
#Creating object
e= Employee()
print("Bonus:", e.calculate_bonus(5000))
print("Bonus:", e.calculate_bonus(10000, "Average"))
print("Bonus:", e.calculate_bonus(15000, "Good"))
print("Bonus:", e.calculate_bonus(20000, "Excellent"))
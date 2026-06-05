#Class Employee defined
class Employee:
    #Function to calculate bonus based on salary and performance
    def calculate_bonus(self, salary, performance=None):
        if performance is None:
            bonus=salary * 0.10
        elif performance == "Excellent":
            bonus=salary * 0.20
        elif performance == "Good":
            bonus=salary * 0.15
        else:
            bonus= salary * 0.05
        return bonus
#Creating object
e=Employee()
print("Bonus:", e.calculate_bonus(5000))
print("Bonus:", e.calculate_bonus(10000, "Excellent"))
print("Bonus:", e.calculate_bonus(15000, "Good"))
print("Bonus:", e.calculate_bonus(20000, "Average"))
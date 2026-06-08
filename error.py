#Question 1 adding int and string error
try:
    a = 12
    s = "hello"
    print(a + s)
except TypeError:
    print("Cannot add integer and string together convert both variables to same type")



#Question 2 division of two numbers error
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result =", result)
except ValueError:
    print("ERROR: Wrong datatype try again")
except ZeroDivisionError:
    print("ERROR: Division by zero")


#Question 3 string formating
def title(name):
    if not isinstance(name, str):
        raise TypeError("Argument must be a string")
    return name.capitalize()
try:
    print(title("abhishek"))
    print(title(123))
except TypeError as e:
    print(e)

#Question 4 list functions
list1 = [5,4,3,2,1,0]
try:
    index = int(input("Enter index number: "))
    print("Element at the position is ", list1[index])
except ValueError:
    print("Please enter a numeric value within range")
except IndexError:
    print("Index out of range")
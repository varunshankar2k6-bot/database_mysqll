try:
    a = 12
    s = "hello"
    print(a + s)
except TypeError:
    print("Cannot add integer and string together convert both variables to same type")




try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result =", result)
except ValueError:
    print("ERROR: Wrong datatype try again")
except ZeroDivisionError:
    print("ERROR: Division by zero")



def title(name):
    if not isinstance(name, str):
        raise TypeError("Argument must be a string")
    return name.capitalize()
try:
    print(title("abhishek"))
    print(title(123))
except TypeError as e:
    print(e)
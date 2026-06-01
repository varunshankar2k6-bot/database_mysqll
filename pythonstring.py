#Question 1
ip = input("Enter a sentence: ")
print("Uppercase:", ip.upper())
print("Lowercase:", ip.lower())
print("Title Case:", ip.title())
print("Swapcase:", ip.swapcase())

#Question 2
word = "Mississippi"
count = word.lower().count('s')
print("Count of 's':", count)

#Question 3
username = input("Enter username: ")
if (username.startswith("xm_") and
    username.replace("_", "").isalnum() and
    len(username) > 8):
    print("Valid Username")
else:
    print("Invalid Username")

#Question 4
sentence = input("Enter a sentence: ")
result = ""
prev_space = False
for ch in sentence:
    if ch == " ":
        if not prev_space:
            result += ch
        prev_space = True
    else:
        result += ch
        prev_space = False
print(result)

#Question 5
sentence = input("Enter a sentence: ")
words = sentence.split()
s=""
for i in range(len(words)-1, -1, -1):
    s=s+(words[i]+" ")
print(s)

#Question 6
mail=input("Enter your email: ")
s=""
for i in range(len(mail)):
    if mail[i]=="@":
        print(mail[i+1:])

#Question 7
password = input("Enter password: ")
has_upper = False
has_lower = False
has_digit = False
has_special = False
special_chars = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/"
for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in special_chars:
        has_special = True
if (len(password) >= 8 and has_upper and
    has_lower and has_digit and has_special):
    print("Strong Password")
else:
    print("Weak Password")

#Question 8
text = input("Enter a string: ")
c=input("Enter a character to count: ")
count=0
for i in range(len(text)):
    if text[i] == c:
        count = count+1
print(count)

#Question 9
sentence = input("Enter a sentence: ")
words = sentence.split()
words.sort()
print("Second Largest Word:", words[-2])

#Question 10
snake = input("Enter snake case string: ")
words = snake.split("_")
camel = words[0]
for i in range(1, len(words)):
    camel += words[i].capitalize()
print("Camel Case:", camel)


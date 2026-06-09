#Question 1 to print content in sample.txt file using with
with open(r"C:\Users\sample.txt", "r") as file:
    text = file.read()
    print(text)


#Question 2 to print number of words in a file
with open(r"C:\Users\sample.txt", "r") as file:
    text= file.read()
word= text.split()
print("Number of words =", len(word))

#Question 3 to print the text from a random position taken as input from user
with open(r"C:\Users\sample.txt", "r") as file:
    text= file.read()
position = int(input("Enter position"))
if position>=0 & position<len(text):
    print("Data from position ",position," is:       ",text[position:])
else:
    print("Wrong position try again")

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
import random
with open(r"C:\Users\sample.txt", "r") as file:
    file.seek(0, 2)      
    size = file.tell()   
    position = random.randint(0, size - 1)
    file.seek(position)  
    print("Random Position is at ", position)
    print("Text from random position is ")
    print(file.read())

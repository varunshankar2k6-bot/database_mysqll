#Question 1
n=int(input("Enter number"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("Sum of numbers is",sum)

#Question 2
n=int(input("Enter number"))
sum=0
for i in range(1,n+1,2):
    sum=sum+i
print("Sum of numbers is",sum)

#Question 3
n=int(input("Enter number"))
for i in range(1,11):
    print(n," *",i,"=",n*i)

#Question 4
n=int(input("Enter number"))
for i in range(1,11):
    if (i!=10):
        continue
    else:
        print("Done")
    
#Question 5
n=int(input("Enter a number: "))
for i in range(2,n+1):
    count=0
    for j in range(2,i+1):
        if i%j==0:
            count=count+1
    if count==1:
        print(i," is a prime number")

#Question 6        
n=int(input("Enter number"))
if(n>0):
    print("Positive")
elif(n<0):
    print("Negative")
else:
    print("Zero")



#Question 6        
num = int(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")

#Question 7
order=input("Enter order: ")
price=0
match order:
    case "Veg":
        price=100
    case "Chicken":
        price=120
    case "Beef":
        price=150
    case _:
        price=0
        print("Invalid order")
print("Order is ",order," and price is ",price)

#Question 1
list1=[]
for i in range(5):
    list1.append(int(input("Enter a number: ")))
print("The list is: ", list1)

#Question 2
l1=[]
l2=[]
for i in range(5):
    l1.append(int(input("Enter a number in first list: ")))
for i in range(5):
    l2.append(int(input("Enter a number in second list: ")))
l1.extend(l2)
print("Merged list is: ", l1)

#Question 3
l=["V","S","K","A","B"]
l.insert(3,"Z")
print(l)

#Question 4
l=[1,1,2,3,4,5,2,3,4,2,2,3]
n=int(input("Enter a number to remove: "))
l.remove(n)
print(l)    

#Question 5
l=[1,1,2,3,4,5,2,3,4,2,2,3]
l.pop()
print(l)

#Question 6
l=[1,1,2,3,4,5,2,3,4,2,2,3]
n=int(input("Enter a number to find index: "))
print("Index of ", n, " is: ", l.index(n))

#Question 7
l=[1,1,2,3,4,5,2,3,4,2,2,3]
n=int(input("Enter a number to find frequency: "))
print("Frequency of ", n, " is: ", l.count(n))

#Question 8
l=[1,1,2,3,4,5,2,3,4,2,2,3]
new=l.copy()
new.append(7)
new.append(8)
new.pop(1)
print("Original list: ", l)
print("Copy list: ", new)

#Question 9
employee = [1, "Varun", 20000, ["Python", "Java","SQL"]]
print("Employee ID:", employee[0])
print("Name:", employee[1])
print("Salary:", employee[2])
print("Skills:", employee[3])
employee[3].append("IDE")
print("FinalSkills:", employee[3])
memberset1=set()
memberset2=set()
#Question 1
#Adding elements to set1
memberset1.add("V")
memberset1.update("A","B","Z")
#Question 2
print(memberset1)
#Question 3 Removing elements
memberset1.remove("A")
print(memberset1)
#Adding elements to set2
memberset2.update("Z","Y","V","X")
print(memberset2)
#Question 4 finding common elements between two sets
memberset3=memberset1.intersection(memberset2)
print("Common members ", memberset3)
#Question 5 Finding common elements between two sets
m3=memberset1.union(memberset2)
print("Merge libraries is: ", m3)
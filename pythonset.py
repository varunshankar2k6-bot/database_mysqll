m1=set()
m2=set()
#Question 1
m1.add("V")
m1.update("A","B","Z")
#Question 2
print(m1)
#Question 3
m1.remove("A")
print(m1)
m2.update("Z","Y","V","X")
print(m2)
#Question 4
m3=m1.intersection(m2)
print("Common members ", m3)
#Question 5
m3=m1.union(m2)
print("Merge libraries is: ", m3)
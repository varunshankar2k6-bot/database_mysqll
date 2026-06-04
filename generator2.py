pages = [
    ["Rahul", "Anu"],
    ["John", "Priya"],
    ["Arun", "Meera"]
]
def name_seperator():
    #For loop to get the 3 lists
    for i in pages:
        #For loop to get the internal elements of the list
        for j in i:
            yield j
gen = name_seperator()
#6 next() calls to get the 6 names from the lists
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
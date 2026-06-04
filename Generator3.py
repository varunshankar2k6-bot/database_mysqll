nums = [1,2,3,15,11,21,25,31]
def prime(data):
    for num in data:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                yield num
for i in prime(nums):
    print(i)



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
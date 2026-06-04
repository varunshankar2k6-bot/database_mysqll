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
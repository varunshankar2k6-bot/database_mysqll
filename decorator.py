#Importing time module for time calculation
import time
def timer(func):
    def wrapper():
#Start and end to calculate starting and end timings
        start = time.time()
        func()
        end = time.time()
#Time taken=end-start
        print("Execution Time:", end - start)
    return wrapper

#Timer decorated function
@timer
def display():
    for i in range(11):
        continue
    print("Hello World")
display()
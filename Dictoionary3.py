#Defining dictionary
user = {
    "id": 1,
    "name": "Rahul",
    "email": "rahul@gmail.com",
    "address": {
        "city": "Kochi",
        "state": "Kerala"
    }
}
#Question 1 getting name
name=user.get("name")
print("Username is :",name)
#Question 2 getting city
city=user.get("address", {}).get("city")
print("User city is :",city)
#Question 3 updating email
user["email"]="rahulnew@gmail.com"
print("Updated email is :",user["email"])
#Question 4 adding phone number
user["phone"]="1234567890"
print("User phone is :",user["phone"])
#Question 5 deleting key
del user["address"]["state"]
print("User address after deleting key is:",user)
#Question 6 checking key existence
key=input("Enter key to check: ")
if key in user:
    print("Key exists in the dictionary")
else:
    print("Key does not exist in the dictionary")
#Question 7 displaying all keys as list
keylist=list(user.keys())
print("Key dictionary is:",keylist)
#Question 8 displaying all values key pairs
print("Value dictionary is:",user.items())

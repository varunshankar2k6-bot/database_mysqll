user = {
    "id": 1,
    "name": "Rahul",
    "email": "rahul@gmail.com",
    "address": {
        "city": "Kochi",
        "state": "Kerala"
    }
}
name=user.get("name")
print("Username is :",name)
city=user.get("address", {}).get("city")
print("User city is :",city)
user["email"]="rahulnew@gmail.com"
print("Updated email is :",user["email"])
user["phone"]="1234567890"
print("User phone is :",user["phone"])
del user["address"]["state"]
print("User address after deleting key is:",user)
key=input("Enter key to check: ")
if key in user:
    print("Key exists in the dictionary")
else:
    print("Key does not exist in the dictionary")
keylist=list(user.keys())
print("Key dictionary is:",keylist)
print("Value dictionary is:",user.items())

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

users = response.json()

print(users)

for user in users:
    print("ID:",user["ID"])
    print("Name:",user["Name"])
    print("Email:",users["email"])
    print("City:",users["address"]["City"])
    print("-------------------------------")



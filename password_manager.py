import json
import base64
import os

FILE = "passwords.json"

def load_data():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def encode(text):
    return base64.b64encode(text.encode()).decode()

def decode(text):
    return base64.b64decode(text.encode()).decode()

data = load_data()

while True:
    print("\n1. Add password\n2. Show passwords\n3. Exit")
    choice = input("Choice: ")

    if choice == "1":
        site = input("Website: ")
        login = input("Login: ")
        password = input("Password: ")
        data[site] = {
            "login": encode(login),
            "password": encode(password)
        }
        save_data(data)
        print("Saved!")

    elif choice == "2":
        if not data:
            print("No passwords saved.")
        else:
            for site, info in data.items():
                print(f"\nSite: {site}")
                print("Login:", decode(info["login"]))
                print("Password:", decode(info["password"]))

    elif choice == "3":
        break

    else:
        print("Error!")

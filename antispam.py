import time

reports = {}
banned = set()

def report(user):
    now = time.time()
    if user not in reports:
        reports[user] = []

    reports[user] = [t for t in reports[user] if now - t < 60]

    reports[user].append(now)

    if len(reports[user]) >= 5:
        banned.add(user)
        print(f"{user} has been banned!")
    else:
        print(f"Report added. ({len(reports[user])}/5 before ban)")

while True:
    print("\n1. Report user\n2. Check status\n3. Exit")
    choice = input("Choice: ")

    if choice == "1":
        user = input("User: ")
        report(user)

    elif choice == "2":
        user = input("User: ")
        if user in banned:
            print(f"{user} is banned.")
        else:
            print(f"{user} is not banned.")

    elif choice == "3":
        break

    else:
        print("Error!")

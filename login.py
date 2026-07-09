import time
import getpass
print("===== Secure Login System =====")

users = {}

with open("users.txt", "r") as file:
    for line in file:
        username, password = line.strip().split(":")
        users[username] = password
        
max_attempts = 3
attempts = 0

while attempts < max_attempts:

    username = input("Enter Username: ")
    password = getpass.getpass("Enter Password: ")

    if username in users and users[username] == password:
        print("Login Successful!")
        print("Welcome", username)
        break

    else:
        attempts = attempts + 1
        remaining = max_attempts - attempts

        print("Invalid Username or Password")
        print("Attempts Left:", remaining)
        
        with open("login_log.txt", "a") as file:
            file.write(f"Failed login for username: {username}\n")

if attempts == max_attempts:
    print("Too many failed attempts!")
    print("System Locked for 5 seconds...")

    time.sleep(5)

    print("Try Again Later")
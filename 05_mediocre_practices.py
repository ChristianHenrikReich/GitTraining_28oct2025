"""
Mediocre Code Practices - File 5/10
This file demonstrates mediocre coding with several style and structure issues.
"""

# Mixed imports (some unused)
import os
import sys
import random
import time
import json
from datetime import datetime

# Global variables everywhere
users = []
current_user = None
settings = {"theme": "dark", "language": "en"}
data_file = "users.txt"

class user:  # Wrong naming convention
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.created_at = datetime.now()
        self.login_count = 0
        
    def login(self):
        self.login_count += 1
        print("User logged in")
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Login count: {self.login_count}")

# Functions with poor naming and structure
def loadUsers():  # Wrong naming convention
    global users
    try:
        with open(data_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    u = user(parts[0], int(parts[1]), parts[2])
                    users.append(u)
    except:
        pass  # Silent failure - bad practice

def saveUsers():
    global users
    with open(data_file, 'w') as f:
        for u in users:
            f.write(f"{u.name},{u.age},{u.email}\n")

def addUser():
    global users
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    
    # No validation
    u = user(name, int(age), email)
    users.append(u)
    print("User added!")

def findUser():
    global users
    name = input("Enter name to search: ")
    for u in users:
        if u.name == name:
            u.display()
            return u
    print("User not found")
    return None

def deleteUser():
    global users
    name = input("Enter name to delete: ")
    for i in range(len(users)):
        if users[i].name == name:
            del users[i]
            print("User deleted")
            return
    print("User not found")

def listUsers():
    global users
    if len(users) == 0:
        print("No users")
    else:
        for u in users:
            print(f"{u.name} - {u.age} - {u.email}")

# Long function with multiple responsibilities
def userMenu():
    global current_user
    while True:
        print("\n1. Add User")
        print("2. Find User")
        print("3. List Users")
        print("4. Delete User")
        print("5. Login User")
        print("6. Change Settings")
        print("7. Generate Random Users")
        print("8. Export to JSON")
        print("9. Statistics")
        print("10. Exit")
        
        choice = input("Choice: ")
        
        if choice == "1":
            addUser()
        elif choice == "2":
            findUser()
        elif choice == "3":
            listUsers()
        elif choice == "4":
            deleteUser()
        elif choice == "5":
            u = findUser()
            if u:
                u.login()
                current_user = u
        elif choice == "6":
            # Inline settings change
            theme = input("Theme (light/dark): ")
            lang = input("Language (en/es/fr): ")
            settings["theme"] = theme
            settings["language"] = lang
            print("Settings updated")
        elif choice == "7":
            # Generate random users inline
            names = ["John", "Jane", "Bob", "Alice", "Charlie", "Diana"]
            for i in range(5):
                name = random.choice(names) + str(random.randint(1, 100))
                age = random.randint(18, 80)
                email = f"{name.lower()}@email.com"
                u = user(name, age, email)
                users.append(u)
            print("Random users generated")
        elif choice == "8":
            # Export to JSON inline
            data = []
            for u in users:
                data.append({
                    "name": u.name,
                    "age": u.age,
                    "email": u.email,
                    "login_count": u.login_count
                })
            with open("users.json", "w") as f:
                json.dump(data, f)
            print("Exported to JSON")
        elif choice == "9":
            # Statistics calculation inline
            if len(users) > 0:
                ages = [u.age for u in users]
                avg_age = sum(ages) / len(ages)
                total_logins = sum([u.login_count for u in users])
                print(f"Total users: {len(users)}")
                print(f"Average age: {avg_age:.1f}")
                print(f"Total logins: {total_logins}")
            else:
                print("No users for statistics")
        elif choice == "10":
            saveUsers()
            break
        else:
            print("Invalid choice")

# Function with magic numbers and hardcoded values
def backup_data():
    import shutil
    timestamp = str(int(time.time()))
    backup_name = f"backup_{timestamp}.txt"
    shutil.copy(data_file, backup_name)
    print(f"Backup created: {backup_name}")
    
    # Clean old backups (hardcoded to keep only 5)
    backups = [f for f in os.listdir('.') if f.startswith('backup_')]
    if len(backups) > 5:
        backups.sort()
        for old_backup in backups[:-5]:
            os.remove(old_backup)

# Poor error handling
def import_from_csv():
    try:
        filename = input("CSV filename: ")
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines[1:]:  # Skip header
                parts = line.strip().split(',')
                u = user(parts[0], int(parts[1]), parts[2])
                users.append(u)
        print("Import successful")
    except:
        print("Import failed")

# Main function doing too much
def main():
    global users, settings
    
    print("User Management System v1.0")
    print("Loading users...")
    loadUsers()
    
    # Hardcoded initial settings
    if len(users) == 0:
        print("No users found, creating sample data...")
        sample_users = [
            user("Admin", 30, "admin@system.com"),
            user("Test User", 25, "test@example.com")
        ]
        users.extend(sample_users)
    
    # Display current settings
    print(f"Current theme: {settings['theme']}")
    print(f"Current language: {settings['language']}")
    
    while True:
        print("\nMain Menu:")
        print("1. User Management")
        print("2. Backup Data")
        print("3. Import CSV")
        print("4. Exit")
        
        choice = input("Choice: ")
        
        if choice == "1":
            userMenu()
        elif choice == "2":
            backup_data()
        elif choice == "3":
            import_from_csv()
        elif choice == "4":
            print("Saving and exiting...")
            saveUsers()
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
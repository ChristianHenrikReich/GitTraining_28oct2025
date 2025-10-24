"""
Below Average Code - File 6/10
This file shows below average code with poor structure and many bad practices.
"""

import random
import os
import sys
import time
import json

# Global variables with poor names
l = []  # users list
c = None  # current user
d = {}  # data dictionary 
f = "data.txt"  # filename

class Person:  # inconsistent with rest of code
    def __init__(self, n, a, e):  # single letter parameters
        self.n = n
        self.a = a
        self.e = e
        self.t = time.time()  # unclear variable name
        self.x = 0  # what is x?
        
    def do_something(self):  # vague method name
        self.x = self.x + 1
        print("done")
        
    def show(self):
        print(self.n, self.a, self.e, self.x)

def load():  # too generic name
    global l
    try:
        f = open("data.txt", "r")
        data = f.read()
        f.close()
        lines = data.split("\n")
        for line in lines:
            if line:
                parts = line.split(",")
                p = Person(parts[0], parts[1], parts[2])
                l.append(p)
    except:
        print("error")

def save():
    global l
    f = open("data.txt", "w")
    for p in l:
        f.write(p.n + "," + p.a + "," + p.e + "\n")
    f.close()

def add():
    global l
    n = input("name: ")
    a = input("age: ")
    e = input("email: ")
    p = Person(n, a, e)
    l.append(p)

def find():
    global l
    n = input("name: ")
    for p in l:
        if p.n == n:
            p.show()
            return p

def delete():
    global l
    n = input("name: ")
    i = 0
    while i < len(l):
        if l[i].n == n:
            del l[i]
            print("deleted")
            return
        i = i + 1

def list_all():
    global l
    for p in l:
        print(p.n + " " + p.a + " " + p.e)

# Extremely long function with everything mixed together
def menu():
    global l, c, d
    while True:
        print("1. add")
        print("2. find") 
        print("3. list")
        print("4. delete")
        print("5. random")
        print("6. stats")
        print("7. exit")
        
        x = input("> ")  # poor variable name
        
        if x == "1":
            add()
        elif x == "2":
            find()
        elif x == "3":
            list_all()
        elif x == "4":
            delete()
        elif x == "5":
            # Inline random generation without any structure
            names = ["a", "b", "c", "d", "e"]
            for i in range(10):
                n = names[random.randint(0, 4)] + str(i)
                a = str(random.randint(20, 50))
                e = n + "@test.com"
                p = Person(n, a, e)
                l.append(p)
            print("added random")
        elif x == "6":
            # Inline statistics without proper calculation
            total = 0
            count = 0
            for p in l:
                total = total + int(p.a)
                count = count + 1
            if count > 0:
                avg = total / count
                print("avg age: " + str(avg))
            else:
                print("no data")
        elif x == "7":
            save()
            break

# Functions with side effects and poor naming
def process_data():
    global l, d
    d["count"] = len(l)
    d["total"] = 0
    for p in l:
        d["total"] = d["total"] + int(p.a)
    print("processed")

def do_backup():
    import shutil
    shutil.copy("data.txt", "backup.txt")
    print("backup done")

def cleanup():
    global l
    # Remove duplicates in a very inefficient way
    new_list = []
    for p in l:
        found = False
        for existing in new_list:
            if existing.n == p.n:
                found = True
                break
        if not found:
            new_list.append(p)
    l = new_list

# Poor validation function
def validate(data):
    if data == "":
        return False
    if data == None:
        return False
    return True

# Function with hardcoded values and magic numbers
def generate_report():
    global l
    print("=== REPORT ===")
    print("Total users: " + str(len(l)))
    
    # Hardcoded age categories
    young = 0
    middle = 0
    old = 0
    
    for p in l:
        age = int(p.a)
        if age < 30:
            young = young + 1
        elif age < 50:
            middle = middle + 1
        else:
            old = old + 1
    
    print("Young (< 30): " + str(young))
    print("Middle (30-49): " + str(middle))
    print("Old (50+): " + str(old))

# Poor error handling and resource management
def import_data():
    global l
    try:
        filename = input("file: ")
        f = open(filename, "r")  # No proper file closing
        data = f.read()
        lines = data.split("\n")
        for line in lines:
            if "," in line:
                parts = line.split(",")
                if len(parts) == 3:
                    p = Person(parts[0], parts[1], parts[2])
                    l.append(p)
        print("imported")
    except:
        print("failed")  # Generic error message

def main():
    global l, c, d
    print("System Starting...")
    load()
    
    # Hardcoded sample data
    if len(l) == 0:
        p1 = Person("admin", "25", "admin@test.com")
        p2 = Person("user", "30", "user@test.com")
        l.append(p1)
        l.append(p2)
    
    while True:
        print("\nMAIN:")
        print("1. menu")
        print("2. process")
        print("3. backup")
        print("4. cleanup")
        print("5. report")
        print("6. import")
        print("7. quit")
        
        choice = input("> ")
        
        if choice == "1":
            menu()
        elif choice == "2":
            process_data()
        elif choice == "3":
            do_backup()
        elif choice == "4":
            cleanup()
        elif choice == "5":
            generate_report()
        elif choice == "6":
            import_data()
        elif choice == "7":
            save()
            print("bye")
            break

if __name__ == "__main__":
    main()
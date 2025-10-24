"""
Poor Code Practices - File 7/10
This file demonstrates poor coding with many anti-patterns and bad practices.
"""

# Massive imports, many unused
import os, sys, time, random, json, math, datetime, re, csv, urllib, socket
from random import *
from time import *
from os import *

# Too many global variables with terrible names
data = []
stuff = {}
things = []
temp = None
x = 0
y = 0
z = 0
flag = False
counter = 0
result = ""

class thing:  # terrible class name
    def __init__(self, a, b, c, d, e):  # too many single-letter params
        self.a = a
        self.b = b
        self.c = c
        self.d = d  
        self.e = e
        self.f = 0
        self.g = []
        self.h = {}
        
    def func1(self):  # meaningless function names
        self.f += 1
        
    def func2(self, val):
        self.g.append(val)
        
    def func3(self):
        return self.f > 5

# Extremely long function doing way too much
def big_function():
    global data, stuff, things, temp, x, y, z, flag, counter, result
    
    print("starting...")
    
    # Inline file reading without proper error handling
    try:
        file = open("file.txt", "r")
        content = file.read()
        file.close()
    except:
        content = ""
    
    # Parse data in a terrible way
    lines = content.split("\n")
    for line in lines:
        if line != "":
            parts = line.split(",")
            if len(parts) > 3:
                obj = thing(parts[0], parts[1], parts[2], parts[3], parts[4] if len(parts) > 4 else "")
                data.append(obj)
    
    # Some random processing
    for item in data:
        item.func1()
        if item.a == "special":
            item.func2("important")
            flag = True
        
        # Nested conditions getting deeper
        if item.b != "":
            if len(item.b) > 5:
                if item.c.isdigit():
                    val = int(item.c)
                    if val > 10:
                        if val < 100:
                            counter += 1
                            if counter % 2 == 0:
                                things.append(item)
                                if len(things) > 10:
                                    print("too many things")
    
    # More inline processing
    x = len(data)
    y = len(things)
    z = counter
    
    # Terrible string building
    result = "Results: "
    result = result + "Total: " + str(x) + ", "
    result = result + "Things: " + str(y) + ", "
    result = result + "Counter: " + str(z)
    
    # Random calculations mixed in
    if x > 0:
        avg = 0
        total = 0
        for item in data:
            if item.c.isdigit():
                total += int(item.c)
        avg = total / x
        result = result + ", Avg: " + str(avg)
    
    # More file operations without proper handling
    try:
        output_file = open("output.txt", "w")
        output_file.write(result)
        output_file.close()
    except:
        pass
    
    return result

# Function with side effects everywhere
def process():
    global data, stuff, x, y, z
    
    # Modify global state unpredictably
    x = x + 1
    y = y * 2
    z = random.randint(1, 100)
    
    # Create random data
    for i in range(10):
        name = "item" + str(i)
        value = str(random.randint(1, 1000))
        category = choice(["A", "B", "C", "D"])
        priority = choice(["low", "high", "medium"])
        status = choice(["active", "inactive"])
        
        obj = thing(name, value, category, priority, status)
        data.append(obj)
    
    # Modify existing data
    for item in data:
        if random.random() > 0.5:
            item.func1()
            item.func2(str(random.randint(1, 100)))
    
    print("processed " + str(len(data)) + " items")

# Terrible input validation
def get_input():
    while True:
        try:
            choice = input("Enter choice: ")
            if choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                return choice
            else:
                print("bad input")
        except:
            print("error")

# No separation of concerns - everything mixed together
def menu_system():
    global data, stuff, things, temp, x, y, z, flag
    
    while True:
        print("\n" + "="*50)
        print("MAIN MENU")
        print("="*50)
        print("1. Load Data")
        print("2. Process Data") 
        print("3. Generate Random")
        print("4. Show Stats")
        print("5. Save Everything")
        print("6. Clean Data")
        print("7. Export")
        print("8. Backup")
        print("9. Exit")
        
        choice = get_input()
        
        if choice == "1":
            result = big_function()
            print(result)
            
        elif choice == "2":
            process()
            
        elif choice == "3":
            # Inline random generation with hardcoded values
            count = 50  # magic number
            for i in range(count):
                a = "gen_" + str(i)
                b = str(random.randint(100, 999))
                c = str(random.randint(1, 100))
                d = choice(["type1", "type2", "type3"])
                e = choice(["status1", "status2"])
                
                new_thing = thing(a, b, c, d, e)
                data.append(new_thing)
            
            print("generated " + str(count) + " items")
            
        elif choice == "4":
            # Inline statistics with no organization
            total_items = len(data)
            print("Total items: " + str(total_items))
            
            if total_items > 0:
                # Count categories
                cat_a = 0
                cat_b = 0  
                cat_c = 0
                cat_d = 0
                
                for item in data:
                    if item.c == "A":
                        cat_a += 1
                    elif item.c == "B":
                        cat_b += 1
                    elif item.c == "C":
                        cat_c += 1
                    elif item.c == "D":
                        cat_d += 1
                
                print("Category A: " + str(cat_a))
                print("Category B: " + str(cat_b))
                print("Category C: " + str(cat_c))
                print("Category D: " + str(cat_d))
                
                # Calculate averages in a terrible way
                total_val = 0
                count_val = 0
                for item in data:
                    try:
                        val = int(item.b)
                        total_val += val
                        count_val += 1
                    except:
                        pass
                
                if count_val > 0:
                    avg = total_val / count_val
                    print("Average value: " + str(avg))
            
        elif choice == "5":
            # Save everything to multiple files
            try:
                main_file = open("main_data.txt", "w")
                for item in data:
                    main_file.write(item.a + "," + item.b + "," + item.c + "," + item.d + "," + item.e + "\n")
                main_file.close()
                
                stats_file = open("stats.txt", "w")
                stats_file.write("Total: " + str(len(data)) + "\n")
                stats_file.write("X: " + str(x) + "\n")
                stats_file.write("Y: " + str(y) + "\n")
                stats_file.write("Z: " + str(z) + "\n")
                stats_file.close()
                
                print("saved")
            except:
                print("save failed")
                
        elif choice == "6":
            # Terrible data cleaning
            original_count = len(data)
            
            # Remove duplicates inefficiently
            cleaned = []
            for item in data:
                found = False
                for existing in cleaned:
                    if existing.a == item.a and existing.b == item.b:
                        found = True
                        break
                if not found:
                    cleaned.append(item)
            
            data = cleaned
            print("cleaned: removed " + str(original_count - len(data)) + " duplicates")
            
        elif choice == "7":
            # Export in multiple formats without structure
            try:
                json_data = []
                for item in data:
                    json_data.append({
                        "a": item.a,
                        "b": item.b, 
                        "c": item.c,
                        "d": item.d,
                        "e": item.e,
                        "f": item.f
                    })
                
                json_file = open("export.json", "w")
                json.dump(json_data, json_file)
                json_file.close()
                
                csv_file = open("export.csv", "w")
                csv_file.write("a,b,c,d,e,f\n")
                for item in data:
                    csv_file.write(item.a + "," + item.b + "," + item.c + "," + item.d + "," + item.e + "," + str(item.f) + "\n")
                csv_file.close()
                
                print("exported to json and csv")
            except:
                print("export failed")
                
        elif choice == "8":
            # Backup with timestamp
            timestamp = str(int(time()))
            backup_name = "backup_" + timestamp + ".txt"
            
            try:
                import shutil
                shutil.copy("main_data.txt", backup_name)
                print("backup created: " + backup_name)
            except:
                print("backup failed")
                
        elif choice == "9":
            print("exiting...")
            break

# Main function with initialization problems
def main():
    global data, stuff, things, x, y, z, flag
    
    print("Starting System...")
    
    # Initialize with random values
    x = random.randint(1, 10)
    y = random.randint(10, 20)
    z = 0
    flag = False
    
    # Create some initial data
    for i in range(5):
        obj = thing("init_" + str(i), str(i*10), "init", "normal", "active")
        data.append(obj)
    
    menu_system()
    
    print("System stopped.")

if __name__ == "__main__":
    main()
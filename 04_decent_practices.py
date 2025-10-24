"""
Decent Code Practices - File 4/10
This file shows decent code with some inconsistencies and missing best practices.
"""

import math

class calculator:  # class name should be capitalized
    def __init__(self):
        self.memory = 0
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        if b != 0:
            result = a / b
            self.history.append(f"{a} / {b} = {result}")
            return result
        else:
            print("Error: Division by zero!")
            return None
    
    def power(self, base, exponent):
        result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result
    
    def sqrt(self, number):
        if number >= 0:
            result = math.sqrt(number)
            self.history.append(f"sqrt({number}) = {result}")
            return result
        else:
            print("Error: Cannot calculate square root of negative number!")
            return None
    
    def store_memory(self, value):
        self.memory = value
        print(f"Stored {value} in memory")
    
    def recall_memory(self):
        return self.memory
    
    def clear_memory(self):
        self.memory = 0
    
    def clear_history(self):
        self.history = []
    
    def show_history(self):
        if len(self.history) > 0:
            print("Calculation History:")
            for calculation in self.history:
                print(f"  {calculation}")
        else:
            print("No calculations in history")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Please enter a valid number")


def main():
    calc = calculator()
    
    print("Simple Calculator")
    print("Available operations:")
    print("1. Addition")
    print("2. Subtraction") 
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Memory Store")
    print("8. Memory Recall")
    print("9. Memory Clear")
    print("10. Show History")
    print("11. Clear History")
    print("12. Exit")
    
    while True:
        choice = input("\nEnter operation number: ")
        
        if choice == "1":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = calc.add(a, b)
            print(f"Result: {result}")
        
        elif choice == "2":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = calc.subtract(a, b)
            print(f"Result: {result}")
        
        elif choice == "3":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = calc.multiply(a, b)
            print(f"Result: {result}")
        
        elif choice == "4":
            a = get_number("Enter dividend: ")
            b = get_number("Enter divisor: ")
            result = calc.divide(a, b)
            if result is not None:
                print(f"Result: {result}")
        
        elif choice == "5":
            base = get_number("Enter base: ")
            exp = get_number("Enter exponent: ")
            result = calc.power(base, exp)
            print(f"Result: {result}")
        
        elif choice == "6":
            num = get_number("Enter number: ")
            result = calc.sqrt(num)
            if result is not None:
                print(f"Result: {result}")
        
        elif choice == "7":
            value = get_number("Enter value to store: ")
            calc.store_memory(value)
        
        elif choice == "8":
            memory_value = calc.recall_memory()
            print(f"Memory value: {memory_value}")
        
        elif choice == "9":
            calc.clear_memory()
            print("Memory cleared")
        
        elif choice == "10":
            calc.show_history()
        
        elif choice == "11":
            calc.clear_history()
            print("History cleared")
        
        elif choice == "12":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again")


# Some utility functions with inconsistent naming
def convertToPercent(decimal):
    return decimal * 100

def convert_to_decimal(percent):
    return percent / 100

def Calculate_factorial(n):  # Mixed naming convention
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            sequence.append(sequence[i-1] + sequence[i-2])
        return sequence

# Global variable (not ideal)
PI = 3.14159

def circle_area(radius):
    return PI * radius ** 2

def circle_circumference(radius):
    return 2 * PI * radius


if __name__ == "__main__":
    main()
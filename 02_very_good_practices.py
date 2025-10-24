"""
Very Good Code Practices - File 2/10
This file demonstrates very good Python coding with minor areas for improvement.
"""

from typing import List, Dict
import json
import os


class User:
    """User class with good practices but could use dataclasses."""
    
    def __init__(self, username: str, email: str, age: int):
        self.username = username
        self.email = email
        self.age = age
        self.is_active = True
    
    def deactivate(self):
        """Deactivate the user account."""
        self.is_active = False
    
    def to_dict(self) -> Dict:
        """Convert user to dictionary."""
        return {
            'username': self.username,
            'email': self.email,
            'age': self.age,
            'is_active': self.is_active
        }
    
    def __str__(self) -> str:
        return f"User(username='{self.username}', email='{self.email}')"


class UserRepository:
    """Repository for managing users with good separation of concerns."""
    
    def __init__(self, data_file: str = "users.json"):
        self.data_file = data_file
        self.users: List[User] = []
        self.load_users()
    
    def load_users(self):
        """Load users from file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    data = json.load(file)
                    for user_data in data:
                        user = User(
                            user_data['username'],
                            user_data['email'],
                            user_data['age']
                        )
                        user.is_active = user_data.get('is_active', True)
                        self.users.append(user)
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error loading users: {e}")
    
    def save_users(self):
        """Save users to file."""
        try:
            with open(self.data_file, 'w') as file:
                user_data = [user.to_dict() for user in self.users]
                json.dump(user_data, file, indent=2)
        except IOError as e:
            print(f"Error saving users: {e}")
    
    def add_user(self, user: User) -> bool:
        """Add a new user."""
        if self.find_user_by_username(user.username):
            print(f"User {user.username} already exists")
            return False
        
        self.users.append(user)
        self.save_users()
        return True
    
    def find_user_by_username(self, username: str) -> User:
        """Find user by username."""
        for user in self.users:
            if user.username == username:
                return user
        return None
    
    def get_active_users(self) -> List[User]:
        """Get all active users."""
        return [user for user in self.users if user.is_active]
    
    def get_users_by_age_range(self, min_age: int, max_age: int) -> List[User]:
        """Get users within age range."""
        return [
            user for user in self.users 
            if min_age <= user.age <= max_age
        ]


def validate_email(email: str) -> bool:
    """Enhanced email validation with regex."""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def create_user_interactive():
    """Create user through interactive input."""
    print("Creating new user...")
    
    username = input("Enter username: ").strip()
    if not username:
        print("Username cannot be empty")
        return None
    
    email = input("Enter email: ").strip()
    if not validate_email(email):
        print("Invalid email format")
        return None
    
    try:
        age = int(input("Enter age: "))
        if age < 0 or age > 150:
            print("Invalid age")
            return None
    except ValueError:
        print("Age must be a number")
        return None
    
    return User(username, email, age)


def main():
    """Main function with good structure."""
    repo = UserRepository()
    
    while True:
        print("\n=== User Management System ===")
        print("1. Add user")
        print("2. List active users")
        print("3. Find user")
        print("4. Users by age range")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == '1':
            user = create_user_interactive()
            if user:
                if repo.add_user(user):
                    print(f"User {user.username} added successfully")
        
        elif choice == '2':
            active_users = repo.get_active_users()
            if active_users:
                print("\nActive users:")
                for user in active_users:
                    print(f"  {user}")
            else:
                print("No active users found")
        
        elif choice == '3':
            username = input("Enter username to search: ").strip()
            user = repo.find_user_by_username(username)
            if user:
                print(f"Found: {user}")
            else:
                print("User not found")
        
        elif choice == '4':
            try:
                min_age = int(input("Enter minimum age: "))
                max_age = int(input("Enter maximum age: "))
                users = repo.get_users_by_age_range(min_age, max_age)
                
                if users:
                    print(f"\nUsers aged {min_age}-{max_age}:")
                    for user in users:
                        print(f"  {user}")
                else:
                    print("No users found in that age range")
            except ValueError:
                print("Please enter valid numbers for age")
        
        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again")


if __name__ == "__main__":
    main()
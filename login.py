class User:
    """A class to represent a user."""
    
    def __init__(self, first_name, last_name):
        """Initialize the user with first and last name."""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"User: {self.first_name.title()} {self.last_name.title()}")
    
    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")
    
    def increment_login_attempts(self):
        """Increment the login_attempts by 1."""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


# Create an instance of the User class
user1 = User("arthur", "johnson")

# Call increment_login_attempts() several times
print("Incrementing login attempts...")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# Print the value of login_attempts
print(f"Login attempts after incrementing: {user1.login_attempts}")

# Reset login_attempts
print("\nResetting login attempts...")
user1.reset_login_attempts()

# Print login_attempts again
print(f"Login attempts after reset: {user1.login_attempts}")

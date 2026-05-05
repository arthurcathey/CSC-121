"""Demonstration of the Employee class."""
from employee import Employee


# Create an employee
employee1 = Employee("John", "Doe", 50000)
print(f"Employee: {employee1.first_name} {employee1.last_name}")
print(f"Starting salary: ${employee1.annual_salary:,}\n")

# Test default raise
print("Giving default raise of $5,000...")
employee1.give_raise()
print(f"New salary: ${employee1.annual_salary:,}\n")

# Test custom raise
print("Giving custom raise of $10,000...")
employee1.give_raise(10000)
print(f"New salary: ${employee1.annual_salary:,}\n")

# Create another employee
employee2 = Employee("Jane", "Smith", 60000)
print(f"Employee: {employee2.first_name} {employee2.last_name}")
print(f"Starting salary: ${employee2.annual_salary:,}")
print("Giving custom raise of $8,000...")
employee2.give_raise(8000)
print(f"New salary: ${employee2.annual_salary:,}")

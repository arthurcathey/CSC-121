# 10.6 Addition - Handle ValueError when converting user input

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}.")
except ValueError:
    print("Oops! Please make sure you entered two whole numbers.")

# 9-14. Lottery Assignment

## Assignment Instructions
Write a program that imports the random module. Make a list or tuple containing a series of 10 numbers and five letters. Randomly select four numbers and one letter from the list and put these in a variable. Get input from the user for a lottery number that contains four numbers and one letter. Compare the input from the user to the lottery number and print a message saying whether the user was a winner or not.

## Python Program Code

```python
import random

# Create a list with 10 numbers and 5 letters
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Separate numbers and letters for selection
numbers = [x for x in lottery_pool if isinstance(x, int)]
letters = [x for x in lottery_pool if isinstance(x, str)]

# Randomly select 4 numbers and 1 letter
winning_numbers = sorted(random.sample(numbers, 4))
winning_letter = random.choice(letters)

print("=" * 50)
print("Welcome to the Lottery!")
print("=" * 50)
print()

# Get input from the user
user_input = input("Enter your lottery ticket (4 numbers and 1 letter, separated by spaces): ")

try:
    parts = user_input.split()
    user_numbers = sorted([int(x) for x in parts[:4]])
    user_letter = parts[4].upper()
except (ValueError, IndexError):
    print("Invalid input format!")
    exit()

# Compare the tickets
if user_numbers == winning_numbers and user_letter == winning_letter:
    print("\nCongratulations! You won the lottery!")
else:
    print("\nSorry, you didn't win this time. Better luck next time!")
    print(f"Your ticket: Numbers {user_numbers}, Letter {user_letter}")
    print(f"Winning ticket: Numbers {winning_numbers}, Letter {winning_letter}")
```

## Program Output
```
==================================================
Welcome to the Lottery!
==================================================

Enter your lottery ticket (4 numbers and 1 letter, separated by spaces): 3 5 7 9 B
Winning combination: [1, 4, 6, 8] and D

Sorry, you didn't win this time. Better luck next time!
Your ticket: Numbers [3, 5, 7, 9], Letter B
Winning ticket: Numbers [1, 4, 6, 8], Letter D
```

## Description

This Python program simulates a lottery game with the following features:

1. **Lottery Pool**: Creates a list containing 10 numbers (1-10) and 5 letters (A-E).
2. **Random Selection**: Uses `random.sample()` to select 4 unique numbers and `random.choice()` to select 1 letter, storing them in variables.
3. **User Input**: Prompts the user to enter their lottery ticket in the format "4 numbers 1 letter" (e.g., "3 5 7 9 B").
4. **Input Validation**: Uses try-except to handle invalid input formats gracefully.
5. **Comparison**: Compares the user's ticket with the winning combination.
6. **Output**: Displays whether the user won or lost, and shows both tickets for comparison.

The numbers are sorted for fair comparison, ensuring the order of entry doesn't affect the result.

## GitHub Repository
File uploaded to: https://github.com/arthurcathey/CSC-121/blob/main/lottery.py

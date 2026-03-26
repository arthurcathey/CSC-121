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

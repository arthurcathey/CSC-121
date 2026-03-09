# Movie Theater Assignment

## Assignment Instructions
Write a program for a movie theater that charges different ticket prices depending on a person's age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. The program will prompt the user for the number of tickets. Write a loop which asks the user for the ages of the ticket holders, and then tells them the total cost of their movie tickets.

## Python Program Code

```python
# Movie Theater Ticket Pricing Program
# Pricing: Under 3 = free, 3-12 = $10, Over 12 = $15

# Get the number of tickets
num_tickets = int(input("How many tickets would you like to purchase? "))

total_cost = 0

# Loop to get each person's age and calculate cost
for i in range(1, num_tickets + 1):
    age = int(input(f"What is the age of ticket holder {i}? "))
    
    # Determine ticket price based on age
    if age < 3:
        ticket_price = 0
        print(f"Age {age}: Free")
    elif age <= 12:
        ticket_price = 10
        print(f"Age {age}: $10")
    else:
        ticket_price = 15
        print(f"Age {age}: $15")
    
    total_cost += ticket_price

# Display the total cost
print(f"\nTotal cost: ${total_cost}")
```

## Program Output
```
How many tickets would you like to purchase? 3
What is the age of ticket holder 1? 2
Age 2: Free
What is the age of ticket holder 2? 8
Age 8: $10
What is the age of ticket holder 3? 15
Age 15: $15

Total cost: $25
```

## Code and Output Screenshot
![movie_theater](movie_theater.png)

## Description

This program calculates the total cost of movie tickets based on the ages of ticket holders. It uses a loop to ask for the age of each person and applies the pricing rules: free for ages under 3, $10 for ages 3-12, and $15 for ages over 12. The program displays the price for each ticket and then shows the total cost at the end.

## GitHub Repository
File uploaded to: https://github.com/arthurcathey/CSC-121/blob/main/movie_theater.py

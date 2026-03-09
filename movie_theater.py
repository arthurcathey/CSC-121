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

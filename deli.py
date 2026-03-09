# 7-8. Deli Assignment

sandwich_orders = ["tuna", "turkey", "pastrami", "pb&j", "italian"]
finished_sandwiches = []

# Loop through sandwich orders and make each sandwich
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

# Print the finished sandwiches
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"  - {sandwich}")

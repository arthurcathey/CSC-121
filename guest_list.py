# Create a list of people to invite to dinner
guest_list = [
    "Alfred E Newman",
    "Sade",
    "Phil Leotardo"
]

# Print an invitation message to each guest
print(
    f"Dear {guest_list[0]}, I would be honored to have you "
    "join me for dinner."
)
print(
    f"Dear {guest_list[1]}, please join me for a special "
    "dinner gathering."
)
print(
    f"Dear {guest_list[2]}, it would be amazing to have "
    "you at dinner."
)

# Original guest list
guest_list = [
    "Alfred E Newman",
    "Sade",
    "Phil Leotardo"
]

# Inform guests about the bigger dinner table
print(
    "Good news! I found a bigger dinner table, so I can "
    "invite more guests.\n"
)

# Add new guests
guest_list.insert(0, "Elvis Presley")
guest_list.insert(2, "Mos Def")
guest_list.append("Dan Carlin")

# Sort the guest list alphabetically
guest_list.sort()

# Print sorted invitation messages
print("Here are the updated dinner invitations:\n")
for guest in guest_list:
    print(f"Dear {guest}, you are cordially invited to dinner.")

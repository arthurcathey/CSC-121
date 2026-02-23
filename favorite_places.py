# 6-9. Favorite Places

favorite_places = {
    "arthur": ["mountains", "beach", "library"],
    "maria": ["new york", "paris"],
    "james": ["tokyo"]
}

for name, places in favorite_places.items():
    formatted_places = ", ".join(place.title() for place in places)
    print(f"{name.title()}'s favorite places are: {formatted_places}.")

def report_points(alien_color):
    if alien_color == "green":
        print("Alien color: green. You earned 5 points.")
    elif alien_color == "yellow":
        print("Alien color: yellow. You earned 10 points.")
    else:
        print("Alien color: red. You earned 15 points.")


report_points("green")
report_points("yellow")
report_points("red")

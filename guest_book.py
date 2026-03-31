while True:
    name = input("Please enter your name (or 'quit' to exit): ")
    
    if name.lower() == 'quit':
        print("Thank you for signing the guest book!")
        break
    
    # Print greeting to screen
    print(f"Welcome, {name}! Thank you for visiting!")
    
    # Add entry to guest book file
    with open('guest_book.txt', 'a') as file:
        file.write(name + '\n')

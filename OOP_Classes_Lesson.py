"""
OOP Classes: Understanding Objects and Their Properties
Demonstrates the fundamental concepts of Object-Oriented Programming
"""

# ============================================================================
# CLASS DEFINITION: Dog
# ============================================================================

class Dog:
    """
    A class that represents a dog as an everyday object.
    Dogs are familiar animals that have distinct characteristics and behaviors.
    """
    
    # Attributes (Properties/Characteristics)
    # These define what data a Dog object stores
    
    def __init__(self, name, breed, age, color):
        """
        Initialize a Dog object with its attributes.
        
        Attributes:
            - name (str): The name of the dog
            - breed (str): The breed of the dog (e.g., "Labrador", "Golden Retriever")
            - age (int): The age of the dog in years
            - color (str): The color of the dog's fur (e.g., "brown", "black", "white")
            - is_trained (bool): Whether the dog has been trained
        """
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        self.is_trained = False  # Default: dog hasn't been trained yet
    
    # Methods (Behaviors/Actions)
    # These define what a Dog object can DO
    
    def bark(self):
        """The dog barks."""
        return f"{self.name} says: Woof! Woof!"
    
    def accelerate(self):
        """The dog runs or accelerates its movement."""
        return f"{self.name} is running quickly!"
    
    def fetch(self, item):
        """The dog fetches an item for you."""
        if self.is_trained:
            return f"{self.name} fetched the {item} successfully!"
        else:
            return f"{self.name} doesn't know how to fetch yet. Training is needed."
    
    def train(self):
        """Train the dog to follow commands."""
        self.is_trained = True
        return f"{self.name} has been trained and is now obedient!"
    
    def birthday(self):
        """Increment the dog's age by one year."""
        self.age += 1
        return f"Happy birthday to {self.name}! {self.name} is now {self.age} years old."
    
    def get_info(self):
        """Return a summary of the dog's information."""
        training_status = "trained" if self.is_trained else "not trained"
        return f"{self.name} is a {self.age}-year-old {self.color} {self.breed} that is {training_status}."


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    # Create instances (objects) of the Dog class
    dog1 = Dog("Max", "Labrador", 3, "golden")
    dog2 = Dog("Buddy", "Golden Retriever", 2, "light brown")
    
    print("=== Dog Information ===")
    print(dog1.get_info())
    print(dog2.get_info())
    
    print("\n=== Dog Actions ===")
    print(dog1.bark())
    print(dog1.accelerate())
    print(dog1.fetch("ball"))  # Try to fetch without training
    
    print("\n=== Training ===")
    print(dog1.train())
    print(dog1.fetch("ball"))  # Now try to fetch with training
    
    print("\n=== Birthday ===")
    print(dog1.birthday())


# ============================================================================
# ATTRIBUTES SUMMARY
# ============================================================================
"""
ATTRIBUTES (Data Types):
1. name (str) - The dog's name
2. breed (str) - The dog's breed
3. age (int) - The dog's age in years
4. color (str) - The dog's fur color
5. is_trained (bool) - Whether the dog has been trained
"""

# ============================================================================
# METHODS SUMMARY
# ============================================================================
"""
METHODS (Behaviors):
1. __init__() - Constructor that initializes a new Dog object
2. bark() - Makes the dog bark
3. accelerate() - Makes the dog run
4. fetch(item) - Makes the dog fetch an object (if trained)
5. train() - Trains the dog to be obedient
6. birthday() - Increases the dog's age by one year
7. get_info() - Returns information about the dog
"""


# ============================================================================
# THE IMPORTANCE OF CLASSES IN OOP: House Plants Example
# ============================================================================
"""
IMPORTANCE OF CLASSES IN OOP

Imagine you have a collection of house plants in your home. Each plant has
specific characteristics (type, height, water frequency, light requirement)
and behaviors (photosynthesis, growing, wilting). Without classes, you would
need to track each plant's data separately using individual variables:

    plant1_name = "Snake Plant"
    plant1_height = 18
    plant1_water_frequency = 3
    
    plant2_name = "Succulent"
    plant2_height = 6
    plant2_water_frequency = 2

This approach becomes messy and unmanageable very quickly. With classes, you 
can define a single "Plant" template that encapsulates all of these related
attributes and behaviors:

    class Plant:
        def __init__(self, name, height, water_frequency):
            self.name = name
            self.height = height
            self.water_frequency = water_frequency
        
        def water(self):
            # Logic to water the plant
            pass

Now you can create multiple plant objects easily, and each one automatically
has all the necessary properties and behaviors. This is the power of classes:
they allow us to model real-world objects, organize code logically, promote
code reuse, and make our programs more maintainable and scalable. Classes
transform scattered data and functions into cohesive, self-contained units
that mirror how we think about objects in the real world.
"""

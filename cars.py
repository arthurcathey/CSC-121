# 8-14. Cars Assignment

def make_car(manufacturer, model, **kwargs):
    """Store information about a car in a dictionary."""
    car_info = {
        'manufacturer': manufacturer,
        'model': model
    }
    car_info.update(kwargs)
    return car_info

# Call the function with required information and additional keyword arguments
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

car2 = make_car('toyota', 'camry', color='red', leather_seats=True)
print(car2)

car3 = make_car('honda', 'civic', color='black', sunroof=True)
print(car3)

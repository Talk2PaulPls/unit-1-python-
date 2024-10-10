# Task 1
def greet(name):
    """Prints a greeting message for the given name."""
    print(f"Hello, {name}!")

greet("Paul")  # Greet Paul

# Task 2
def square_number(num):
    """Returns the square of the given integer."""
    return num ** 2

print(f"Square of 4: {square_number(4)}")  # Output: 16

# Task 3
def is_even(num):
    """Checks if the given number is even."""
    return num % 2 == 0

print(f"Is 10 even? {is_even(10)}")  # True
print(f"Is 3 even? {is_even(3)}")    # False

# Task 4
def rectangle_area(length, width):
    """Calculates the area of a rectangle."""
    return length * width

print(f"Area of rectangle (5 x 3): {rectangle_area(5, 3)}")  # Output: 15

# Task 5
def celsius_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

print(f"0°C to Fahrenheit: {celsius_to_fahrenheit(0)}")  # Output: 32.0

# Task 6
def average(numbers):
    """Calculates the average of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0

print(f"Average of [1, 2, 3, 4, 5]: {average([1, 2, 3, 4, 5])}")  # Output: 3.0
print(f"Average of []: {average([])}")  # Output: 0

# Task 7
def total_calculator(price, quantity, discount=0):
    """Calculates total cost based on price and quantity, applying an optional discount."""
    total = price * quantity
    return total - total * (discount / 100) if discount else total

print(f"Total cost (100 x 2): {total_calculator(100, 2)}")  # Output: 200
print(f"Total cost (100 x 2 with 10% discount): {total_calculator(100, 2, 10)}")  # Output: 180

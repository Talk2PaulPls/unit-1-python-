# Task 1
def greet(name):
    print(f"Hello, {name}!")
# Task 2
def square_number(num):
    return num ** 2
# Task 3
def is_even(num):
    return num % 2 == 0
# Task 4
def rectangle_area(length, width):
    return length * width
# Task 5
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
# Task 6
def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
    # Task 7
def total_calculator(price, quantity, discount=0):
    total = price * quantity
    if discount:
        total -= total * (discount / 100)
    return total

# Task 1
my_float = 7.2
my_integer = int(my_float)
print("Original float value:", my_float)
print("Converted integer value:", my_integer)

# Task 2
user_input = input("Enter a number: ")
try:
    number = float(user_input)
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")
except ValueError:
    print("Invalid input. Please enter a valid number.")

# Task 3
integer_input = input("Enter an integer: ")
float_input = input("Enter a float: ")
try:
    integer_number = int(integer_input)
    float_number = float(float_input)
    
    addition = integer_number + float_number
    subtraction = integer_number - float_number
    multiplication = integer_number * float_number
    
    # Use a conditional to handle division by zero
    if float_number != 0:
        division = integer_number / float_number
    else:
        division = "undefined (division by zero)"
    
    print(f"Addition: {integer_number} + {float_number} = {addition}")
    print(f"Subtraction: {integer_number} - {float_number} = {subtraction}")
    print(f"Multiplication: {integer_number} * {float_number} = {multiplication}")
    print(f"Division: {integer_number} / {float_number} = {division}")

except ValueError:
    print("Invalid input. Please enter a valid integer and a valid float.")
my_var = "Paul B"
sentence = "Hello, {name}".format(name=my_var)

# Task 4
`# Fruit quantities dictionary
fruit_quantities = {
    'apples': 10,
    'bananas': 5,
    'oranges': 8,
    'grapes': 12,
    'pears': 7
}

# Check the quantity of a specific fruit
fruit_to_check = 'oranges'
if fruit_to_check in fruit_quantities:
    quantity = fruit_quantities[fruit_to_check]
    print(f"The quantity of {fruit_to_check} is: {quantity}")
else:
    print(f"{fruit_to_check} is not in the dictionary.")

# Display age
age = 77
sentence = f"You are {age}"
print(sentence)  # Corrected this line

# Task 5
numbers_string = "1, 2, 3, 4, 5"
numbers_list = numbers_string.split(", ")
numbers_tuple = tuple(map(int, numbers_list))
print("Original string:", numbers_string)
print("Converted tuple:", numbers_tuple)
nmb = 1 / 5
txt = f"Result: {nmb:.2f}"
print(txt)
nmb = 1 / 5
txt = "Result: {0:.2f}".format(nmb)
print(txt)
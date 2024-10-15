"""
Example 1: Division
"""
def divide_numbers(num1, num2):
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
        print("Result:", result)

# Example usage:
divide_numbers(10, 0)  # This will now print an error message
divide_numbers(10, 2)  # This will print "Result: 5.0"

"""
Example 2: Opening Files
"""
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print("Error: An I/O error occurred.")

# Example usage:
read_file("nonexistent.txt")  # This will now print an error message

"""
Example 3: List Items
"""

def get_item(lst, index):
    try:
        item = lst[index]
        print("Item:", item)
    except IndexError:
        print(f"Error: Index {index} is out of range for the list.")

# Example usage:
my_list = [1, 2, 3]
get_item(my_list, 5)  # This will now print an error message

"""
Example 4: Dictionaries
"""

def get_value(dictionary, key):
    try:
        value = dictionary[key]
        print("Value:", value)
    except KeyError:
        print(f"Error: The key '{key}' does not exist in the dictionary.")

# Example usage:
my_dict = {"a": 1, "b": 2}
get_value(my_dict, "c")  # This will now print an error message

"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: An I/O error occurred while reading the file.")

# Example usage:
process_file("example.txt")  # Adjust the filename as needed
# Task 1
# Creating my 4 elements
my_elements = ["Fire", "Water", "Air", "Earth"]
print("Original list:", my_elements)

# Task 2
# Add an element to the end of the list
my_elements.append("Time")
print("Updated list after appending 'Time':", my_elements)

# Task 3
# Removing an element from the list
my_elements.remove("Time")
print("Updated list after removing 'Time':", my_elements)

# Task 4
# Modify the second element in the list
my_elements[1] = "Wind"  # Change "Water" to "Wind"
print("Updated list after modification:", my_elements)

# Task 5 
my_elements.extend(["Space", "Soul", "Blood"])
print("Updated list after appending multiple elements:", my_elements)

# Task 6
del my_elements[2]  # Remove the element at index 2
print("Updated list after deleting element at index 2:", my_elements)

# Task 7
first_two_items = my_elements[:2]
print("First two items of the list:", first_two_items)

# Task 8
another_elements = ["Wood", "Metal"]
my_elements.extend(another_elements)
print("Updated list after extending with another list:", my_elements)
